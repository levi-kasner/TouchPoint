# Shell Editor

Shell Editor is a TouchPoint Special Content tool for editing registration, giving, and login shells with a live preview.

- **Editor:** `/PyScriptForm/ShellEditor`
- **Installer:** `/PyScriptForm/ShellEditorInstaller`

You need the **Admin** or **SpecialContentFull** role.

---

## Install

### 1. Get the installer script

Download or copy the latest `ShellEditorInstaller` from this folder:

https://raw.githubusercontent.com/levi-kasner/TouchPoint/main/ShellEditor/ShellEditorInstaller

Or open the file in this repo and copy its full contents.

### 2. Add it as Special Content in TouchPoint

1. Go to **Admin → Special Content → Python Scripts** (or the equivalent Special Content screen for Python).
2. Create a new Python script named exactly **`ShellEditorInstaller`**.
3. Paste the installer contents and save.

### 3. Run the installer wizard

1. Open **`/PyScriptForm/ShellEditorInstaller`** on your church database.
2. Click **Start installation**.
3. Click **Install / verify files** to create:
   - `ShellEditor` (Python)
   - `ShellLoginTemplate`
   - `ShellGivingTemplate`
   - `ShellRegistrationTemplate`
   - `ShellGivingWorkingCopy`
4. Complete the **Registration** step (required). The installer creates a preview involvement named **Shell Editor Preview** by copying settings from an involvement you choose.
5. Optionally configure **Giving**, **Login**, and the Admin reports menu link.
6. When finished, open **Shell Editor** from the success page, or go to `/PyScriptForm/ShellEditor`.

**Notes**

- Existing Special Content files are **not** overwritten. If a name already exists, that file is left as-is.
- Registration preview setup is required. Giving and login modules can be skipped and installed later from the editor or installer (`?focus=giving` / `?focus=login`).

---

## Update

When a newer version is published, Shell Editor can show an **Update available** banner (it checks [`dist/manifest.json`](dist/manifest.json) on GitHub). Custom shells you created are kept; they migrate automatically when opened in the editor.

The installer **never overwrites** existing files, so updating the editor means replacing the `ShellEditor` script, then re-running the installer to recreate it.

### 1. Get the latest installer

Copy the current `ShellEditorInstaller` from:

https://raw.githubusercontent.com/levi-kasner/TouchPoint/main/ShellEditor/ShellEditorInstaller

Release notes and version info are in [`dist/manifest.json`](dist/manifest.json) and on the matching GitHub release (for example `shell-editor-v1.0.0`).

### 2. Refresh the installer in TouchPoint

1. Open Special Content **`ShellEditorInstaller`**.
2. Replace its body with the latest installer text and save.

### 3. Replace the editor script

1. In Special Content, delete (or rename) the existing **`ShellEditor`** Python script.
2. Open `/PyScriptForm/ShellEditorInstaller`.
3. Run **Install / verify files** so `ShellEditor` is created again from the embedded package.

You do **not** need to redo registration / giving / login setup unless you want to change those options. Preview settings already stored on the database are left alone.

### Optional: refresh stock templates

Only do this if you want the built-in template files reset to the package versions. Your named custom shells (Content Keyword `Shell`) are separate and are not removed by this.

1. Delete any of these Special Content items you want refreshed:
   - `ShellLoginTemplate`
   - `ShellGivingTemplate`
   - `ShellRegistrationTemplate`
   - `ShellGivingWorkingCopy` (only if you understand this may be the live giving page skin)
2. Run **Install / verify files** again.

If giving is live on `ShellGivingWorkingCopy`, prefer leaving that file alone unless you intentionally want to reset it.

---

## After install

| Item | URL / location |
|------|----------------|
| Shell Editor | `/PyScriptForm/ShellEditor` |
| Installer (add skipped modules later) | `/PyScriptForm/ShellEditorInstaller` |
| Menu (if enabled) | Admin reports menu → **Shell Editor** |

Editable shells use Content Keyword **`Shell`**. Kind (registration / giving / login) is identified by a marker comment at the top of the HTML body.
