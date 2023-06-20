import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.dependencies import Input, Output
import pandas as pd
from heatmap import generate_heatmap, get_players_heatmap

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
# server = app.server

load_figure_template('FLATLY')
avg_stat_players_df = pd.read_csv('players/avg_stats_players.csv')
players_df = pd.read_csv('players/normelized_diff_players.csv')
players_heatmap = generate_heatmap(players_df['player'].unique(), players_df, stat_columns=['tov_per_g-diff', 'pf_per_g-diff','pts_per_g-diff', 'bpm-diff'])
@app.callback(
    Output(component_id='players-heatmap-graph', component_property='figure'),
    [Input(component_id='player-category-dropdown', component_property='value'),
     Input(component_id='player-stats-checklist', component_property='value')]
)
def build_player_heatmap_fig(num_of_players, stats):
    players = get_players_heatmap(num_of_players, avg_stat_players_df)
    player_column = players_df[players_df['player'].isIn(players)]
    return generate_heatmap(player_column, stats,players_df)


def get_dash_layout():
    layout = dbc.Container([
        html.H1(children="NBA Playoff & Regular season analysis", className='mt-4 mb-4', style={'text-align': 'center'}),
        dbc.Row([
            dbc.Col([
                  html.Div(
                      style={'width': '4000px',
                        'overflowX':'scroll'},
                      id='first-row-first-col',
                      children=[
                          html.Label('Select player:', style={'font-weight': 'bold', 'text-align': 'center'}),
                          dcc.Dropdown(options=['Leading Players', 'Rule Players'], value='Leading Players', id='player-category-dropdown'),
                          dcc.Checklist(id='player-stats-checklist',
                                        options=['mp_per_g-diff', 'fg_pct-diff', 'fg3_pct-diff',
                                        'fta_per_g-diff', 'ft_pct-diff', 'tov_per_g-diff', 'pf_per_g-diff',
                                        'pts_per_g-diff', 'bpm-diff', 'per-diff', 'ts_pct-diff', 'usg_pct-diff',
                                        'ws-diff'],
                                        value=['pts_per_g'],inline=True),
                          dcc.Graph(
                              id='players-heatmap-graph',
                              figure=players_heatmap,
                              style={'width': '4000px'}
                                  )
                              ]
                          )
                      ],
                width={'size': 4, 'offset': 2, 'order': 1}
                  )
              ],
              className='mt-4 mb-4'
            )
        ]
    )
    return layout

app.layout = get_dash_layout()

# Run the application
if __name__ == '__main__':

    app.run_server(debug=True)