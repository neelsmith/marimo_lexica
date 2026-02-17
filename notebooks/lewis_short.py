import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Lewis and Short, *Latin Dictionary*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(f"""
    /// admonition | Search settings


    ///
    """)
    return


@app.cell(hide_code=True)
def _(mo, search, search_in):
    mo.md(f"*Search for* {search} *in* {search_in}")
    return


@app.cell(hide_code=True)
def _(formatresults, mo, results):
    mo.md(f"""
    {formatresults(results)} 

    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.Html("<hr/><hr/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Computation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **UI**
    """)
    return


@app.cell
def _(mo):
    search = mo.ui.text(debounce=True)
    return (search,)


@app.cell
def _(mo):
    search_in = mo.ui.dropdown(["headword", "article", "all"],value="headword")
    return (search_in,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Display**
    """)
    return


@app.cell
def _():
    colnames = {
        "headword": "key",
        "article": "entry",
        "all": "all",
    }
    return (colnames,)


@app.cell
def _(colnames, search, search_in):
    def formatresults(results):
        if results.is_empty():
            return f"*No matches for* {search.value} *in* {colnames[search_in.value]}."

        formatted = []
        for row in results.iter_rows(named=True):
            lemma = row.get("key", "")
            urn = row.get("urn", "")
            text = row.get("entry", "")
            formatted.append(f"## *{lemma}*\n\n`{urn}`\n\n{text}")

        return "\n\n".join(formatted)

    return (formatresults,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Search**
    """)
    return


@app.cell
def _(colnames, df, pl, search, search_in):
    if not search.value:
        results = df
    else:
        results = df.filter(
            pl.col(colnames[search_in.value]).str.contains(search.value)
        )


    return (results,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Data**
    """)
    return


@app.cell
def _(Path, pl):
    def load_ls():
        datadir = Path.cwd() / "notebooks" / "public"
        lsfile = str(datadir / "ls-articles.cex")
        return pl.read_csv(lsfile, separator="|").with_columns(
            pl.concat_str([pl.col("key"), pl.col("entry")], separator=" ").alias("all")
        )


    return (load_ls,)


@app.cell
def _(load_ls):
    df = load_ls()
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Imports**
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import polars as pl

    return Path, pl


if __name__ == "__main__":
    app.run()
