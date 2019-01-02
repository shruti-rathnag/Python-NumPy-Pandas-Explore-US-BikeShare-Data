import pandas as pd
import math

def trip_duration_stats(df):
    """
    Calculates the station statistics for the specified city and filters by month and day if applicable.

    Args:
        (Pandas DataFrame) df - name of the DataFrame to analyze

    Returns:
        (str) total_travel_time- Total Travel Time
        (str) average_travel_time-Average Travel Time

    """
    """
    Start_Time = pd.to_datetime(df['Start Time'],infer_datetime_format = True)
    End_Time = pd.to_datetime(df['End Time'],infer_datetime_format = True)
    Travel_Time = End_Time-Start_Time
    total_travel_time=Travel_Time.sum()
    average_travel_time=Travel_Time.mean()
    """
    #print("Total Travel time is: {} hours".format(total_travel_time.total_seconds()/3600))
    print("Total Travel time is: {} hours".format(df['Trip Duration'].sum()/3600))
    #print("Average Travel time is: {} minutes".format(average_travel_time.total_seconds()/60))
    print("Average Travel time is: {} minutes".format(df['Trip Duration'].mean()/60))


def main():
    df=pd.read_csv('chicago.csv')
    trip_duration_stats(df)

if __name__ == '__main__':
    main()
