"""Embed VirtuousRaiseImport into InstallVirtuousRaiseImport as base64/zlib.

Usage (from this folder):
  python build_installer.py

Upload InstallVirtuousRaiseImport as TouchPoint Special Content (Python).
"""
from __future__ import annotations

import base64
import pathlib
import re
import zlib

ROOT = pathlib.Path(__file__).resolve().parent
IMPORT = ROOT / "VirtuousRaiseImport"
INSTALLER = ROOT / "InstallVirtuousRaiseImport"

MARKER_BEGIN = "# ==== BEGIN EMBEDDED IMPORT (generated; do not edit) ===="
MARKER_END = "# ==== END EMBEDDED IMPORT ===="


def build_import_block(import_text: str) -> str:
    # Base64/zlib avoids r''' escape corruption (e.g. \\n becoming real newlines).
    raw = import_text.encode("utf-8")
    b64 = base64.b64encode(zlib.compress(raw, 9)).decode("ascii")
    chunk = 120
    parts = [b64[i : i + chunk] for i in range(0, len(b64), chunk)]
    lines = [
        MARKER_BEGIN,
        "importBody = zlib.decompress(base64.b64decode(",
        "    (",
    ]
    for part in parts:
        lines.append("        %r" % part)
    lines.append("    )")
    lines.append(")).decode('utf-8')")
    lines.append(MARKER_END)
    return "\n".join(lines) + "\n"


def main() -> None:
    import_text = IMPORT.read_text(encoding="utf-8")
    installer = INSTALLER.read_text(encoding="utf-8")
    block = build_import_block(import_text)
    if MARKER_BEGIN not in installer or MARKER_END not in installer:
        raise SystemExit("Installer is missing embed markers")
    installer = re.sub(
        re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n?",
        block,
        installer,
        count=1,
        flags=re.S,
    )
    # Ensure decode helpers are imported at top of installer.
    if "import zlib" not in installer.split(MARKER_BEGIN, 1)[0]:
        installer = installer.replace(
            "import json\nimport traceback\n",
            "import base64\nimport json\nimport traceback\nimport zlib\n",
            1,
        )
    INSTALLER.write_text(installer, encoding="utf-8", newline="\n")
    print("Updated", INSTALLER)


if __name__ == "__main__":
    main()
