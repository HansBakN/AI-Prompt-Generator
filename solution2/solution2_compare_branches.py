#!/usr/bin/env python3
"""
compare_branches.py

A CLI tool to summarize changes between two Git branches with enhanced context for AI review.
Supports C# and Dart/Flutter projects.

Features implemented:
 1. Project structure tree output
 2. Dependency graph export (dotnet & dart)
 3. Static analysis summaries (dotnet build warnings & dart analyze)
 4. AST-based semantic diffs (via external `diffsitter` CLI)
 5. Call graph export (via external `callgraph-gen` CLI)
 6. Code metrics (via external `metrics-cli`)
 7. Multi-level diff chunking for later summarization

Usage:
  python compare_branches.py <branch1> <branch2> [options]

Run `python compare_branches.py --help` for details.
"""
import argparse
import os
import subprocess
import sys
import json
import xml.etree.ElementTree as ET
from pathlib import Path

# === Helpers ===

def run_cmd(cmd, cwd=None):
    """
    Run shell command and return stdout, exit on error.
    """
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, cwd=cwd)
        return out
    except subprocess.CalledProcessError as e:
        print(f"[Error] Command failed: {' '.join(cmd)}", file=sys.stderr)
        print(e.output, file=sys.stderr)
        return None

# === Feature 1: Project Structure ===

def dump_project_tree(root):
    """
    Return a markdown-formatted tree of the project structure.
    """
    lines = ["```"]
    for dirpath, dirs, files in os.walk(root):
        depth = dirpath.replace(root, '').count(os.sep)
        indent = '  ' * depth
        lines.append(f"{indent}{os.path.basename(dirpath)}/")
        for f in files:
            lines.append(f"{indent}  {f}")
    lines.append("```")
    return '\n'.join(lines)

# === Feature 2: Dependency Graph ===

def dump_dotnet_deps(repo_path):
    """
    Run `dotnet list package --include-transitive --format json` if available.
    """
    out = run_cmd(["dotnet", "list", "package", "--include-transitive", "--format", "json"], cwd=repo_path)
    if not out:
        return None
    data = json.loads(out)
    return json.dumps(data, indent=2)

def dump_dart_deps(repo_path):
    """
    Run `dart pub deps --style=json` for Dart/Flutter projects.
    """
    out = run_cmd(["dart", "pub", "deps", "--style=json"], cwd=repo_path)
    return out

# === Feature 3: Static Analysis ===

def dump_dotnet_analysis(repo_path):
    """
    Capture warnings/errors from `dotnet build`.
    """
    out = run_cmd(["dotnet", "build", "-warnaserror:false"], cwd=repo_path)
    return out

def dump_dart_analysis(repo_path):
    """
    Run `dart analyze` and capture issues.
    """
    out = run_cmd(["dart", "analyze"], cwd=repo_path)
    return out

# === Feature 4: Semantic AST Diffs ===

def semantic_diff(file_path, branch1, branch2, lang):
    """
    Use external `diffsitter` CLI for AST diff. lang: 'csharp' or 'dart'
    """
    cmd = ["diffsitter", "diff", f"--lang={lang}", f"{branch1}", f"{branch2}", "--", file_path]
    return run_cmd(cmd)

# === Feature 5: Call Graphs ===

def generate_call_graph(file_path, lang):
    """
    Use external `callgraph-gen` CLI. lang: 'csharp' or 'dart'
    """
    cmd = ["callgraph-gen", f"--lang={lang}", file_path]
    return run_cmd(cmd)

# === Feature 6: Code Metrics ===

def generate_metrics(file_path, lang):
    """
    Use external `metrics-cli` to compute complexity, etc.
    """
    cmd = ["metrics-cli", f"--lang={lang}", file_path, "--format=json"]
    return run_cmd(cmd)

# === Feature 7: Chunked Diffs ===

def chunk_diff(diff_text, max_chars=5000):
    """
    Split diff_text into chunks <= max_chars.
    """
    chunks = []
    for i in range(0, len(diff_text), max_chars):
        chunks.append(diff_text[i:i+max_chars])
    return chunks

# === Main CLI ===

