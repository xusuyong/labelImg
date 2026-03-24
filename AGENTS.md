# AGENTS.md - Developer Guidelines for NineSkyLabelImg

## Overview

NineSkyLabelImg is a fork of LabelImg - a graphical image annotation tool for YOLO, PascalVOC, and CreateML formats. It's a PyQt6-based Python application.

## Build/Lint/Test Commands

```bash
# Run all tests
python3 -m unittest discover tests

# Run a single test file, class, or method
python3 -m unittest tests.test_io
python3 -m unittest tests.test_io.TestPascalVocRW
python3 -m unittest tests.test_io.TestPascalVocRW.test_upper

# Compile Qt resources (after modifying resources.qrc)
# Note: pyrcc6 may not be available on Windows, resources.py import updated manually
pyrcc6 -o libs/resources.py resources.qrc
make qt6

# Install and run pre-commit hooks
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Code Style Guidelines

### Language Version
- Python 3.0+ only

### Imports (order: stdlib → third-party → local)
```python
import os
import sys
from math import sqrt

import yaml

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QColor, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from libs.ustr import ustr
from libs.logger import logger
```

### Naming Conventions
- **Functions/variables**: snake_case (`new_icon`, `label_validator`)
- **Classes**: PascalCase (`PascalVocReader`, `Settings`)
- **Constants**: UPPER_SNAKE_CASE
- **Private methods**: prefix with underscore (`_private_method`)

### Type Hints & Formatting
- Use Python 3.0+ style type hints
- Uses **ruff** for import sorting and formatting
- Line length: **120 characters**
```python
def format_shortcut(text: str) -> str:
    mod, key = text.split("+", 1)
    return "<b>%s</b>+<b>%s</b>" % (mod, key)
```

### Error Handling
- Use try/except blocks, catch specific exceptions when possible
- Log errors using the logger

```python
try:
    if os.path.exists(self.path):
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = convert_from_yaml(yaml.safe_load(f))
except Exception as e:
    logger.error("Loading setting failed: {}".format(e))
```

### PyQt6 API Changes (vs PyQt5)
- Enums are now scoped: `Qt.Vertical` → `Qt.Orientation.Vertical`
- Cursor shapes: `Qt.ArrowCursor` → `Qt.CursorShape.ArrowCursor`
- Mouse buttons: `Qt.LeftButton` → `Qt.MouseButton.LeftButton`
- Focus policy: `Qt.WheelFocus` → `Qt.FocusPolicy.WheelFocus`
- Dialog buttons: `QDialogButtonBox.Ok` → `QDialogButtonBox.StandardButton.Ok`
- File dialog: `QFileDialog.getOpenFileName` returns tuple `(str, str)` not `(QString, QString)`
- `Signal` → `pyqtSignal`
- `QVariant` removed (use Python types directly)
- `QStringListModel` in `QtCore`, not `QtWidgets`
- `QFileDialog`, `QAction`, `QMenu` in `QtWidgets`, not `QtGui`

### File Organization
- Main entry: `NineSkyLabelImg.py`
- Core library: `libs/`
- Tests: `tests/` (use unittest, `test_*.py`, `Test*`, `test_*`)
- Settings: YAML at `~/.NineSkyLabelImgSettings.yaml`

### Common Patterns
- Use `os.path.join()` and `os.path.abspath()`
- Use `encoding="utf-8"` when opening files

## Project Structure

```
labelImg/
├── NineSkyLabelImg.py       # Main entry point
├── libs/                    # Core library (canvas.py, settings.py, utils.py, etc.)
├── tests/                  # Unit tests (test_*.py)
├── resources.qrc           # Qt resources
├── setup.py                # Package setup
└── Makefile               # Build automation
```

## Key Dependencies
- PyQt6, lxml, pyyaml, loguru

## Notes for Agents
- Compile resources after modifying `resources.qrc`
- Run tests with `python3 -m unittest discover tests`
- Project targets YOLO format by default (supports PascalVOC and CreateML)
- Settings are YAML-based (not .pkl)
