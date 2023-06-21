# import LinearRegression
import plotly.graph_objects as go
import numpy as np


def generate_teams_stat_by_season_graph(df, team, statName):
    # Generate sample data

    seasons, stat_season, playoffs_seasons, stat_playoffs = get_team_stats(df, team, statName)

    # Create scatter plot
    fig = go.Figure()

    # Add scatter plot for points1
    fig.add_trace(go.Scatter(
      x=seasons,
      y=stat_season,
      mode='markers',
      name='season data'
    ))

    # Add scatter plot for points2
    fig.add_trace(go.Scatter(
      x=playoffs_seasons,
      y=stat_playoffs,
      mode='markers',
      name='playoffs data'
    ))

    # Example non-linear line
    coefficients = np.polyfit(seasons, stat_season, 4)
    poly = np.poly1d(coefficients)
    line_y = poly(seasons)

    coefficients2 = np.polyfit(playoffs_seasons, stat_playoffs, 4)
    poly2 = np.poly1d(coefficients2)
    line_y_2 = poly2(seasons)

    fig.add_trace(go.Scatter(
      x=seasons,
      y=line_y,
      mode='lines',
      name='Regular season'
    ))

    fig.add_trace(go.Scatter(
      x=playoffs_seasons,
      y=line_y_2,
      mode='lines',
      name='Playoffs'
    ))

    # Set axis labels
    fig.update_layout(
      title=f'{statName} over the Seasons for {team}',
      xaxis_title='Season',
      yaxis_title=statName
    )

    return fig


def get_team_stats(df, team_id, stat_name):
    team_data = df[df['Team'] == team_id]
    seasons = []
    playoffs_seasons = []
    stat_season = []
    stat_playoffs = []

    for index, row in team_data.iterrows():
        season = row['Year']

        if season < 1982:
            continue

        season_stat = row[f'{stat_name}-Season']
        playoffs_stat = row[f'{stat_name}-Playoffs']

        if season_stat > 126.5:
            continue

        seasons.append(season)
        stat_season.append(season_stat)

        playoffs_seasons.append(season)
        stat_playoffs.append(playoffs_stat)

    return seasons, stat_season, playoffs_seasons, stat_playoffs


def get_player_diff_stats(df, player, statName):
    data = df[df['player'] == player]
    seasons = []
    stat_diffs = []

    for index, row in data.iterrows():
        season = row['season']
        stat_season = row[f'{statName}-season']
        stat_playoff = row[f'{statName}-playoffs']
        stat_diff = stat_playoff - stat_season
        seasons.append(season)
        stat_diffs.append(stat_diff)

    return seasons, stat_diffs


def generate_stat_diff_graph(df, player, statName):

  seasons, stats = get_player_diff_stats(df, player, statName)


  trace = go.Scatter(
      x=seasons,
      y=stats,
      mode='lines+markers',
      name='Stats'
  )

  trace2 = go.Scatter(
      x=seasons,
      y=[0] * len(seasons),
      mode='lines'
  )

  # Create the layout
  layout = go.Layout(
      title=f'{player} Seasonal {statName} difference between playoff and season',
      xaxis=dict(title='Season'),
      yaxis=dict(title=f'{statName}')
  )

  # Create the figure
  fig = go.Figure(data=[trace], layout=layout)
  fig.update_xaxes(zeroline=True)

  return fig


def generate_finalist_bar_graph(finalist_df, total_teams_df, year):
    # Filter datasets based on the specified year
    filtered_data_1 = finalist_df[finalist_df['Year'] == year]
    filtered_data_2 = total_teams_df[total_teams_df['Year'] == year]

    # Get the stat_avg column names
    stat_avg_columns = ['FG%', '2P%', '3P%', 'FT%', 'FG',
       'FGA', '2P', '2PA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'TRB',
       'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

    # Create the bar chart trace for dataset 1
    trace1 = go.Bar(
        x=stat_avg_columns,
        y=filtered_data_1[stat_avg_columns].values[0],
        name='Finalist Averages',
        marker=dict(color='rgb(0, 128, 0)')
    )

    # Create the bar chart trace for dataset 2
    trace2 = go.Bar(
        x=stat_avg_columns,
        y=filtered_data_2[stat_avg_columns].values[0],
        name='All Teams Averages',
        marker=dict(color='rgb(0, 0, 255)')
    )

    # Create the layout
    layout = go.Layout(
        title=f"Finalist Averages vs All Teams Averages for Season {year}",
        xaxis=dict(title='Statistics'),
        yaxis=dict(title='Normalized Average')
    )

    # Create the figure
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    return fig