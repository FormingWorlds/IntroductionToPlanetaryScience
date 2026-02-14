# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

University course materials repository for "Introduction to Planetary Science" at the Kapteyn Institute (course code WBAS002-05). Part of the [FormingWorlds](https://github.com/FormingWorlds) organization.

## Repository Structure

- `planning/` — Curriculum outlines and course planning documents
- `content/course2025` — Symlink to Google Drive containing actual lecture materials (slides, data, etc.); gitignored and not tracked
- `.gitignore` is Python-oriented, anticipating future Python-based course tooling or notebooks

## Key Details

- This is an early-stage repository primarily for course planning and content indexing. Actual course materials live in Google Drive via symlink.
- No build system, tests, or CI/CD are configured yet.
- The course covers 14 primary lectures spanning planet formation through exoplanets and astrobiology (see `planning/content.md`).