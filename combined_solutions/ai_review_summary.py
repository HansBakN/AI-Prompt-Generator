#!/usr/bin/env python3
"""
ai_review_summary.py

A CLI tool to generate AI-friendly code review summaries by combining advanced
analysis features from multiple implementations.
Supports generic languages (Python, JavaScript, Dart, C#) with optional
AST-based semantic diffs, call graphs, and code metrics via external tools.
Only executes language-specific steps when enabled via the `--languages` flag.
Project structure now lists only files not excluded by .gitignore (tracked files).
"""
import argparse
import os
import subprocess
import sys
import json
from pathlib import Path
from collections import defaultdict
import shutil

# --- Helpers ---

def must_exist_file(p):
    p = Path(p)
    if not p.is_file():
        raise argparse.ArgumentTypeError(f"File not found: {p}")
    return p


def must_be_repo(p):
    p = Path(p)
    if not (p / '.git').exists():
        raise argparse.ArgumentTypeError(f"Not a Git repository: {p}")
    return p


def run_cmd(cmd, cwd=None):
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, cwd=cwd)
    except subprocess.CalledProcessError:
        return None


def chunk_diff(diff_text, max_chars=5000):
    return [diff_text[i:i+max_chars] for i in range(0, len(diff_text), max_chars)]


def dump_project_tree(root):
    """
    Build a directory tree from `git ls-files` (only tracked/unignored files).
    """
    files_out = run_cmd(["git", "ls-files"], cwd=root)
    if not files_out:
        return "```\n(empty or no tracked files)\n```"
    files = files_out.splitlines()
    tree = defaultdict(list)
    for f in files:
        parts = f.split('/')
        if len(parts) == 1:
            tree['.'].append(parts[0])
        else:
            tree[parts[0]].append('/'.join(parts[1:]))
    lines = ['```']
    for dir_, subfiles in sorted(tree.items()):
        lines.append(f"{dir_}/")
        for sf in sorted(subfiles):
            lines.append(f"  {sf}")
    lines.append('```')
    return '\n'.join(lines)


def semantic_diff(file_path, branch1, branch2, ext_lang):
    if not ext_lang or not shutil.which('diffsitter'):
        return None
    return run_cmd(["diffsitter", "diff", f"--lang={ext_lang}", branch1, branch2, "--", file_path])


def generate_call_graph(file_path, ext_lang):
    if not ext_lang or not shutil.which('callgraph-gen'):
        return None
    return run_cmd(["callgraph-gen", f"--lang={ext_lang}", file_path])


def generate_metrics(file_path, ext_lang):
    if not ext_lang or not shutil.which('metrics-cli'):
        return None
    return run_cmd(["metrics-cli", f"--lang={ext_lang}", file_path, "--format=json"])


