import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

def generate_heatmap(player_column, dataframe,stat_columns):
    # Transpose the dataframe to switch the x and y axes
    transposed_df = dataframe.set_index(player_column)[stat_columns].T

    # Create the heatmap figure
    fig = go.Figure(data=go.Heatmap(
        x=transposed_df.columns,
        y=transposed_df.index,
        z=transposed_df.values,
        colorscale='RdYlBu',
        reversescale=True
    ))

    # Set axis labels
    fig.update_layout(
        xaxis_title='Player Name',
        yaxis_title='Statistic'
    )
    return fig
def get_players_heatmap(num_of_players, df):
    players = list((df.sort_values(by=['pts_per_g-season'],ascending=False)['player'].drop_duplicates()))[:num_of_players]
    return players



if __name__ == '__main__':
    pass
