import pandas as pd
import matplotlib.pyplot as plt
def individual_stats(df):
    df['Trip Duration hrs'] = pd.DataFrame(df['Trip Duration']/3600,columns=['Trip Duration'])
    trip_dur_plot=df['Trip Duration hrs'].plot()
    trip_dur_plot.set_xlabel('Records')
    trip_dur_plot.set_ylabel('Trip Duration Hrs')
    trip_dur_plot.set_title('Trip duration (hrs) across records in the dataframe')
    plt.show()
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.dayofweek
    print(df['day_of_week'])

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month= months.index(month)+1

        # filter by month to create the new dataframe
        df =df[df.month== month]

    # filter by day of week if applicable
    if day != 'all':
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day=days.index(day.title())
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week==day]
    return df
def main():
    df=load_data('chicago','february','tuesday')
    individual_stats(df)

if __name__ == '__main__':
    main()
