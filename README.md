# Lewis-Short in marimo

> Lewis and Short's *Latin Dictionary* in a marimo notebook.

![](./nb.gif)

## Use it in a web browser



It's hosted on github [here](https://neelsmith.github.io/marimo_lewis-short/)


## Run it locally (no internet connection required)



You need a python environment with marimo installed (e.g., `pip install marimo`). If you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/), you can run marimo notebooks with the `--sandbox` flag and `uv` will automatically manage any dependencies your notebook requires.


Use either

`marimo edit --sandbox NOTEBOOKFILE.py` (for edit mode)

or 

`marimo run --sandbox  NOTEBOOKFILE.py` (for app mode)

## Hosting it on your own website

Export the notebook as HTML-WASM, and provide a directory name for output. The notebook page will be `index.html` in that directory.

`marimo export html-wasm NOTEBOOKEFILE.py -o OUTPUT_FILE_OR_DIRECTORY --mode "run"`

## Change log

### 1.0.0 - 2026-02-18

Initial release.

**Added**

- search Lewis-Short by headword or article text
- results sorted by "Blackwell Sort" algorithm
- view all results at once or in accordion-fold display