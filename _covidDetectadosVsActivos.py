import pandas as pd
import world_bank_data as wb

rs = wb.get_series('SP.POP.TOTL', mrv=1,simplify_index=True)

confirmados = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

lista = rs.index.unique()

confirmados.drop(["Province/State","Lat","Long"],axis=1, inplace=True)
confirmados  = confirmados[confirmados['Country/Region']=='Argentina']
confirmados.rename(columns = {'Country/Region': 'Pais'}, inplace = True)
confirmados = confirmados.groupby(['Pais']).sum()

lista = confirmados.index 

confirmados = confirmados.transpose()


recuperados = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")

lista = rs.index.unique()

recuperados.drop(["Province/State","Lat","Long"],axis=1, inplace=True)
recuperados  = recuperados[recuperados['Country/Region']=='Argentina']
recuperados.rename(columns = {'Country/Region': 'Pais'}, inplace = True)
recuperados = recuperados.groupby(['Pais']).sum()

lista = recuperados.index 

recuperados = recuperados.transpose()


muertos = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

lista = rs.index.unique()

muertos.drop(["Province/State","Lat","Long"],axis=1, inplace=True)
muertos['Country/Region'] = muertos['Country/Region'].replace(['US'],'United States')
muertos['Country/Region'] = muertos['Country/Region'].replace(['Russia'],'Russian Federation')
muertos  = muertos[muertos['Country/Region']=='Argentina']
muertos.rename(columns = {'Country/Region': 'Pais'}, inplace = True)
muertos = muertos.groupby(['Pais']).sum()

lista = muertos.index 

muertos = muertos.transpose()

activos = confirmados - muertos - recuperados

confirmados.rename(columns = {'Argentina': 'Detectados'}, inplace = True)
activos.rename(columns = {'Argentina': 'Activos'}, inplace = True)

ax = confirmados.plot(figsize=(10,5))
activos.plot(ax=ax)

del confirmados
del recuperados
del activos
del rs
del lista
del muertos