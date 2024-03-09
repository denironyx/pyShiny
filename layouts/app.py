import plotly.express as px
from shiny.express import input, render, ui
from shinywidgets import render_widget

ui.page_opts(title="Multi-page example", fillable=True)

tips = px.data.tips()

with ui.sidebar():
    ui.input_select("var", "Select variable", choices=["total_bill", "tip"])

with ui.navset_card_underline(title="Penguins"):
    with ui.nav_panel("Plot"):
        @render_widget
        def hist():
            return px.histogram(px.data.tips(), input.var())
        

# with ui.nav_panel("Plot"):
#     @render_widget
#     def hist():
#         return px.histogram(px.data.tips(), input.var())

    with ui.nav_panel("Table"):
        @render.table
        def table():
            return px.data.tips() 
    # with ui.nav_panel("Table"):
    #     @render.data_frame
    #     def table():
    #         return tips[[input.var()]]

# @render_widget
# def hist():
#     return px.histogram(px.data.tips(), input.var())
