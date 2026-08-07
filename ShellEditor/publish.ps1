# Rebuild installer payloads and show git status for a Shell Editor release.
# Usage (from this folder):
#   1. Bump EDITOR_VERSION in .\ShellEditor (and migrators/SHELL_FORMAT_VERSION if needed)
#   2. Update .\dist\manifest.json to match
#   3. .\publish.ps1
#   4. From repo root: git add ShellEditor; git commit; git push
#   5. Optional: create GitHub release tag shell-editor-vX.Y.Z

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "Rebuilding ShellEditorInstaller..."
python .\build_installer.py

Write-Host ""
Write-Host "Repo status:"
git -C (Resolve-Path ..) status -sb

Write-Host ""
Write-Host "Next:"
Write-Host "  - Confirm EDITOR_VERSION matches dist\manifest.json editorVersion"
Write-Host "  - git add ShellEditor"
Write-Host "  - git commit -m 'Release Shell Editor vX.Y.Z'"
Write-Host "  - git push"
Write-Host "  - Optional tag: git tag shell-editor-vX.Y.Z; git push origin shell-editor-vX.Y.Z"
