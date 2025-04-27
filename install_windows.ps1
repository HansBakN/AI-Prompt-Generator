#!/usr/bin/env pwsh
Set-ExecutionPolicy Bypass -Scope Process -Force

# Install Chocolatey if missing
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
  Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# Install Git and Dart SDK
choco install git -y
choco install dart-sdk -y

# Install .NET SDK via Winget
winget install --id Microsoft.dotnet.SDK.8 -e

# Install ESLint globally
npm install -g eslint

# Install Python package
pip install .
