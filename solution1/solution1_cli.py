
#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os
import shutil
from pathlib import Path
from collections import defaultdict

from git_ai_review.git_wrapper import must_exist_file, must_be_repo, run_git

def generate_review(
    ctx_file: Path,
    task_file: Path | None,
    out_file: str,
    src: str,
    dst: str,
    repo_path: Path
) -> None:
    """
    Generate an AI-friendly review summary for the changes between two Git refs.
    """
    # Read optional AI task instructions and feature context
    task_text = task_file.read_text(encoding="utf-8") if task_file else ""
    context = ctx_file.read_text(encoding="utf-8")

    # Ensure both source and destination refs exist
    for ref in (src, dst):
        try:
            subprocess.run(
                ["git", "rev-parse", "--verify", ref],
                cwd=str(repo_path), capture_output=True, text=True, check=True
            )
        except subprocess.CalledProcessError:
            sys.exit(f"Branch or ref not found: {ref}")

    # Determine repository root and name
    top = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=str(repo_path), capture_output=True, text=True, check=True
    ).stdout.strip()
    repo_root = Path(top).resolve()
    print(f"Repository path:  {repo_root}")
    print(f"Repository name:  {repo_root.name}")

    # Fetch and parse remote origin URL
    try:
        remote_url = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=str(repo_path), capture_output=True, text=True, check=True
        ).stdout.strip()
    except subprocess.CalledProcessError:
        sys.exit("Failed to get remote URL for 'origin'")
    url = remote_url[:-4] if remote_url.endswith(".git") else remote_url
    path = url.split(":", 1)[1] if url.startswith("git@") else url.split("/", 3)[-1]
    remote_repo_name = Path(path).name
    print(f"Remote URL:        {remote_url}")
    print(f"Remote repo name:  {remote_repo_name}\n")

    # Build the initial sections with task, context, stats, and commit list
    parts = [
        task_text,
        context,
        "\n--- STAT SUMMARY ---",
        run_git(["diff", "--stat"], src, dst, repo_path),
        "\n--- COMMITS ---",
        run_git(["log", "--oneline"], src, dst, repo_path)
    ]

    # Group changed files by their top-level directory
    changed = run_git(["diff", "--name-only"], src, dst, repo_path).splitlines()
    groups = defaultdict(list)
    for f in changed:
        key = f.split(os.sep, 1)[0] if os.sep in f else "."
        groups[key].append(f)

    # For each group, add per-file summaries, lint warnings, and diffs
    for group, files in sorted(groups.items()):
        parts.append(f"\n## Directory: {group}")
        for f in files:
            parts.append(f"\n### File: {f}")
            # Last commit message affecting this file
            msgs = run_git(
                ["log", "--pretty=format:%s"], src, dst, repo_path,
                extra_args=["--", f]
            ).splitlines()
            parts.append(f"*Summary:* {msgs[0] if msgs else 'No commits'}")

            # Run language-specific linters if available
            file_path = repo_root / f
            if f.endswith(".py") and shutil.which("flake8"):
                lint = subprocess.run(
                    ["flake8", "--format=%(row)d:%(col)d %(code)s %(text)s", str(file_path)],
                    cwd=str(repo_root), capture_output=True, text=True
                ).stdout.strip().splitlines() or ["None"]
                parts.append("**Flake8 warnings:**")
                parts.extend(lint)
            elif f.endswith(".js") and shutil.which("eslint"):
                lint = subprocess.run(
                    ["eslint", "--quiet", "--format", "unix", str(file_path)],
                    cwd=str(repo_root), capture_output=True, text=True
                ).stdout.strip().splitlines() or ["None"]
                parts.append("**ESLint warnings:**")
                parts.extend(lint)
            elif f.endswith(".dart") and shutil.which("dart"):
                analysis = subprocess.run(
                    ["dart", "analyze", str(file_path)],
                    cwd=str(repo_root), capture_output=True, text=True
                ).stdout.strip().splitlines() or ["None"]
                parts.append("**Dart analyzer warnings:**")
                parts.extend(analysis)
            elif f.endswith(".cs") and shutil.which("dotnet"):
                cs_out = subprocess.run(
                    ["dotnet", "format", "--verify-no-changes", "--include", str(file_path)],
                    cwd=str(repo_root), capture_output=True, text=True
                ).stdout.strip().splitlines() or ["None"]
                parts.append("**dotnet format warnings:**")
                parts.extend(cs_out)

            # Include the diff with function context
            diff = run_git(
                ["diff", "--function-context"], src, dst, repo_path,
                extra_args=["--", f]
            )
            parts += ["```diff", diff, "```"]

    # Write the assembled review to the output file
    try:
        Path(out_file).write_text("\n".join(parts), encoding="utf-8")
    except OSError as e:
        sys.exit(f"Failed to write output file {out_file}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Generate an AI-friendly Git review summary"
    )
    parser.add_argument(
        "-c", "--context-file", type=must_exist_file, required=True,
        help="Path to the .txt file with feature context"
    )
    parser.add_argument(
        "-t", "--task-file", type=must_exist_file,
        help="Path to the .txt file with AI task instructions"
    )
    parser.add_argument(
        "-o", "--output-file", type=str, required=True,
        help="Output file for the review"
    )
    parser.add_argument(
        "-s", "--source", type=str, required=True,
        help="Source Git ref (e.g. origin/main)"
    )
    parser.add_argument(
        "-d", "--destination", type=str, required=True,
        help="Destination Git ref (e.g. feature/xyz)"
    )
    parser.add_argument(
        "-r", "--repo-path", type=must_be_repo, default=".",
        help="Path to the Git repository (default: current dir)"
    )

    args = parser.parse_args()
    generate_review(
        ctx_file=args.context_file,
        task_file=args.task_file,
        out_file=args.output_file,
        src=args.source,
        dst=args.destination,
        repo_path=args.repo_path
    )

if __name__ == "__main__":
    main()
