# Lewis-Short in marimo

> Lewis and Short's *Latin Dictionary* in a marimo notebook.

![](./nb.gif)

## Ways to use it

**From a web browser**:

- it's hosted on github [here](https://neelsmith.github.io/marimo_lewis-short/)


**Run it locally (no internet connection required)**:

You need a python environment with marimo installed (e.g., `pip install marimo`). Use either

`marimo edit NOTEBOOKFILE.py` (for edit mode)

or 

`marimo run NOTEBOOKFILE.py` (for app mode)

**Hosting it on your own website**:

`marimo export html-wasm NOTEBOOKEFILE.py -o OUTPUT_FILE_OR_DIRECTORY --mode "run"`

## Change log

### 1.0.0 - 2026-02-18

Initial release.

**Added**

- search Lewis-Short by headword or article text
- results sorted by "Blackwell Sort" algorithm
- view all results at once or in accordion-fold display