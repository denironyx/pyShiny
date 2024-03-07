from shiny.express import input, render, ui
from shinywidgets import render_plotly, render_altair

ui.page_opts(title="Penguins dashboard", fillable=True)


ui.input_selectize(
    "var", "Select variable",
    choices=['bill_length_mm', 'body_mass_g']
)

# @render.data_frame
# def head():
#     from palmerpenguins import load_penguins
#     df = load_penguins()
#     return df[["species",input.var()]]

# @render_altair
# def hist():
#     import altair as alt
#     from palmerpenguins import load_penguins
#     df = load_penguins()
#     return alt.Chart(df).mark_bar().encode(
#         x=alt.X(f"{input.var()}:Q", bin=True),
#         y="count()"
#     )

@render_plotly
def hist():
    import plotly.express as px
    from palmerpenguins import load_penguins
    df = load_penguins()
    return px.histogram(df, x=input.var())

# with ui.sidebar():
#     ui.input_selectize(
#         "var", "Select variable",
#         ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "year"]
#     )
#     ui.input_numeric("bins", "Number of bins", 30)

# with ui.card(full_screen=True):
#     @render_plotly
#     def hist():
#         import plotly.express as px
#         from palmerpenguins import load_penguins
#         return px.histogram(load_penguins(), x=input.var(), nbins=input.bins())