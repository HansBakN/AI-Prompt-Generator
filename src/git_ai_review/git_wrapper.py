import argparse
import subprocess
import sys
from pathlib import Path

def must_exist_file(p):
    """
    Ensure the given path points to an existing file.
    """
    p = Path(p)
    if not p.is_file():
        raise argparse.ArgumentTypeError(f"File not found: {p}")
    return p

def must_be_repo(p):
    """
    Ensure the given path is inside a Git repository.
    """
    p = Path(p)
    if not p.is_dir():
        raise argparse.ArgumentTypeError(f"Not a directory: {p}")
    res = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=str(p), capture_output=True, text=True
    )
    if res.returncode != 0 or res.stdout.strip() != "true":
        raise argparse.ArgumentTypeError(f"Not a Git repo: {p}")
    return p

def run_git(cmd, src, dst, repo_path, extra_args=None):
    """
    Run a git command comparing src..dst and return its stdout, exiting on error.
    """
    args = ["git"] + cmd + [f"{src}..{dst}"]
    if extra_args:
        args += extra_args
    try:
        cp = subprocess.run(
            args,
            cwd=str(repo_path),
            capture_output=True, text=True, check=True
        )
        return cp.stdout.strip()
    except subprocess.CalledProcessError as e:
        sys.exit(f"Git command failed ({e.cmd}):\n{e.stderr.strip()}")
