#!/usr/bin/env bash
set -e

# Install Homebrew packages
brew install git node dart-sdk dotnet-sdk

# Install ESLint globally
npm install -g eslint

# Install Python package into current environment
python3 -m pip install .
