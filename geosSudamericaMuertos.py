# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:13:05 2020

@author: ValeYBrau
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import os
import subprocess
import glob
from PIL import Image

df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

listaPaises = ['Chile','Argentina','Brazil','Uruguay','Bolivia',
      'Paraguay','Peru','Ecuador','Colombia',
      'Venezuela','Guyana','Suriname']

df  = df[df['Country/Region'].isin(listaPaises)]

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

mapa  = world[world['name'].isin(listaPaises)]

mapa = mapa.sort_values(["name"], ascending = (True))

pa = mapa['name'].tolist()
pob =mapa['pop_est'].tolist()


lista = df.columns
cols = lista.size -1
i = 1
l = []

while i <= cols:
    l.append(lista[i])
    i = i + 1

valores  = pd.DataFrame()
valores['Pais']=pa

i=1
while i < cols:
    z = 0
    v = []
    while z < len(pa) :
        v.append(float((df.iloc[z][l[i]]*1000000)/pob[z]))
        #v.append(float((df.iloc[z][l[i]])))
        z = z + 1

    valores[l[i]]=v
    i = i + 1


vma = 0
vmi = 999999999
vmax = valores.max(axis=1)
vmin = valores.min(axis=1)

for m in vmax:
    if (float(m) > float(vma)):
        vma = m
        
for m in vmin:
    if (m < vmi):
        vmi = m

lista = valores.columns
cols = lista.size -1

i=38
while i < lista.size:
    z = 0
    v = []
    while z < len(pa) :
        mul = 1000000
        v.append(valores.iloc[z][l[i]])
        z = z + 1
    mapa[l[i]] =v
    i = i + 1

i=38
output_path = ''
cont = 0


while i < lista.size:
   fig = mapa.plot(l[i], cmap='gist_gray_r', figsize=(10,10),
                  linewidth=1, edgecolor='0', vmin=vmi, vmax=vma,
                  legend=True, norm=plt.Normalize(vmin=vmi, vmax=vma))
   fig.axis('off')
   t = lista[i].split('/')
   fig.set_title('Casos FALLECIDOS ' + t[1] + '/' + t[0] + '/' + t[2] + ' (casos / millon hab)' , fontdict={'fontsize': '17','fontweight' : '3'})
   fig.annotate('Fuente: Johns Hopkins University Center for Systems Science and Engineering , 2020',
                xy=(0.1, .08), xycoords='figure fraction',
                horizontalalignment='left', verticalalignment='top',
                fontsize=10, color='#555555')
   fi=""
     
   if (cont<10) :
       fi = "0" + str(cont)
   else:
       fi = str(cont) 
   filepath = os.path.join(output_path, fi+'.png')
   chart = fig.get_figure()
   chart.savefig(filepath, dpi=72)
   cont = cont + 1
   i = i + 1


frames = []
imgs = glob.glob("*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save('00000.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=175, loop=0)











#BORRO DE VALORES LOS QUE NO ME INTERESAN







    #print (l[i])
    
    #EN MAPA TENGO LOS VALORES QUE QUIERO
    #EN LISTA TENGO LA FECHA (usar el subindice i)















"""




while i < lista.size:
   #print(mapa[lista[i]])
   #print("---------------------------------")
   fig = mapa.plot(l[i], cmap='Reds', figsize=(10,10),
                  linewidth=1, edgecolor='0', vmin=vmi, vmax=vma,
                  legend=True, norm=plt.Normalize(vmin=vmi, vmax=vma))
   fig.axis('off')
   t = lista[i].split('/')
   fig.set_title('Casos CONFIRMADOS ' + t[1] + '/' + t[0] + '/' + t[2] + ' (casos / millon hab)' , fontdict={'fontsize': '20','fontweight' : '3'})
   fig.annotate('Fuente: Johns Hopkins University Center for Systems Science and Engineering , 2020',
                xy=(0.1, .08), xycoords='figure fraction',
                horizontalalignment='left', verticalalignment='top',
                fontsize=10, color='#555555')
   fi=""
     
   if (cont<10) :
       fi = "0" + str(cont)
   else:
       fi = str(cont) 
   filepath = os.path.join(output_path, fi+'.png')
   chart = fig.get_figure()
   chart.savefig(filepath, dpi=72)
   cont = cont + 1
   i = i + 1
























pa.append("Argentina")
pa.append("Bolivia")
pa.append("Brazil")
pa.append("Chile")
pa.append("Colombia")
pa.append("Ecuador")
pa.append("Guyana")
pa.append("Paraguay")
pa.append("Peru")
pa.append("Suriname")
pa.append("Uruguay")
pa.append("Venezuela")

pob.append(44270000)
pob.append(11350000)
pob.append(209300000)
pob.append(18000000)
pob.append(49650000)
pob.append(17080000)
pob.append(779094)
pob.append(6950000)
pob.append(31990000)
pob.append(575991)
pob.append(3457000)
pob.append(28870000)



c = []
c.append("b")
c.append("g")
c.append("r")
c.append("y")





mapa = world.loc[(world['name']=='Argentina') |
              (world['name']=='Brazil') |
              (world['name']=='Chile') |
              (world['name']=='Uruguay') | 
              (world['name']=='Paraguay')| 
              (world['name']=='Bolivia')| 
              (world['name']=='Peru')| 
              (world['name']=='Ecuador')| 
              (world['name']=='Colombia')| 
              (world['name']=='Venezuela')| 
              (world['name']=='Guyana')| 
              (world['name']=='Suriname')]

i=1
    
while i < 35:
    print(i)
    valores = valores.drop(l[i], 1)
    i = i +1
    


z = 0
while z < 4 :
    i = 1
    v = []
    l2= []
    
    
    p=[]
    l3=[]
    #print (z)                    
    while i <= cols:
        
        if (df.iloc[z][lista[i]] > 0 ):
            v.append((df.iloc[z][lista[i]]*1000000)/pob[z])
        else:
            v.append(0)
            
        if (df.iloc[z][lista[i]] >= 100 ):
            p.append(df.iloc[z][lista[i]])
            l3.append(lista[i])
        
        l2.append(lista[i])
        
     
    for dia in l:
        print(df.iloc[z][dia])
        #print(df.loc[df[dia]])
    print("----------------------------------------------")
    z = z + 1

"""

