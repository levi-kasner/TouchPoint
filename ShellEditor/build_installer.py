"""
Pack ShellEditor + templates into ShellEditorInstaller as zlib/base64 payloads.

Usage (from this folder):
  python build_installer.py

Uploads: run the generated ShellEditorInstaller Special Content script in TouchPoint.
"""
from __future__ import annotations

import base64
import pathlib
import re
import zlib

ROOT = pathlib.Path(__file__).resolve().parent
INSTALLER = ROOT / "ShellEditorInstaller"

# (content name, kind, source path relative to ROOT)
# kind: python | html | html_copy_from
PACKAGE = [
    ("ShellEditor", "python", "ShellEditor"),
    ("ShellLoginTemplate", "html", "ShellLoginTemplate.html"),
    ("ShellGivingTemplate", "html", "ShellGivingTemplate.html"),
    ("ShellRegistrationTemplate", "html", "ShellRegistrationTemplate.html"),
    ("ShellGivingWorkingCopy", "html_copy_from", "ShellGivingTemplate.html"),
]

MARKER_BEGIN = "# ==== BEGIN EMBEDDED PAYLOADS (generated; do not edit) ===="
MARKER_END = "# ==== END EMBEDDED PAYLOADS ===="


def pack_file(path: pathlib.Path) -> str:
    data = path.read_bytes()
    return base64.b64encode(zlib.compress(data, 9)).decode("ascii")


def build_payloads_block() -> str:
    lines = [MARKER_BEGIN, "PAYLOADS = {"]
    for name, kind, rel in PACKAGE:
        src = ROOT / rel
        if not src.exists():
            raise SystemExit("Missing package source: " + str(src))
        b64 = pack_file(src)
        # Keep lines readable / under common editor limits.
        chunk = 120
        parts = [b64[i : i + chunk] for i in range(0, len(b64), chunk)]
        lines.append("    %r: {" % name)
        lines.append("        'kind': %r," % kind)
        lines.append("        'data': (")
        for part in parts:
            lines.append("            %r" % part)
        lines.append("        ),")
        lines.append("    },")
    lines.append("}")
    lines.append(MARKER_END)
    return "\n".join(lines) + "\n"


def main() -> None:
    text = INSTALLER.read_text(encoding="utf-8")
    block = build_payloads_block()
    if MARKER_BEGIN in text and MARKER_END in text:
        text = re.sub(
            re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n?",
            block,
            text,
            count=1,
            flags=re.S,
        )
    else:
        raise SystemExit("Installer is missing payload markers")
    INSTALLER.write_text(text, encoding="utf-8", newline="\n")
    print("Updated", INSTALLER)
    print("Payloads:", ", ".join(n for n, _, _ in PACKAGE))


if __name__ == "__main__":
    main()