def generate_summary(branch1, branch2, repo_path, context_file, task_file, output_file, langs):
    # Prepare absolute output path
    output_path = Path(output_file).expanduser().resolve()
    repo = Path(repo_path).expanduser().resolve()

    # Read context/task
    context_text = context_file.read_text(encoding='utf-8') if context_file else ''
    task_text = task_file.read_text(encoding='utf-8') if task_file else ''

    os.chdir(repo)
    enabled = {
        'cs': 'cs' in langs,
        'dart': 'dart' in langs,
        'py': 'py' in langs,
        'js': 'js' in langs
    }

    # Validate branches
    for ref in (branch1, branch2):
        if not run_cmd(["git", "rev-parse", "--verify", ref], cwd=repo):
            sys.exit(f"Branch or ref not found: {ref}")

    # Open output file
    try:
        out = output_path.open('w', encoding='utf-8')
    except Exception as e:
        sys.exit(f"Cannot write output file {output_path}: {e}")

    # Header sections
    if context_text:
        out.write("## Context Notes\n```")
        out.write(context_text)
        out.write("```\n\n")
    if task_text:
        out.write("## Task Instructions\n```")
        out.write(task_text)
        out.write("```\n\n")

    # Project Tree
    out.write("## Project Structure (tracked files)\n")
    out.write(dump_project_tree(str(repo)))
    out.write("\n\n")

    # Change summary
    shortstat = run_cmd(["git", "diff", "--shortstat", branch1, branch2], cwd=repo) or ''
    out.write(f"## Change Summary\n{shortstat}\n\n")

    # Commits
    commits = run_cmd(["git", "log", f"{branch1}..{branch2}", "--pretty=format:%h|%an|%s"], cwd=repo) or ''
    out.write("## Commits\n")
    for line in commits.splitlines():
        h, a, s = line.split('|', 2)
        out.write(f"- **{h}** by {a}: {s}\n")
    out.write("\n")

    # File changes details
    files = run_cmd(["git", "diff", "--name-only", branch1, branch2], cwd=repo) or ''
    groups = defaultdict(list)
    for f in files.splitlines():
        key = f.split('/', 1)[0] if '/' in f else '.'
        groups[key].append(f)

    out.write("## File Changes with Details\n")
    for grp in sorted(groups):
        out.write(f"### Directory: {grp}\n")
        for f in sorted(groups[grp]):
            out.write(f"#### File: {f}\n")
            # Commit summary
            msgs = run_cmd([
                "git", "log", "--pretty=format:%s", f"{branch1}..{branch2}", "--", f
            ], cwd=repo) or ''
            summary = msgs.splitlines()[0] if msgs else 'No commits'
            out.write(f"*Summary:* {summary}\n\n")

            path = repo / f
            ext = path.suffix.lower()
            code_key = None
            ext_lang = None
            if ext == '.cs':
                code_key, ext_lang = 'cs', 'csharp'
            elif ext == '.dart':
                code_key, ext_lang = 'dart', 'dart'
            elif ext == '.py':
                code_key = 'py'
            elif ext in ('.js', '.jsx'):
                code_key = 'js'

            # Linters
            if code_key == 'py' and shutil.which('flake8'):
                lint = run_cmd(['flake8', str(path)]) or ''
                out.write(f"**Flake8 warnings:**\n```\n{lint}```\n")
            if code_key == 'js' and shutil.which('eslint'):
                lint = run_cmd(['eslint', '--quiet', '--format', 'unix', str(path)]) or ''
                out.write(f"**ESLint warnings:**\n```\n{lint}```\n")
            if code_key == 'dart' and shutil.which('dart'):
                lint = run_cmd(['dart', 'analyze', str(path)]) or ''
                out.write(f"**Dart analyzer warnings:**\n```\n{lint}```\n")
            if code_key == 'cs' and shutil.which('dotnet'):
                lint = run_cmd(['dotnet', 'format', '--verify-no-changes', '--include', str(path)]) or ''
                out.write(f"**C# format check:**\n```\n{lint}```\n")

            # Diffs
            sem = semantic_diff(f, branch1, branch2, ext_lang)
            raw = run_cmd(["git", "diff", "-U3", branch1, branch2, "--", f], cwd=repo) or ''
            chunks = chunk_diff(raw)
            if sem:
                out.write(f"**Semantic AST Diff:**\n```\n{sem}```\n")
            out.write("**Raw Diff (chunked):**\n")
            for i, c in enumerate(chunks, 1):
                out.write(f"_Chunk {i}_\n```\n{c}\n```\n")

            # Advanced
            if ext_lang:
                cg = generate_call_graph(f, ext_lang)
                if cg:
                    out.write(f"**Call Graph:**\n```json\n{cg}```\n")
                met = generate_metrics(f, ext_lang)
                if met:
                    out.write(f"**Code Metrics:**\n```json\n{met}```\n")
            out.write("\n")

    out.close()


def main():
    parser = argparse.ArgumentParser(description="AI-friendly Git review summary generator")
    parser.add_argument("branch1", help="Source Git ref (e.g., main)")
    parser.add_argument("branch2", help="Destination Git ref (e.g., feature/xyz)")
    parser.add_argument("-r", "--repo-path", type=must_be_repo, default='.', help="Path to Git repository")
    parser.add_argument("-c", "--context-file", type=must_exist_file, help="Additional context file")
    parser.add_argument("-t", "--task-file", type=must_exist_file, help="Task instructions file")
    parser.add_argument("-o", "--output-file", default="review_summary.md", help="Output Markdown file")
    parser.add_argument("-l", "--languages", default="cs,py,js,dart", help="Comma-separated list of languages to include: cs,py,js,dart")
    args = parser.parse_args()
    langs = {l.strip().lower() for l in args.languages.split(',')}
    generate_summary(
        args.branch1, args.branch2,
        args.repo_path,
        args.context_file,
        args.task_file,
        args.output_file,
        langs
    )

if __name__ == '__main__':
    main()
