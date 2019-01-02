import pandas as pd
def compare_cities(df1,df2,df3):
    """

    """
    df4=pd.concat([df1,df2,df3])
    print(df4.columns)
def main():
    df_chicago=pd.read_csv('chicago.csv')
    df_ny=pd.read_csv('new_york_city.csv')
    df_washington=pd.read_csv('washington.csv')
    compare_cities(df_chicago,df_ny,df_washington)

if __name__ == '__main__':
    main()
