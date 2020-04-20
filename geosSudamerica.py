import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import os
import subprocess
import glob
from PIL import Image
import time

df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

listaPaises = ['Chile','Argentina','Brazil','Uruguay','Bolivia',
      'Paraguay','Peru','Ecuador','Colombia',
      'Venezuela','Guyana','Suriname']

df  = df[df['Country/Region'].isin(listaPaises)]

df.drop(['Province/State','Country/Region',
         'Lat','Long'],axis=1, inplace=True)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

mapa  = world[world['name'].isin(listaPaises)]

mapa = mapa.sort_values(["name"], ascending = (True))

mapa.drop(['continent','iso_a3','gdp_md_est'],axis=1, inplace=True)

pa = mapa['name'].tolist()
pob =mapa['pop_est'].tolist()


lista = df.columns
cols = lista.size -1
i = 4
l = []

while i <= cols:
    l.append(lista[i])
    i = i + 1
    
i=31

vma = 0
vmi = 999999999

lista =[]

while i < len(l):
    z = 0
    v = []
    while z < len(pa) :
        mul = 1000000
        valor = int(df.iloc[z][l[i]]) * mul / int(mapa.iloc[z]['pop_est'])
        v.append(valor)
        if (valor > vma):
            vma = valor
        if (valor < vmi):
            vmi = valor
        z = z + 1        
    mapa[l[i]] =v
    lista.append(l[i])
    i = i + 1

i=0
output_path = ''

while i < len(lista):

   fig = mapa.plot(lista[i], cmap='Reds', figsize=(10,10),
                  linewidth=1, edgecolor='0', vmin=vmi, vmax=vma,
                  legend=True, norm=plt.Normalize(vmin=vmi, vmax=vma))
   fig.axis('off')
   t = lista[i].split('/')
   fig.set_title('Casos CONFIRMADOS ' + t[1] + '/' + t[0] + '/' + t[2] + ' (casos / millon hab)' , fontdict={'fontsize': '17','fontweight' : '3'})
   fig.annotate('Fuente: Johns Hopkins University Center for Systems Science and Engineering , 2020',
                xy=(0.1, .08), xycoords='figure fraction',
                horizontalalignment='left', verticalalignment='top',
                fontsize=10, color='#555555')
   fi=""
     
   if (i<10) :
       fi = "00" + str(i)
   elif (i<100):
       fi = "0" + str(i)
   else:
       fi = str(i)

   filepath = os.path.join(output_path, fi+'.png')
   chart = fig.get_figure()
   chart.savefig(filepath, dpi=72)
   i = i + 1
   

millis = int(round(time.time() * 1000))
frames = []
imgs = glob.glob("*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save('anim/'+str(millis)+' CONFIRMADOS.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=175, loop=0)    