import pandas as pd
def time_stats(df):
    """
    Calculates the time statistics for the specified city and filters by month and day if applicable.

    Args:
        (Pandas DataFrame) df - name of the DataFrame to analyze

    Returns:
        (str) popular_month-most common month
        (str) popular_day_of_week-most common day of the week
        (int) popular_hour- most common hour of the day
    """
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'],infer_datetime_format=True)

    # extract month using dt.strftime method(January-June) from the Start Time column to create a month column
    df['month'] =df['Start Time'].dt.strftime('%B')
    #print(df['month'])
    # find the most common month
    popular_month=df['month'].mode()
    # resulting popular_month is a Series.So to extract the value
    print('Most Frequent Month:', popular_month[0])

    # extract day of week using  from the Start Time column to create a month column
    df['dayofweek'] =df['Start Time'].dt.weekday_name
    #print(df['month'])
    # find the most common month
    popular_day_of_week=df['dayofweek'].mode()
    # resulting popular_month is a Series.So to extract the value
    print('Most Frequent Day of week:', popular_day_of_week[0])

    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour
    #val_cnt=df['hour'].value_counts()
    popular_hour =df['hour'].mode()
    # find the most common hour (from 0 to 23)
    #popular_hour = val_cnt.idxmax()
    print('Most Frequent Start Hour:', popular_hour[0],':00')

def main():
    df=pd.read_csv('chicago.csv')
    time_stats(df)

if __name__ == '__main__':
    main()
