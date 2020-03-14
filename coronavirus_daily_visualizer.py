import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib import colors as mcolors
import random
import time

today = time.strftime("%m/%d/%Y")[1:][:-2]

df = pd.read_csv('COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/latest_saved.csv')

df_sum = df
#uniq = df['Country/Region'].unique()
uniq = ['US']
df_final = pd.DataFrame()
number_of_days = 4

for country in uniq:
    country_code = df['Country/Region']==country
    df_coutry = df[country_code]
    df_coutry = df_coutry.sort_values(by=[today], ascending=False)
    df_coutry = df_coutry.head(10)

    #print(df_coutry)

    # df_coutry['Province/State'] = df_coutry['Province/State'].str.split(', ').str[1]
    
    column_list = list(df_coutry)
    column_list.remove('Country/Region')
    column_list.remove('Lat')
    column_list.remove('Long')
    
    dfToBeT = df_coutry[column_list]
    dfToBeT = dfToBeT.groupby(['Province/State']).sum()
    print(dfToBeT)
    dfT = dfToBeT.T
    dfT['date'] = dfT.index    
    dfT = dfT[-number_of_days:]
    print(dfT)
    column_list_T = list(dfT)
    column_list_T.remove('date')
    
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    colors_to_draw = []

    for color in mcolors.TABLEAU_COLORS:
        colors_to_draw.append(color)

    index = 0
    for column in column_list_T:
        plt.plot( 'date' , column, data=dfT, marker='', color=colors_to_draw[index], linewidth=2, label=column)
        plt.legend()
        index = index + 1
    plt.show()