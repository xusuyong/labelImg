# Agent Coding Guidelines for NineSkyLabelImg

## Overview

NineSkyLabelImg is a graphical image annotation tool for YOLO, PascalVOC, and CreateML formats. This file contains guidelines for agents working on this codebase.

## Build, Lint, and Test Commands

### Running Tests

```bash
# Run all tests
python3 -m unittest discover tests

# Run a specific test file
python3 -m unittest tests.test_settings

# Run a specific test class
python3 -m unittest tests.test_settings.TestSettings

# Run a single test method
python3 -m unittest tests.test_settings.TestSettings.test_basic

# Using make
make test
```

### Linting and Formatting

```bash
# Lint with ruff
ruff check .

# Auto-fix fixable issues
ruff check --fix .

# Format code
ruff format .
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit manually
pre-commit run
```

### Building Resources

```bash
# Build Qt resources (required after modifying resources.qrc)
pyrcc6 -o libs/resources.py resources.qrc

# Using make
make qt6
```

### Building Package

```bash
# Build distribution package
python3 -m build

# Or using setup.py
python3 setup.py sdist
```

## Code Style Guidelines

### General

- **Python Version**: 3.11+ (as specified in pyproject.toml)
- **Line Length**: 120 characters max
- **Indentation**: Spaces (4 spaces standard, follow existing code)
- **Quotes**: Double quotes for strings

### Imports

- Use ruff/isort for import sorting
- Known third-party: `PyQt6`, `loguru`, `yaml`
- Known first-party: `libs`
- Example order: stdlib → third-party → first-party

```python
# Correct order
import os
import sys

from PyQt6.QtCore import QPoint, Qt

from libs.canvas import Canvas
from libs.settings import Settings
```

### Ruff Lint Rules

Enabled rules (from pyproject.toml):
- `E` - pycodestyle errors
- `F` - pyflakes errors
- `I` - isort import sorting
- `UP` - pyupgrade (modern Python syntax)
- `B` - flake8-bugbear (potential bugs)

Ignored rules:
- `E501` - line length (handled by formatter)
- `B007` - unused loop variable

### Naming Conventions

- **Functions/variables**: snake_case (e.g., `load_file`, `image_dir`)
- **Classes**: PascalCase (e.g., `MainWindow`, `LabelDialog`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `XML_EXT`, `DEFAULT_LINE_COLOR`)
- **Private methods**: prefix with underscore (e.g., `_beginner`)

### Type Hints

- Use type hints where appropriate for clarity
- Follow Python 3.11+ typing conventions

### Error Handling

- Use `logger` from `libs.logger` for logging errors
- Avoid bare `except:` clauses
- Use specific exceptions when possible

```python
# Good
try:
    something()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
```

### Git Commit Messages

- Use clear, concise commit messages
- Prefix with scope if applicable (e.g., "fix:", "feat:", "refactor:")

## Project Structure

```
NineSkyLabelImg/
├── NineSkyLabelImg.py    # Main application entry
├── libs/                  # Core library modules
│   ├── canvas.py
│   ├── settings.py
│   ├── labelFile.py
│   └── ...
├── resources/             # Qt resources
│   └── resources.qrc
├── tests/                 # Unit tests
└── data/                  # Default classes file
    └── predefined_classes.txt
```

## Key Patterns

### MainWindow Initialization

The main window accepts two optional arguments:
- `image_dir`: Path to images directory
- `class_file`: Path to class definitions file

Both should be validated before passing to MainWindow (as added in the codebase).

### Label File Formats

- YOLO format: `.txt` files
- PascalVOC: `.xml` files
- CreateML: `.json` files

Current default is YOLO format.

## Testing Guidelines

- Tests are located in `tests/` directory
- Use `unittest` framework
- Each test file should have a corresponding test class
- Run single test for quick verification during development
