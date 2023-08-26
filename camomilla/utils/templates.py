from pathlib import Path
from typing import Sequence

from django import template as django_template
from os.path import relpath


def get_all_templates_files() -> Sequence[str]:
    dirs = []
    for engine in django_template.loader.engines.all():
        # Exclude pip installed site package template dirs
        dirs.extend(
            x
            for x in engine.template_dirs
            if "site-packages" not in str(x) or "camomilla" in str(x)
        )
    files = []
    for dir in dirs:
        files.extend(relpath(x, dir) for x in Path(dir).glob("**/*.html") if x)
    return files
