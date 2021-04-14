import pandas as pd
import argparse
def main():
    parser = argparse.ArgumentParser(description='Process a csv file name.')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    filename = args.filename
    # Task 1.1
    df = pd.read_csv("owid-covid-data.csv")
    df_2020 = df[df['date'].str.contains('2020')].copy()
    df_2020['month'] = df['date'].apply(lambda x:int(x[5:7]))
    df_new = df_2020[['location', 'month', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
    #aggregating
    df_new = df_new.groupby(['location', 'month']).agg({
        'total_cases':'max',
        'new_cases':'sum',
        'total_deaths':'max',
        'new_deaths':'sum'
    })
    # Task 1.2
    df_new['case_fatality_rate'] = df_new['total_deaths'] / df_new['total_cases']
    df_new = df_new.sort_values(by=['location', 'month'], ascending=True)
    
    df_res = df_new[['case_fatality_rate', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
    print(df_res.head(5))

    df_res.to_csv(filename)
main()
