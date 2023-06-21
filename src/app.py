import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
from heatmap import generate_heatmap, get_players_heatmap
from src.graphs import generate_teams_stat_by_season_graph, generate_stat_diff_graph, generate_finalist_bar_graph
from src.utils import get_team_dropdown_options, get_players_stats_names, get_team_stats_dropdown_options, \
    get_player_dropdown_options, get_player_diff_stats_dropdown_options, get_leading_scorer_card, \
    get_leading_assister_card, get_leading_3pt_card, get_season_dropdown_options

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
# server = app.server

load_figure_template('FLATLY')

# DataFrames initialization
avg_stat_players_df = pd.read_csv('https://raw.githubusercontent.com/tomerm2323/NBA-visualization/master/src/players/avg_stats_players.csv')
players_df = pd.read_csv('https://raw.githubusercontent.com/tomerm2323/NBA-visualization/master/src/players/normelized_diff_players.csv')
teams_df = pd.read_csv('https://raw.githubusercontent.com/tomerm2323/NBA-visualization/master/src/teams/fix_team_merge.csv')
players_diff = pd.read_csv("https://raw.githubusercontent.com/tomerm2323/NBA-visualization/master/src/players/regular_season_playoff_merge_players.csv")
finalist_df = pd.read_csv("teams/norm_finalist_avg.csv")
total_teams_df = pd.read_csv("https://raw.githubusercontent.com/tomerm2323/NBA-visualization/master/src/teams/norm_total_avg.csv")

# Graphs and plots generation
#   TODO: Change color legend of the heat map so its shown clearly
players_heatmap = generate_heatmap(players_df['player'].unique(), players_df,
                                   stat_columns=['pts_per_g-diff', 'fg_pct-diff', 'usg_pct-diff'])
team_stats_scatter = generate_teams_stat_by_season_graph(teams_df, 'ATL', 'PTS')
players_stat_diff_line = generate_stat_diff_graph(players_diff, 'Kobe Bryant', 'fg_pct')
finalist_bar = generate_finalist_bar_graph(finalist_df, total_teams_df, 1982)


# onDataChange methods
@app.callback(
    Output(component_id='players-heatmap-graph', component_property='figure'),
    [Input(component_id='heatmap-player-slider', component_property='value'),
     Input(component_id='player-stats-checklist', component_property='value')]
)
def build_player_heatmap_fig(num_of_players, stats):
    players = get_players_heatmap(num_of_players, avg_stat_players_df)
    df_filtered_players = players_df[players_df['player'].isin(players)]
    players_column = df_filtered_players['player'].values
    return generate_heatmap(players_column, df_filtered_players, stats)


@app.callback(
    Output(component_id='teams-stats-scatter-graph', component_property='figure'),
    [Input(component_id='team-dropdown', component_property='value'),
     Input(component_id='stats-dropdown', component_property='value')]
)
def build_team_stats_scatter_fig(team, stat):
    return generate_teams_stat_by_season_graph(teams_df, team, stat)


@app.callback(
    Output(component_id='players_stat_diff_line-graph', component_property='figure'),
    [Input(component_id='player-dropdown', component_property='value'),
     Input(component_id='player-stats-dropdown', component_property='value')]
)
def build_team_stats_scatter_fig(player, stat):
    return generate_stat_diff_graph(players_diff, player, stat)


@app.callback(
    Output(component_id='finalist-bar-graph', component_property='figure'),
    [Input(component_id='season-dropdown', component_property='value')]
)
def build_finalist_bar_fig(year):
    return generate_finalist_bar_graph(finalist_df, total_teams_df, year)


