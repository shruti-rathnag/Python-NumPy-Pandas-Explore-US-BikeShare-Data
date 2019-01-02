import time
import pandas as pd
import matplotlib.pyplot as plt


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*40)
    print('\n\n\nHello! Let\'s explore some US bikeshare data!\n\n')

    while True:

    # get user input for city (chicago, new york city, washington).
        while True:
            city = input("\n Choose one of the following cities: Chicago, New York City, Washington\n (Please note that you may be prompted this question again if you don't enter the right values:\n)").lower()
            if city in ['chicago','new york city', 'washington']:
                break
        while True:
            filter_question = input("\n Do you want to filter by either month/day/both? Choose Y/N.\n (Please note that you may be prompted this question again if you don't enter the right values:\n)")
            if filter_question.lower() in ['y','n']:
                break

        if filter_question.lower() == 'y':

            while True:
    # get user input for month (all, january, february, ... , june)
                month = input("\n Enter a month as full name between January-June. Enter All if you'd like to analyze all months\n (Please note that you may be prompted this question again if you don't enter the right values:\n").lower()
                if month in ['january', 'february', 'march','april','may','june','all']:
                    break

    # get user input for day of week (all, monday, tuesday, ... sunday)
            while True:
                day = input("\n Enter a day of the week as full name (Sunday-Saturday). Enter All if you'd like to analyze all days\n (Please note that you may be prompted this question again if you don't enter the right values:\n").lower()
                if day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
                    break
        else:
            day = 'all'
            month = 'all'

        while True:
            response = input("\n Do you want to make changes to your response? Choose Y/N.\n")
            if response.lower() in ['y','n']:
                break
        if response.lower() != 'y':
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.dayofweek


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df.month== month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        day = days.index(day.title())
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week==day]
    return df




def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Args:
        df - Pandas DataFrame containing city data
    Prints:
        popular_month - Most Frequent month
        popular_day_of_week - Most Frequest day of week
        Popular hour - Most Frequent start hour

    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)


    # extract month name using dt.strftime method(January-June) from the Start Time
    # column to create a month column
    df['month'] = df['Start Time'].dt.strftime('%B')
    #print(df['month'])
    # find the most common month
    popular_month = df['month'].mode()
    # resulting popular_month is a Series.So to extract the value
    # display the most common month
    print('Most Frequent Month:', popular_month[0])

    # extract day of week using  from the Start Time column to create a month column
    df['dayofweek'] = df['Start Time'].dt.weekday_name

    # find the most common day of week
    popular_day_of_week = df['dayofweek'].mode()
    # resulting popular_day_of_week is a Series.So to extract the value
    # display the most common day of week
    print('Most Frequent Day of week:', popular_day_of_week[0])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()

    # display the most common start hour
    print('Most Frequent Start Hour:', popular_hour[0],':00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    Args:
        df - Pandas DataFrame containing city data
    Prints:
        common_start_st - Most Common Start Station
        common_end_st - Most Common End Station
        common_trip - Most Common Trip

    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_st = df['Start Station'].mode()
    common_end_st = df['End Station'].mode()
    common_trip = ('From ' + df['Start Station'] + ' To ' + df['End Station']).mode()
    # display most commonly used start station
    print('Most Common Start Station:', common_start_st[0])
    # display most commonly used end station
    print('Most Common End Station:', common_end_st[0])
    # display most frequent combination of start station and end station trip
    print('Most Common Trip:', common_trip[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    Args:
        df - Pandas DataFrame containing city data
    Prints:
        Total Travel Time
        Average Travel Time


    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel time is: {} hours".format(df['Trip Duration'].sum()/3600))
    # display mean travel time
    print("Average Travel time is: {} minutes".format(df['Trip Duration'].mean()/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_type_stats(df):
    """
    Displays statistics on bikeshare users.
    Args:
        df - Pandas DataFrame containing city data
    Prints:
         user_type_cnt - Counts of each user type
         gender_cnt - Counts of each gender
         Earliest Birth year
         Most common Birth year
         Most recent Birth year
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    #converting results to a DataFrame
    user_type_cnt = df['User Type'].value_counts().to_frame()
    print("\nThe counts of each user type are:\n" , user_type_cnt)
    # Enclosing gender and birth statistics in try except block as Washington
    # dataset doesn't have this info
    try:
        gender_cnt = df['Gender'].value_counts().to_frame()

        Birth_yr = df['Birth Year'].dropna().astype('int64')
        # Display counts of gender
        print("\nThe counts of each gender are:\n" , gender_cnt)
        # Display earliest, most recent, and most common year of birth
        print("\nEarliest Birth Year is:", Birth_yr.min())
        print("\nMost common Birth Year is:", Birth_yr.mode()[0])
        print("\nMost recent Birth Year is:", Birth_yr.max())

    except Exception as e:
        print(e,"No birth or gender data available for this dataset")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, start_position):
    """
    Displays 5 rows in the requested dataset
    Args:
        df- Pandas DataFrame containing city data
        start_position - Starting row for displaying data
    Prints:
        5 lines of dataset from the start_position
    """
    print('\nDisplaying data for the individual dataset...\n')
    start_time = time.time()
    print("\n Below are 5 lines of data from the requested dataset:\n")
    print(df.iloc[start_position:start_position+5, :])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_plot(df):
    """
    Displays plot of Trip Duration in hrs
    Args:
        df - Pandas DataFrame containing city data
    Prints:
        Dictionary:Records-Individual trip data
        Plot of Trip Duration in hours

    """
    print('\nCalculating Individual Trip Stats...\n')
    start_time = time.time()
    df['Trip Duration hrs'] = pd.DataFrame(df['Trip Duration']/3600, columns = ['Trip Duration'])
    print("\n The plot of total duration in hours for the dataset is:\n (Please close the plot to continue)\n ")
    trip_dur_plot = df['Trip Duration hrs'].plot()
    trip_dur_plot.set_xlabel('Records')
    trip_dur_plot.set_ylabel('Trip Duration Hrs')
    trip_dur_plot.set_title('Trip duration (hrs) across the DataFrame')
    plt.show()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # Ask for user input for each statistics
        Time_stats_q = input("\n Would you like to view the most frequest times of travel? Enter Y or N.\n")
        if Time_stats_q.lower() == 'y':
            time_stats(df)
        Station_stats_q = input("\n Would you like to view the most popular stations/trip? Enter Y or N.\n")
        if Station_stats_q.lower() =='y':
            station_stats(df)
        Trip_duration_stats_q = input("\n Would you like to view the total/mean travel time? Enter Y or N.\n")
        if Trip_duration_stats_q.lower() == 'y':
            trip_duration_stats(df)
        User_stats_q = input("\n Would you like to view the user statistics? Enter Y or N.\n")
        if User_stats_q.lower() == 'y':
            user_type_stats(df)
        start_position = 0
        while True:
            qstn = input("\nWould you like to display 5 rows of data? Enter Y or N.\n")
            if qstn.lower() == 'y':
                display_data(df,start_position)
                start_position += 5
                if start_position >= len(df.index)-1:
                    break
            else:
                break
        trip_duration_plot_q = input("\n Would you like to view the individual trip duration plot? Enter Y or N.\n")
        if trip_duration_plot_q.lower() == 'y':
            trip_duration_plot(df)

        restart = input('\n Would you like to restart? Enter Y/N.\n')
        if restart.lower() != 'y':
            break



if __name__ == "__main__":
	main()
