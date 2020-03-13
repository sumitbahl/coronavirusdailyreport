import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np   

df = pd.read_csv('COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/latest_1.csv')

df_sum = df
#uniq = df['Country/Region'].unique()
uniq = ['US']
df_final = pd.DataFrame()
for country in uniq:
    country_code = df['Country/Region']==country
    df_coutry = df[country_code]
    df_coutry = df_coutry.sort_values(by=['3/12/20'], ascending=False)

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
    dfT = dfT[-3:]
    print(dfT)
    column_list_T = list(dfT)
    column_list_T.remove('date')
    state_list_color = {'California' : 'cyan', 
                'Washington': 'red',
                 'New York': 'orange', 
                 'Massachusetts': 'blue',
                 'Colorado' : 'brown',
                 'Florida' : 'gray',
                 'New Jersey' : 'olive'}
    for column in state_list_color:
        plt.plot( 'date' , column, data=dfT, marker='', color=state_list_color[column], linewidth=2, label=column)
        plt.legend()
    plt.show()