# Dashboard Layout
def get_dash_layout():
    layout = dbc.Container([
        html.H1(children="NBA Playoff & Regular season analysis", className='mt-4 mb-4',
                style={'text-align': 'center'}),
        dbc.Row(
            [
                dbc.Col(get_leading_scorer_card(), width={'size': 3, 'offset': 2, 'order': 1}),
                dbc.Col(get_leading_assister_card(), width={'size': 3, 'offset': 0, 'order': 1}),
                dbc.Col(get_leading_3pt_card(), width={'size': 3, 'offset': 0, 'order': 1})
            ]
        ),
        html.H2(children="But are the playoffs and season really the same ?", className='mt-4 mb-4',
                style={'text-align': 'center'}),
        dbc.Row([
            html.H3(children="Exploring the Variations in Players' Performance between the Playoffs and Regular Season", className='mt-4 mb-4',
                    style={'text-align': 'center'}),
            html.Div(
                style={'width': '2000px', 'overflowX': 'scroll'},
                id='first-row',
                children=[
                    html.Label('Select No. of players:', style={'font-weight': 'bold', 'text-align': 'center'}),
                    dcc.Slider(20, 100, 20, value=60, id='heatmap-player-slider'),
                    ## , style={'width': '500px'}
                    html.Label('Select Statistics:', style={'font-weight': 'bold', 'text-align': 'center'}),
                    dcc.Checklist(id='player-stats-checklist',
                                  options=get_players_stats_names(),
                                  value=['pts_per_g-diff', 'fg_pct-diff', 'usg_pct-diff'], inline=True),
                    dcc.Graph(
                        id='players-heatmap-graph',
                        figure=players_heatmap,
                        style={'width': '4000px'}
                    )
                ]
            )
        ],
            className='mt-4 mb-4'
        ),
        dbc.Row([
            dbc.Col([
                html.H4(
                    children="Teams Statistics in the Playoffs and Regular Season",
                    className='mt-4 mb-4',
                    style={'text-align': 'center'}),
                html.Div(id='second-row-first-col',
                         children=[
                             html.Label('Select team:', style={'font-weight': 'bold', 'text-align': 'center'}),
                             dcc.Dropdown(id='team-dropdown', options=get_team_dropdown_options(teams_df), value='ATL'),
                             html.Label('Select Statistics:', style={'font-weight': 'bold', 'text-align': 'center'}),
                             dcc.Dropdown(id='stats-dropdown', options=get_team_stats_dropdown_options(teams_df), value='PTS'),
                             dcc.Graph(
                                 id='teams-stats-scatter-graph',
                                 figure=team_stats_scatter,
                             )
                         ])

                ],
                width={'size': 6, 'offset': 0, 'order': 1}
            ),
            dbc.Col([
                html.H4(
                    children="Player Statistics difference, Playoffs and Regular Season",
                    className='mt-4 mb-4',
                    style={'text-align': 'center'}),
                html.Div(id='second-row-second-col',
                         children=[
                             html.Label('Select player:', style={'font-weight': 'bold', 'text-align': 'center'}),
                             dcc.Dropdown(id='player-dropdown', options=get_player_dropdown_options(players_diff), value='Kobe Bryant'),
                             html.Label('Select Statistics:', style={'font-weight': 'bold', 'text-align': 'center'}),
                             dcc.Dropdown(id='player-stats-dropdown', options=get_player_diff_stats_dropdown_options(players_diff), value='fg_pct'),
                             dcc.Graph(
                                 id='players_stat_diff_line-graph',
                                 figure=players_stat_diff_line,
                             )
                         ])

                ],
                width={'size': 6, 'offset': 0, 'order': 1}
            )
        ]),
        dbc.Row([
            html.H4(
                children="Finalist Teams Statistic averages & All Teams",
                className='mt-4 mb-4',
                style={'text-align': 'center'}),
            html.Div(
                style={'width': '2000px', 'overflowX': 'scroll'},
                id='third-row',
                children=[
                    html.Label('Select Season:', style={'font-weight': 'bold', 'text-align': 'center'}),
                    dcc.Dropdown(id='season-dropdown', options=get_season_dropdown_options(finalist_df), value=1982),
                    dcc.Graph(
                        id='finalist-bar-graph',
                        figure=finalist_bar
                    )
                ]
            )
        ])
    ]
    )
    return layout


app.layout = get_dash_layout()

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
