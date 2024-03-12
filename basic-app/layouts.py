from shiny.express import input, ui
from shinywidgets import render_plotly

ui.input_selectize(
    "var", "Select variable",
    choices=["bill_length_mm", "body_mass_g"]
)

@render_plotly
def hist():
    import plotly.express as px
    from palmerpenguins import load_penguins
    df = load_penguins()
    return px.histogram(df, x=input.var())


