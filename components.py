from dash import dcc
from dash import html

import data

# Dropdowns
dd_focus = dcc.Dropdown(
    id='focus_choice',
    options=[
        {'label': 'Country', 'value': 'country'},
        {'label': 'Year', 'value': 'year'},
        {'label': 'Cause of Death', 'value': 'cause'}
    ],
    value='country',
    clearable=False,
)

dd_country = dcc.Dropdown(
    id='country_choice',
    options=[{'label': i, 'value': i} for i in data.country_list],
    value='Germany',
    clearable=False,
)

dd_country_method = dcc.Dropdown(
    id='country_method',
    options=[
        {'label': 'Total Occurence', 'value': 'total'},
        {'label': 'Per Milion', 'value': 'milion'},
    ],
    value='total',
    clearable=False,
)

dd_year = dcc.Dropdown(
    id='year_choice',
    options=[{'label': i, 'value': i} for i in data.year_list],
    value='2019',
    clearable=False,
)

dd_year_method = dcc.Dropdown(
    id='year_method',
    options=[
        {'label': 'Country', 'value': 'country'},
        {'label': 'Cause', 'value': 'cause'},
    ],
    value='country',
    clearable=False,
)

dd_year_country = dcc.Dropdown(
    id='year_country',
    options=[{'label': i, 'value': i} for i in data.country_list],
    value='Germany',
    clearable=False,
)

dd_year_cause = dcc.Dropdown(
    id='year_cause',
    options=[{'label': i, 'value': i} for i in data.cause_list],
    value='Meningitis',
    clearable=False,
)

dd_cause = dcc.Dropdown(
    id='cause_choice',
    options=[{'label': i, 'value': i} for i in data.cause_list],
    value='Meningitis',
    clearable=False,
)

dd_cause_method = dcc.Dropdown(
    id='cause_method',
    options=[
        {'label': 'Country', 'value': 'country'},
        {'label': 'Year', 'value': 'year'},
    ],
    value='year',
    clearable=False,
)

dd_cause_country = dcc.Dropdown(
    id='cause_country',
    options=[{'label': i, 'value': i} for i in data.country_list],
    value='Germany',
    clearable=False,
)

dd_cause_year = dcc.Dropdown(
    id='cause_year',
    options=[{'label': i, 'value': i} for i in data.year_list],
    value='2019',
    clearable=False,
)