# TouchPoint

Custom solutions for churches using the TouchPoint ChMS.

## Shell Editor

Source of truth: [`ShellEditor/`](ShellEditor/)

| Path | Purpose |
|---|---|
| `ShellEditor/ShellEditor` | Editor script (TouchPoint Special Content) |
| `ShellEditor/ShellEditorInstaller` | Packaged installer (upload this to churches) |
| `ShellEditor/*Template.html` | Registration / giving / login shell templates |
| `ShellEditor/dist/manifest.json` | Public update-check manifest |
| `ShellEditor/build_installer.py` | Rebuilds installer payloads from sources |
| `ShellEditor/publish.ps1` | Rebuild helper before commit/push |

Update check URL used by the editor:

`https://raw.githubusercontent.com/levi-kasner/TouchPoint/main/ShellEditor/dist/manifest.json`

### Publish a new version

1. Edit files under `ShellEditor/`
2. Bump `EDITOR_VERSION` in `ShellEditor/ShellEditor`
3. Update `ShellEditor/dist/manifest.json` (`editorVersion`, notes, dates)
4. Run `ShellEditor/publish.ps1` (rebuilds the installer)
5. From this repo root:

```powershell
git add ShellEditor
git commit -m "Release Shell Editor vX.Y.Z"
git push
```

6. Optional release tag: `shell-editor-vX.Y.Z`
