import pandas as pd
def station_stats(df):
    """
    Calculates the station statistics for the specified city and filters by month and day if applicable.

    Args:
        (Pandas DataFrame) df - name of the DataFrame to analyze

    Returns:
        (str) common_start_st- most start station
        (str) common_end_st-most common end station
        (int) common_trip - most common trip
    """
    common_start_st= df['Start Station'].mode()
    common_end_st = df['End Station'].mode()
    common_trip = ('From ' + df['Start Station'] + ' To ' + df['End Station']).mode()

    print('Most Common Start Station:', common_start_st[0])
    print('Most Common End Station:', common_end_st[0])
    print('Most Common Trip:', common_trip[0])

def main():
    df=pd.read_csv('chicago.csv')
    station_stats(df)

if __name__ == '__main__':
    main()
