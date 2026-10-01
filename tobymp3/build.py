#!/usr/bin/env python3
"""Genera TOBYMP3.html: un único archivo portable con lamejs incrustado."""
from pathlib import Path

here = Path(__file__).parent
template = (here / "src" / "tobymp3.template.html").read_text(encoding="utf-8")
lame = (here / "vendor" / "lame.min.js").read_text(encoding="utf-8")
assert "</script" not in lame.lower()
out = template.replace("/*__LAMEJS__*/", lame)
(here / "TOBYMP3.html").write_text(out, encoding="utf-8")
print(f"TOBYMP3.html generado ({len(out.encode()) // 1024} KB)")
