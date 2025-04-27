# git-ai-review

Generate an AI-friendly Git review summary between two refs.

## Features

- Generates summaries of diff stats, commits, per-file summaries, lint warnings, and function-context diffs.
- Supports Python, JavaScript, Dart, and C# static analysis.
- Allows custom AI task instructions and feature context.
- Outputs Markdown-ready text for prompt injection.

## Installation

### macOS / Linux

``` bash
brew install git node dart-sdk dotnet-sdk
npm install -g eslint
python3 -m pip install .
```

## Windows (PowerShell) 
```powershell
choco install git dart-sdk -y
winget install --id Microsoft.dotnet.SDK.8 -e
npm install -g eslint
pip install .
```

## Usage 
```bash
generate-review \
  --context-file feature.txt \
  --task-file task.txt \
  --source origin/main \
  --destination feature/xyz \
  --output-file review.md
```

## Example (Python)
```
from git_ai_review.cli import generate_review
from pathlib import Path

generate_review(
    ctx_file=Path("feature.txt"),
    task_file=Path("task.txt"),
    out_file="review.md",
    src="origin/main",
    dst="feature/xyz",
    repo_path=Path(".")
)
````

