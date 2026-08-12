# TouchPoint

Custom solutions for churches using the TouchPoint ChMS.

## Projects

| Folder | Purpose |
|---|---|
| [`ShellEditor/`](ShellEditor/) | Live shell editor for registration, giving, and login |
| [`VirtuousRaiseImport/`](VirtuousRaiseImport/) | Virtuous Raise gift import into TouchPoint batches |

---

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

---

## Virtuous Raise Import

Source of truth: [`VirtuousRaiseImport/`](VirtuousRaiseImport/)

| Path | Purpose |
|---|---|
| `VirtuousRaiseImport/VirtuousRaiseImport` | Morning-batch import script |
| `VirtuousRaiseImport/InstallVirtuousRaiseImport` | Packaged installer (upload this to churches) |
| `VirtuousRaiseImport/build_installer.py` | Embeds the import script into the installer |
| `VirtuousRaiseImport/DeleteImportData.sql` | Optional cleanup SQL for VRDI test data |

Installer raw URL:

`https://raw.githubusercontent.com/levi-kasner/TouchPoint/main/VirtuousRaiseImport/InstallVirtuousRaiseImport`

### Publish an update

1. Edit files under `VirtuousRaiseImport/`
2. Run `python VirtuousRaiseImport/build_installer.py`
3. From this repo root:

```powershell
git add VirtuousRaiseImport
git commit -m "Update Virtuous Raise Import"
git push
```
