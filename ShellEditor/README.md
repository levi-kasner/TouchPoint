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

1. Go to **Admin → Advanced → Special Content → Python Scripts**.
2. Create a new Python script named exactly **`ShellEditorInstaller`**.
3. Paste the installer contents and save.

### 3. Run the installer wizard

1. Open **`/PyScriptForm/ShellEditorInstaller`** on your church database.
2. Click **Start installation**.
3. Click **Install / update files** to create:
   - `ShellEditor` (Python)
   - `ShellLoginTemplate`
   - `ShellGivingTemplate`
   - `ShellRegistrationTemplate`
   - `ShellGivingWorkingCopy`
4. Complete the **Registration** step (required). Choose an existing registration form involvement for the editor preview (preferably a testing form, not one published externally). You can create one in Involvement Search, return to the installer, refresh the list, and select it.
5. Optionally configure **Giving**, **Login**, and the Admin reports menu link.
6. When finished, open **Shell Editor** from the success page, or go to `/PyScriptForm/ShellEditor`.

**Notes**

- Registration preview setup is required (select an existing registration form involvement). Giving and login modules can be skipped and installed later from the editor or installer (`?focus=giving` / `?focus=login`).
- HTML templates that already exist are left unchanged. The `ShellEditor` Python script is always written from the installer package.

---

## Update

When a newer version is published, Shell Editor shows an **Update available** banner (it checks [`dist/manifest.json`](dist/manifest.json) on GitHub).

### From the editor banner (recommended)

1. Open `/PyScriptForm/ShellEditor`.
2. Click **Update now** on the banner.

That downloads the latest `ShellEditorInstaller` from GitHub, refreshes the installer Special Content, and updates the `ShellEditor` script automatically. The page then reloads on the new version.

Custom shells you created are kept; they migrate automatically when opened. Stock HTML templates that already exist are not overwritten.

### Manual update (optional)

If the in-editor update cannot reach GitHub, you can still update manually:

1. Copy the latest `ShellEditorInstaller` from  
   https://raw.githubusercontent.com/levi-kasner/TouchPoint/main/ShellEditor/ShellEditorInstaller
2. Replace the body of Special Content **`ShellEditorInstaller`** and save.
3. Open `/PyScriptForm/ShellEditorInstaller` and click **Install / update files**.

---

## After install

| Item | URL / location |
|------|----------------|
| Shell Editor | `/PyScriptForm/ShellEditor` |
| Installer (add skipped modules later) | `/PyScriptForm/ShellEditorInstaller` |
| Menu (if enabled) | Admin reports menu → **Shell Editor** |

Editable shells use Content Keyword **`Shell`**. Kind (registration / giving / login) is identified by a marker comment at the top of the HTML body.
