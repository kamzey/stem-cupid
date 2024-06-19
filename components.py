from dash import Dash, html, dcc, Input, Output, State, callback, dash_table

main_header = html.Div(id='header-div',
    children=[html.Header('STEMCupid',
                          id='header-header',
                          )]
)

gradcracker_div = html.Div(id='gradcracker-div',
    children=[html.Label('Choose database', id='gradcracker-label'),
              html.Button('Gradcracker', 
                          id='gradcracker-button',
                          n_clicks=0
                          )
              ]
)

background_options = ['Aerospace',
                       'Chemical/Process',
                       'Civil/Building',
                       'Computing/Technology',
                       'Electronic/Electrical',
                       'Maths/Business',
                       'Mechanical/Manufacturing',
                       'Science']
background_dict = {option: option for option in background_options}

options = html.Div(id='options-div',
                   children=[html.Div(id='option1', 
                                      children=[
                                          html.Label('Choose your background:'),
                                          dcc.Dropdown(id='option1-dd',
                                                       options=background_dict,
                                                       placeholder='Select...'
                                                       )]),
                            html.Div(id='option2',
                                     children=[
                                          html.Label("Choose your partner's background:"),
                                          dcc.Dropdown(id='option2-dd',
                                                       options=background_dict,
                                                       placeholder='Select...'
                                                       )]
                                     )
                   ])

location = html.Div(id='location-div',
                    children=[
                        html.Label('Maximum distance between two jobs:'),
                        dcc.Slider(0, 10, 0.25,
                                   marks=None,
                                   tooltip={
                                    'template': '{value} miles'
                                   })
                    ])

go_button = html.Div(id='go-button-div',
                     children=[
                         html.Button('Find us jobs',
                                     id='go-button',
                                     n_clicks=0
                                     )
                     ])

jobs = html.Div(id='jobs-div',
                children=[
                    html.Div(id='jobs1',
                             children=[
                                html.Label('Jobs for YOU:'),
                                dash_table.DataTable()
                             ]),
                    html.Div()
                ])