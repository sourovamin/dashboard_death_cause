from dash import html

import components as cm
import data

main_lo = html.Div(children=[
    html.H1(children='CAUSE OF DEATH IN EU'),

    html.Div([
        html.Div([html.Label('Focus on'), cm.dd_focus], id='focus_choice_div', className='dd_div', style={'width': '34%'}),
        html.Div([html.Label('Country'), cm.dd_country], id='country_choice_div', className='dd_div'),
        html.Div([html.Label('Method'), cm.dd_country_method], id='country_method_div', className='dd_div'),
        html.Div([html.Label('Year'), cm.dd_year], id='year_choice_div', className='dd_div'),
        html.Div([html.Label('Look for'), cm.dd_year_method], id='year_method_div', className='dd_div'),
        html.Div([html.Label('Country'), cm.dd_year_country], id='year_country_div', className='dd_div'),
        html.Div([html.Label('Country'), cm.dd_year_cause], id='year_cause_div', className='dd_div'),
        html.Div([html.Label('Cause'), cm.dd_cause], id='cause_choice_div', className='dd_div'),
        html.Div([html.Label('Look for'), cm.dd_cause_method], id='cause_method_div', className='dd_div'),
        html.Div([html.Label('Country'), cm.dd_cause_country], id='cause_country_div', className='dd_div'),
        html.Div([html.Label('Year'), cm.dd_cause_year], id='cause_year_div', className='dd_div'),
    ], style={'display': 'flex', 'width': '100%'}),

    html.Div(id='output_figure'),

])