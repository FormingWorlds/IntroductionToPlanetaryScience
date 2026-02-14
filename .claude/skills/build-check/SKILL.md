---
name: build-check
description: "Full Jupyter Book build with structured error/warning report"
disable-model-invocation: true
---

Run a full Jupyter Book build and produce a structured report of all issues.

## Steps

### 1. Clean previous build
Run `jupyter-book clean book/` to ensure a fresh build.

### 2. Run full build
Run `jupyter-book build book/` from the repository root, capturing all output (stdout and stderr).

### 3. Parse and categorize issues
Scan the build output for Sphinx warnings and errors. Categorize them:

#### Errors (build failures)
- LaTeX compilation errors
- Missing required files
- Invalid directive syntax
- Configuration errors

#### Cross-reference warnings
- Unknown reference targets (`ref`, `numref`, `cite`)
- Duplicate labels
- Broken figure references

#### Content warnings
- Missing alt text on images
- Unreferenced footnotes
- Math rendering issues (look for `WARNING: latex` or `WARNING: mathjax`)

#### Style warnings
- Non-UTF8 characters
- Very long lines in code blocks
- Deprecated directive usage

### 4. Output structured report
Format:
```
=== Jupyter Book Build Report ===

Build status: SUCCESS / FAILED
Build time: Xs

ERRORS (N):
- [file:line] Description

CROSS-REFERENCE WARNINGS (N):
- [file:line] Description

CONTENT WARNINGS (N):
- [file:line] Description

STYLE WARNINGS (N):
- [file:line] Description

Summary: N errors, N warnings across M files
```

### 5. If build succeeded
Report the output path: `book/_build/html/index.html`
