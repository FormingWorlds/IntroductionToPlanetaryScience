---
name: build-book
description: Build the Jupyter Book and report errors
disable-model-invocation: true
---

Build the Jupyter Book by running `jupyter-book build book/` from the repository root.

After the build completes:
1. Report any warnings or errors, especially:
   - Broken cross-references
   - LaTeX rendering issues
   - Missing files or figures
   - MyST Markdown syntax errors
2. If the build succeeds, report the output path for the HTML files
3. If the build fails, show the relevant error output and suggest fixes
