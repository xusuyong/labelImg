# AGENTS.md - Developer Guide for NineSkyLabelImg

## Overview

NineSkyLabelImg is a graphical image annotation tool based on LabelImg, optimized for YOLO format. It's a PyQt5/Python project with a focus on bounding box annotation for computer vision datasets.

## Build & Development Commands

### Setup Dependencies
```bash
pip install pyqt5 lxml pyyaml
```

### Compile Resources
```bash
pyrcc5 -o libs/resources.py resources.qrc
```

### Run the Application
```bash
python NineSkyLabelImg.py
```

### Install Package
```bash
python setup.py install
```

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run a single test file
python -m pytest tests/test_utils.py

# Run a single test with pytest
python -m pytest tests/test_utils.py::TestUtils::test_generateColorByGivingUniceText_noError

# Run with unittest
python -m unittest tests.test_utils.TestUtils.test_nautalSort_noError
```

## Code Style Guidelines

### General Principles
- **Python Version**: Python 3.x (compatible with Python 3.3+)
- **Encoding**: UTF-8 (`# -*- coding: utf-8 -*-` at file top)
- **Max Line Length**: 100 chars recommended, 120 allowed
- **Indentation**: 4 spaces (no tabs)

### Imports (order: stdlib → third-party → local)
```python
import os
import sys
import re
import hashlib

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    QT5 = True
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    QT5 = False

from libs.utils import some_function
from libs.constants import SOME_CONSTANT
```

### Naming Conventions
- **Classes**: `PascalCase` (e.g., `Shape`, `YOLOWriter`)
- **Functions/Methods**: `snake_case` (e.g., `new_action`, `generate_color_by_text`)
- **Variables**: `snake_case` (e.g., `box_list`, `class_list`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `DEFAULT_LINE_COLOR`, `TXT_EXT`)
- **Private**: prefix underscore (e.g., `_highlight_index`)

### Type Annotations
This codebase uses **duck typing** - do NOT use Python 3.x type hints. Use descriptive names and comments instead.

### Code Structure
```python
class ClassName(object):
    CONSTANT_VALUE = 42

    def __init__(self, param1, param2=None):
        self.param1 = param1
        self._private_var = None

    def public_method(self):
        pass

    def _private_method(self):
        pass
```

### Error Handling
- Use try/except sparingly for recoverable errors
- Catch specific exceptions (e.g., `except ImportError:`)
- Bare `except:` only for PyQt4/5 compatibility
```python
try:
    from PyQt5.QtGui import *
except ImportError:
    from PyQt4.QtGui import *
```

### Documentation
- Use docstrings for public methods
- Keep comments concise
```python
def new_action(parent, text, slot=None, shortcut=None, ...):
    """Create a new action and assign callbacks."""
```

### String Formatting
Use `%` or `.format()` for Python 2 compatibility:
```python
"%d %.6f %.6f %.6f %.6f" % (class_index, x_center, y_center, w, h)
```

### File Headers
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

### Qt/PyQt Conventions
- Use star imports: `from PyQt5.QtGui import *`
- Use `QT5` flag for PyQt4/5 compatibility
- Use `ustr()` from `libs.ustr` for Unicode-safe strings

### Testing Conventions
- Tests in `tests/` directory
- Use `unittest.TestCase`
- Name: `test_<what_is_tested>`
```python
def test_generateColorByGivingUniceText_noError(self):
```

### Common Patterns
```python
# Dictionary update
self.__dict__.update(kwargs)

# Enum-like constants
class Shape(object):
    P_SQUARE, P_ROUND = range(2)

# File path handling
dir_name = os.path.abspath(os.path.dirname(__file__))
libs_path = os.path.join(dir_name, '..', 'libs')
sys.path.insert(0, libs_path)
```

### Performance
- Use list comprehensions
- Avoid repeated string concatenation
- Use `local_img_path` parameter to avoid redundant path lookups
