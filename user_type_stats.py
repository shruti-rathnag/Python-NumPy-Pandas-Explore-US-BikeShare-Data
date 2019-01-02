import pandas as pd
def user_type_stats(df):
    """
    Calculates the user type statistics for the specified city and filters by month and day if applicable.

    Args:
        (Pandas DataFrame) df - name of the DataFrame to analyze

    Returns:
        (str) user_type_counts- Counts of each user type
        (str) gender_cnt-counts of each gender_count
              earliest_yr_birth- Earliest birth year
              common_yr_birth - Common birth year
              recent_yr_birth - Recent birth year

    """
    #user_type_cnt_df=pd.DataFrame(df['User Type'].value_counts())
    #print("The user type counts are:\n", user_type_cnt_df)
    user_type_cnt=df['User Type'].value_counts().to_frame()
    print("The counts of each user type are:\n" , user_type_cnt)
    try:
        gender_cnt=df['Gender'].value_counts().to_frame()
        Birth_yr = df['Birth Year'].dropna().astype('int64')
        print("The counts of each gender are:\n" , gender_cnt)
        print("Earliest Birth Year is:", Birth_yr.min())
        print("Most common Birth Year is:", Birth_yr.mode()[0])
        print("Most recent Birth Year is:", Birth_yr.max())



    except Exception as e:
        print(e,"No birth or gender data available for this dataset")



def main():
    df=pd.read_csv('washington.csv')
    user_type_stats(df)
if __name__ == '__main__':
    main()