def parse_args():
    p = argparse.ArgumentParser(description="Enhanced Git diff summary for AI review")
    p.add_argument("branch1")
    p.add_argument("branch2")
    p.add_argument("-r", "--repo-path", default='.', help="Path to Git repo")
    p.add_argument("-c", "--context-file", help="Context notes file")
    p.add_argument("-t", "--task-file", help="Task instructions file")
    p.add_argument("-o", "--output", default="changes_summary.md", help="Output Markdown file")
    return p.parse_args()

def main():
    args = parse_args()
    repo = Path(args.repo_path).resolve()
    os.chdir(repo)

    # verify .git exists
    if not (repo / '.git').exists():
        print("Error: Not a Git repository", file=sys.stderr)
        sys.exit(1)

    out = open(args.output, 'w', encoding='utf-8')

    # --- Optional: include user-provided files ---
    if args.context_file and os.path.isfile(args.context_file):
        out.write("## Context\n```")
        out.write(Path(args.context_file).read_text())
        out.write("```\n\n")
    if args.task_file and os.path.isfile(args.task_file):
        out.write("## Task Instructions\n```")
        out.write(Path(args.task_file).read_text())
        out.write("```\n\n")

    # --- Project tree ---
    out.write("## Project Structure\n")
    out.write(dump_project_tree(str(repo)))
    out.write("\n\n")

    # --- Dependencies ---
    out.write("## Dependency Graphs\n")
    cs_deps = dump_dotnet_deps(str(repo))
    if cs_deps:
        out.write("### .NET Packages\n```json\n" + cs_deps + "```\n")
    dart_deps = dump_dart_deps(str(repo))
    if dart_deps:
        out.write("### Dart/Flutter Packages\n```json\n" + dart_deps + "```\n")
    out.write("\n")

    # --- Static Analysis ---
    out.write("## Static Analysis\n")
    dotnet_ana = dump_dotnet_analysis(str(repo))
    if dotnet_ana:
        out.write("### .NET Build Warnings & Errors\n```")
        out.write(dotnet_ana)
        out.write("```\n")
    dart_ana = dump_dart_analysis(str(repo))
    if dart_ana:
        out.write("### Dart Analyzer Output\n```")
        out.write(dart_ana)
        out.write("```\n")
    out.write("\n")

    # --- Shortstat & commits ---
    shortstat = run_cmd(["git", "diff", "--shortstat", args.branch1, args.branch2])
    out.write("## Summary of Changes\n" + (shortstat or "") + "\n\n")

    commits = run_cmd(["git", "log", f"{args.branch1}..{args.branch2}", "--pretty=format:%h|%an|%s"])
    out.write("## Commits\n")
    if commits:
        for line in commits.splitlines():
            h, a, s = line.split('|', 2)
            out.write(f"- **{h}** by {a}: {s}\n")
    else:
        out.write("No new commits.\n")
    out.write("\n")

    # --- File diffs with enhancements ---
    out.write("## File Changes with Enhanced Context\n")
    files = run_cmd(["git", "diff", "--name-only", args.branch1, args.branch2]).splitlines()
    for f in files:
        ext = Path(f).suffix.lower()
        out.write(f"### {f}\n")

        # raw diff
        raw = run_cmd(["git", "diff", "-U3", args.branch1, args.branch2, "--", f]) or ""

        # semantic diff
        sem = None
        lang = None
        if ext == '.cs':
            lang = 'csharp'
        elif ext == '.dart':
            lang = 'dart'
        if lang:
            sem = semantic_diff(f, args.branch1, args.branch2, lang)

        # call graph
        cg = None
        if lang:
            cg = generate_call_graph(f, lang)

        # metrics
        met = None
        if lang:
            met = generate_metrics(f, lang)

        # chunk raw diff
        chunks = chunk_diff(raw)

        # write summaries
        if sem:
            out.write("#### Semantic AST Diff\n```")
            out.write(sem)
            out.write("```\n")
        out.write("#### Raw Diff (chunked)\n")
        for i, c in enumerate(chunks, 1):
            out.write(f"##### Chunk {i}\n```")
            out.write(c)
            out.write("```\n")

        if cg:
            out.write("#### Call Graph\n```json\n" + cg + "```\n")
        if met:
            out.write("#### Code Metrics\n```json\n" + met + "```\n")
        out.write("\n")

    out.close()

if __name__ == '__main__':
    main()
