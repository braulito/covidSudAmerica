"""
Braulio A Firpo Banegas - http://www.lu1aam.com.ar/

"""


import pandas as pd
import world_bank_data as wb

confirmados = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

rs = wb.get_countries()

lista = rs['name'].unique()

confirmados.drop(["Province/State","Lat","Long"],axis=1, inplace=True)

confirmados['Country/Region'] = confirmados['Country/Region'].replace(['US'],'United States')

confirmados  = confirmados[confirmados['Country/Region'].isin(lista)]

confirmados.rename(columns = {'Country/Region': 'País'}, inplace = True)

lista = confirmados['País'].unique()

confirmados.set_index('País', inplace=True)

li = confirmados.columns

confirmados = confirmados[li[len(li)-1]]

rs = wb.get_series('SP.POP.TOTL', mrv=1,simplify_index=True)

for x in range(0, len(lista)):
    confirmados[lista[x]] = confirmados[lista[x]]*1000000/rs[lista[x]]

confirmados = confirmados.nlargest(20)

confirmados = confirmados.sort_values(ascending=True)

confirmados.plot.barh(confirmados.values,
                      confirmados.index,
                      figsize=(20,5),
                      title="Casos por millón de habitanes al " + str(li[len(li)-1]))

del li
del lista
del rs
del x
del confirmados
