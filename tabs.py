from dash import html, dcc
import components as cp

start = html.Div(id='start-content',
                 children=[
                     cp.main_header,
                     cp.gradcracker_div
                 ])

selections = html.Div(id='selections-content',
                      children=[])