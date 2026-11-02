"""Validate public catalogue boundaries without running application code."""
from pathlib import Path
import re, subprocess
root=Path(__file__).resolve().parents[1]
allowed={'README.md','AGENTS.md','docs/PROJECT_CONTEXT.md','docs/USING_AGENTS.md','docs/HANDOFF.md','docs/REVIEW_WORKFLOW.md','.github/pull_request_template.md','.github/workflows/catalogue.yml','tools/check_catalogue.py'}
files=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')
for name in filter(None,files):
    assert name in allowed or re.fullmatch(r'icons/[a-z0-9-]+\.png',name), f'Unexpected public file: {name}'
for name in re.findall(r'!\[[^]]*\]\((icons/[^)]+)\)',(root/'README.md').read_text()):
    p=root/name
    assert p.is_file() and p.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'), f'Invalid icon: {name}'
print('PASS: tracked catalogue file boundaries and README PNG references; content privacy still needs review.')
