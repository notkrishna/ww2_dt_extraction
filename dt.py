import pandas as pd
import requests 
from bs4 import BeautifulSoup as s
import numpy
import re

r = requests.get('https://en.wikipedia.org/wiki/World_War_II_casualties')
soup = s(r.content,'html.parser')

cols=[]

dt = soup.select('table')[0]
for i in dt.select('th'):
    cols.append(i.get_text().strip().replace('\xa0%',''))

country=[]
c = [i.name for i in countries]
for i in dt.select('tr b'):
    country.append(i.get_text().strip().replace('\xa0',''))

df = pd.read_html('https://en.wikipedia.org/wiki/World_War_II_casualties')[0]
df = df.drop(61)
df['Country'] = country
df = df.iloc[:-1,:-1]
df = df.drop(['Civilian deaths due towar-related famine and disease'],axis=1)

for i in range(len(df.columns)):
    df.iloc[:,i]=df.iloc[:,i].str.replace(r"[\(\[].*?[\)\]]", "",regex=True)

df = df.rename(columns={'Total population1/1/1939': 'Total population as of 1/1/1939'})

df.to_csv('ww2_dataset.csv')




