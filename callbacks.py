import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash
from dash import dcc
from dash.dependencies import Input, Output, State

import data


def register_callbacks(app, data):
    # Show/hide dropdowns based on the focus choice value
    @app.callback(
        [Output('country_choice_div', 'style'),
        Output('country_method_div', 'style'),
        Output('year_choice_div', 'style'),
        Output('year_method_div', 'style'),
        Output('year_country_div', 'style'),
        Output('year_cause_div', 'style'),
        Output('cause_choice_div', 'style'),
        Output('cause_method_div', 'style'),
        Output('cause_country_div', 'style'),
        Output('cause_year_div', 'style')],
        [Input('focus_choice', 'value'),
        Input('year_method', 'value'),
        Input('cause_method', 'value')])
    def dropdown_show_hide(choice, year_method, cause_method):
        style = []
        if choice == 'country':
            #return [{'width': '33%'}, {'width': '33%'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}]
            for i in range(10):
                if i in [0,1]:
                    style.append({'width': '33%'})
                else:
                    style.append({'display': 'none'})

        elif choice == 'year':
            for i in range(10):
                if i in [0,1,6,7,8,9]:
                    style.append({'display': 'none'})
                elif i in [2,3]:
                    style.append({'width': '22%'})
                elif i == 4:
                    continue
                else:
                    if year_method == 'country':
                        style.append({'width': '22%'})
                        style.append({'display': 'none'})
                    else:
                        style.append({'display': 'none'})
                        style.append({'width': '22%'}) 

        else:
            for i in range(10):
                if i in range(6):
                    style.append({'display': 'none'})
                elif i in [6,7]:
                    style.append({'width': '22%'})
                elif i == 8:
                    continue
                else:
                    if cause_method == 'country':
                        style.append({'width': '22%'})
                        style.append({'display': 'none'})
                    else:
                        style.append({'display': 'none'})
                        style.append({'width': '22%'}) 

        return style

    # Configure and show figure
    @app.callback(
        Output('output_figure', 'children'),
        [Input('focus_choice', 'value'),
        Input('country_choice', 'value'),
        Input('country_method', 'value'),
        Input('year_choice', 'value'),
        Input('year_method', 'value'),
        Input('year_country', 'value'),
        Input('year_cause', 'value'),
        Input('cause_choice', 'value'),
        Input('cause_method', 'value'),
        Input('cause_country', 'value'),
        Input('cause_year', 'value')]
    )
    def update_chart(focus_choice, country_choice, country_method, year_choice, year_method, year_country, year_cause, cause_choice, cause_method, cause_country, cause_year):
        
        if focus_choice == 'country':
            if country_method == 'total':
                fig = px.line(data.df[data.df['Country']==country_choice], x='Year', y=data.cause_list)
                fig.update_layout(title={'text': f'<b>{country_choice}</b> - Causes of Death over Time Counted Based on Total Occurence',
                 'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'}, yaxis_title='Number of Death')
                return dcc.Graph(id='fig_country_total', figure=fig)
            else:
                fig = px.line(data.df_million[data.df_million['Country']==country_choice], x='Year', y=data.cause_list)
                fig.update_layout(title={'text': f'<b>{country_choice}</b> - Causes of Death over Time Counted Based on Per Million', 'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
                return dcc.Graph(id='fig_country_million', figure=fig)
        
        elif focus_choice == 'year':
            if year_method == 'country':
                fig={
                    'data': [
                        {'x': data.cause_list, 'y': data.df[(data.df['Country']==year_country) & (data.df['Year']==int(year_choice))].values[0][3:-1], 'type': 'bar'}
                    ],
                    'layout': {
                        'title': f'<b>{year_choice}</b> - Number of Deaths in <b>{year_country}</b>',
                        'yaxis': {'title': 'Number of Death'}
                    }
                }
                return dcc.Graph(id='fig_year_country', figure=fig)
            else:
                fig = px.violin(data.df_million[(data.df_million['Year'] == int(year_choice)) & (data.df_million[year_cause] > 0)], x='Country', y=year_cause,
                            box=True, points='all')
                fig.update_layout(title={'text': f'<b>{year_choice}</b> - Death per Million by <b>{year_cause}</b>', 'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'}, yaxis_title='Death Per Million')
                return dcc.Graph(id='fig_year_cause', figure=fig)

        elif focus_choice == 'cause':
            if cause_method == 'year':
                fig = px.pie(data.df[data.df['Year']==int(cause_year)], values=cause_choice, names='Country', height=600)
                # fig.update_layout(title=f'{cause_choice} - Portion of Death by Countries in {cause_year}')
                fig.update_layout(title={'text': f'<b>{cause_choice}</b> - Portion of Death by Countries in <b>{cause_year}</b>', 'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
                return dcc.Graph(id='fig_cause_year', figure=fig)
            else:
                fig = px.area(data.df[data.df['Country']==cause_country], x='Year', y=cause_choice, height=500)
                # fig.update_layout(title=f'{cause_choice} - Portion of Death by Countries in {cause_year}')
                fig.update_layout(title={'text': f'<b>{cause_choice}</b> - Death by Years in <b>{cause_country}</b>', 'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'}, yaxis_title='Number of Death')
                return dcc.Graph(id='fig_cause_year', figure=fig)

        else:
            return None