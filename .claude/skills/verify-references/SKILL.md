---
name: verify-references
description: "Verify citations, BibTeX entries, and References sections in lecture files"
---

Verify the citation integrity of one or more lecture files. If no specific file is given, check all lecture `.md` files in `book/`.

## Steps

### 1. Collect all lecture files
Glob for `book/*//*.md` to find all lecture markdown files.

### 2. For each lecture file, check:

#### a. References section exists
- The file must end with a `## References` section
- That section must contain a `{bibliography}` directive with `:filter: docname in docnames`
- Flag any lecture file missing this section

#### b. All citations have BibTeX entries
- Find all `{cite}` directives in the file (patterns: `` {cite}`Key` ``, `` {cite}`Key1,Key2` ``, `` {cite:t}`Key` ``, `` {cite:p}`Key` ``)
- Extract each citation key
- Verify each key exists in `book/references.bib`
- Report any citation keys that have no matching BibTeX entry

#### c. BibTeX entry quality
- For each referenced BibTeX entry, check:
  - Has a `doi` field (warn if missing, suggest `% TODO: verify DOI` comment)
  - Has standard fields for its type (article: author, title, journal, year; book: author, title, publisher, year)
  - Key follows `AuthorYear` or `AuthorYearLetter` format

### 3. Check for orphaned BibTeX entries
- Scan all lecture files for citation keys actually used
- Compare against all keys in `references.bib`
- Report entries in `references.bib` that are never cited (informational, not an error)

### 4. Output a summary report
Format:
```
=== Citation Verification Report ===

Lectures checked: N

ERRORS (must fix):
- [file]: Citation `Key` not found in references.bib
- [file]: Missing ## References section

WARNINGS (should fix):
- [file]: BibTeX entry `Key` missing DOI field
- references.bib: Entry `Key` is never cited

OK: N lectures pass all checks
```
