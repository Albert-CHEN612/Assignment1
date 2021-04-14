import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np

def location2color(locations):
    #convert location to int color
    location2color_dic = {}
    res = []
    for loc in locations:
        if loc not in location2color_dic:
            location2color_dic[loc] = len(res)
        res.append(location2color_dic[loc])
    return res

def main():
    parser = argparse.ArgumentParser(description='Process a csv file name.')
    parser.add_argument('figure1', type=str)
    parser.add_argument('figure2', type=str)
    args = parser.parse_args()
    # Task 2.1
    df = pd.read_csv("owid-covid-data-2020-monthly.csv")
    plt.scatter(df['new_cases'], df['case_fatality_rate'], c=location2color(df['location']),s=5)
    plt.xlabel('new cases')
    plt.ylabel('case fatality rate')
    plt.savefig(args.figure1)
    # Task 1.2
    plt.cla()
    plt.scatter(np.log(df['new_cases']), df['case_fatality_rate'],c=location2color(df['location']),s=5)
    plt.xlabel('log(new cases)')
    plt.ylabel('case fatality rate')
    plt.savefig(args.figure2)

main()