# Virtuous Raise Import

TouchPoint integration that imports gifts from Virtuous Raise into Contribution batches (bundle header type code `VRDI`).

- **Import script:** `VirtuousRaiseImport` (wired into `MorningBatch`)
- **Installer:** `/PyScriptForm/InstallVirtuousRaiseImport`

You need the **Admin** or **SpecialContentFull** role.

---

## Install

### 1. Get the installer script

Copy the latest `InstallVirtuousRaiseImport` from this folder:

https://raw.githubusercontent.com/levi-kasner/TouchPoint/main/VirtuousRaiseImport/InstallVirtuousRaiseImport

### 2. Add it as Special Content in TouchPoint

1. Go to **Admin → Advanced → Special Content → Python Scripts**.
2. Create a new Python script named exactly **`InstallVirtuousRaiseImport`**.
3. Paste the installer contents and save.

### 3. Prerequisites

Before running the installer, create a **Bundle Header Type** with Code **`VRDI`** (Virtuous Raise Donor Import or similar description).

### 4. Run the installer wizard

1. Open **`/PyScriptForm/InstallVirtuousRaiseImport`**.
2. Enter and verify the Virtuous / Raise API key.
3. Set the import start-date floor.
4. Choose the anonymous giver people record.
5. Optionally enable email notices (to/from people must have a primary email).
6. Install / update to write `VirtuousRaiseImport` and add its call to `MorningBatch`.

---

## Settings

| Setting | Purpose |
|---|---|
| `Virtuous API Key` | Raise API bearer token |
| `Virtuous Import Start Date` | Permanent lookback floor (`yyyy-MM-dd`) |
| `Virtuous Import From Start Date` | One-shot reachback to the floor (`true` then cleared after a run) |
| `Virtuous Anonymous Giver Id` | PeopleId used for anonymous gifts |
| `Virtuous Send Email Notices` | `true` to email after each run |
| `Virtuous Email Notice People Id` | Recipient PeopleId |
| `Virtuous Email Notices Sender Id` | Sender PeopleId |

---

## Update

1. Replace Special Content **`InstallVirtuousRaiseImport`** with the latest file from this repo.
2. Open `/PyScriptForm/InstallVirtuousRaiseImport` and run **Install / update**.

Or edit sources here, run `python build_installer.py`, then upload the regenerated installer.

---

## Uninstall

From the installer done page, choose **Uninstall Virtuous Raise Import**. That clears the settings, removes the `MorningBatch` call, deletes `VirtuousRaiseImport`, and optionally deletes the installer.

Imported contribution history is not removed. For cleanup of VRDI batch data during testing, see [`DeleteImportData.sql`](DeleteImportData.sql).

---

## Develop

| Path | Purpose |
|---|---|
| `VirtuousRaiseImport` | Morning-batch import script |
| `InstallVirtuousRaiseImport` | Packaged installer (upload this to churches) |
| `build_installer.py` | Embeds the import script into the installer |
| `DeleteImportData.sql` | Optional SQL to inspect/delete VRDI import data |

```powershell
python build_installer.py
```
