# Python & Pytest Exercises

This repository contains Python exercises and automated tests written in **pytest**.  
It is part of my testing portfolio — feel free to browse the code.

## Purpose

These exercises document my Python learning journey as a Test Engineer.  
Each exercise focuses on a specific Python concept and is accompanied by a test suite written in pytest.  
The goal is to practice both Python fundamentals and test automation skills at the same time.

## Project Structure

```
Pytest/
├── pytest.ini               # pytest configuration
├── requirements.txt         # project dependencies
├── exercises/               # Python functions and concepts
│   ├── __init__.py
│   └── isinstance_demo.py   # isinstance() usage and type checking
└── tests/                   # pytest test suites
    ├── __init__.py
    └── test_isinstance.py   # tests for isinstance_demo.py
```

## Exercises

| File | Concept | Description |
|---|---|---|
| `isinstance_demo.py` | `isinstance()` | Type checking with built-in isinstance() function, including edge cases like bool vs int inheritance |

> More exercises will be added as I progress through Python topics.

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/pszwed/MultiTool_Testing.git
cd MultiTool_Testing/Pytest
```

**2. Create and activate virtual environment:**
```bash
# Create:
python -m venv .venv

# Activate (Windows):
.venv\Scripts\activate

# Activate (Linux/Mac):
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run all tests:**
```bash
pytest -v
```

**5. Run a specific test file:**
```bash
pytest tests/test_isinstance.py -v
```

## Code Quality

This project uses **Ruff** for linting and code formatting.

**Run linter:**
```bash
ruff check .
```

**Auto-fix issues:**
```bash
ruff check . --fix
```

**Format code:**
```bash
ruff format .
```

Ruff enforces PEP 8 compliance and consistent code style across the project.

## What I Focus On

- Writing **testable functions** (return values instead of print)
- Using `@pytest.mark.parametrize` for multiple test cases
- Covering **edge cases** (empty strings, empty lists, negative numbers)
- Keeping tests **readable and independent**
- Following **PEP 8** code style

## Tech Stack

- **Python** 3.13
- **pytest** 9.0.3
- **venv** for environment isolation