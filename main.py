# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('src/players/avg_stats_players.csv')
    print(df.columns)
    # 'usg_pct-season'
    # 'pts_per_g-season'
    # l = df[(df['mp_per_g-season'] < 48) & (df['mp_per_g-season'] > 35)]['player'].values
    l = df[(df['usg_pct-season'] < 34) & (df['usg_pct-season'] > 30 )]['player'].values
    for i in l:
        print(i)
    print(len(l))
