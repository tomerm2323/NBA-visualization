import dash_bootstrap_components as dbc
import dash_html_components as html

from src.heatmap import get_players_heatmap


def get_players_stats_names():
    label_and_values = []

    label_and_values.append({'label': ' MIN    ', 'value': 'mp_per_g-diff'})
    label_and_values.append({'label': ' FG%    ', 'value': 'fg_pct-diff'})
    label_and_values.append({'label': ' 3P%    ', 'value': 'fg3_pct-diff'})
    label_and_values.append({'label': ' FTA    ', 'value': 'fta_per_g-diff'})
    label_and_values.append({'label': ' FT%    ', 'value': 'ft_pct-diff'})
    label_and_values.append({'label': ' TOV    ', 'value': 'tov_per_g-diff'})
    label_and_values.append({'label': ' PF     ', 'value': 'pf_per_g-diff'})
    label_and_values.append({'label': ' PTS    ', 'value': 'pts_per_g-diff'})
    label_and_values.append({'label': ' BPM    ', 'value': 'bpm-diff'})
    label_and_values.append({'label': ' PER    ', 'value': 'per-diff'})
    label_and_values.append({'label': ' TS%    ', 'value': 'ts_pct-diff'})
    label_and_values.append({'label': ' USAGE    ', 'value': 'usg_pct-diff'})
    label_and_values.append({'label': ' WS     ', 'value': 'ws-diff'})

    return label_and_values


def get_team_dropdown_options(df):
    return df['Team'].unique()


def get_team_stats_dropdown_options(df):
    label_and_values = []

    label_and_values.append({'label': ' FG%    ', 'value': 'FG%'})
    label_and_values.append({'label': ' 3P%    ', 'value': '3P%'})
    label_and_values.append({'label': ' FT%    ', 'value': 'FT%'})
    label_and_values.append({'label': ' FTA    ', 'value': 'FTA'})
    label_and_values.append({'label': ' DRB    ', 'value': 'DRB'})
    label_and_values.append({'label': ' TRB    ', 'value': 'TRB'})
    label_and_values.append({'label': ' AST    ', 'value': 'AST'})
    label_and_values.append({'label': ' STL    ', 'value': 'STL'})
    label_and_values.append({'label': ' BLK    ', 'value': 'BLK'})
    label_and_values.append({'label': ' TOV    ', 'value': 'TOV'})
    label_and_values.append({'label': ' PF     ', 'value': 'PF'})
    label_and_values.append({'label': ' PTS    ', 'value': 'PTS'})

    return label_and_values


def get_player_dropdown_options(df):
    return get_players_heatmap(59, df)


def get_player_diff_stats_dropdown_options(df):
    label_and_values = []

    label_and_values.append({'label': ' MIN    ', 'value': 'mp_per_g'})
    label_and_values.append({'label': ' FG%    ', 'value': 'fg_pct'})
    label_and_values.append({'label': ' 3P%    ', 'value': 'fg3_pct'})
    label_and_values.append({'label': ' FTA    ', 'value': 'fta_per_g'})
    label_and_values.append({'label': ' FT%    ', 'value': 'ft_pct'})
    label_and_values.append({'label': ' TOV    ', 'value': 'tov_per_g'})
    label_and_values.append({'label': ' PF     ', 'value': 'pf_per_g'})
    label_and_values.append({'label': ' PTS    ', 'value': 'pts_per_g'})
    label_and_values.append({'label': ' BPM    ', 'value': 'bpm'})
    label_and_values.append({'label': ' PER??    ', 'value': 'per'})
    label_and_values.append({'label': ' TS%    ', 'value': 'ts_pct'})
    label_and_values.append({'label': ' USAGE    ', 'value': 'usg_pct'})
    label_and_values.append({'label': ' WS     ', 'value': 'ws'})

    return label_and_values


def get_season_dropdown_options(df):
    return df['Year'].unique()


def get_leading_scorer_card():
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src='https://cmg-cmg-tv-10040-prod.cdn.arcpublishing.com/resizer/EvRgkt4qVY9PqhdnGPcQcYeveM4=/800x0/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/cmg/FDEYU3XJZNB3BHBLWGRUJWRLXA.jpg',
                            className="img rounded-start",
                            style={'maxHeight': "250px"}
                        ),
                        className="col",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H4("Michael Jordan", className="scorer-name-card-title", style={"font-weight": "bold"}),
                                html.H5("Leading Scorer Per game", className="scorer-card-title"),
                                html.H5("In Season & Playoffs", className="scorer-second-card-title")
                            ]
                        ),
                        # className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "540px"},
    )

    return card


def get_leading_assister_card():
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src='https://cdn.britannica.com/27/189527-050-5BAD12C2/Magic-Johnson.jpg',
                            className="img-fluid rounded-start",
                        ),
                        className="col",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H4("Magic Johnson ", className="assister-name-card-title",  style={"font-weight": "bold"}),
                                html.H5("Leading Assister Per game", className="assister-card-title"),
                                html.H5("In Season & Playoffs", className="assister-second-card-title"),
                            ]
                        ),
                        # className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "540px"},
    )

    return card


def get_leading_3pt_card():
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src='https://s.hdnux.com/photos/01/26/24/70/22629950/4/1200x0.jpg',
                            className="img rounded-start",
                        ),
                        className="col",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H4("Steph Curry", className="3pt-name-card-title", style={"font-weight": "bold"}),
                                html.H5("Leading 3PT Per game", className="3pt-card-title"),
                                html.H5("In Season & Playoffs", className="3pt-second-card-title"),
                            ]
                        ),
                        # className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-4",
        style={"maxWidth": "540px"},
    )

    return card