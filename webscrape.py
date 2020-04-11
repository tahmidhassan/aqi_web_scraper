# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:48:39 2020

@author: Tahmid Hassan Talukdar

Python webscraper to collect air quality index data from "https://aqicn.org/" and similar sub-websites 

The page has a dynamic table - so I suggest you download and copy paste the html into the index.html file and go from there. 
When downloading make sure you have the appropriate table selected. 

Please provide acknowledgement if using this tool results in an academic publication

"""

# Enter the start and end here in YYYYMM format. 00 means January, 11 means December 

start = 201700 
end = 202003

import pandas as pd
import numpy as np

import requests 
from bs4 import BeautifulSoup

# results = requests.get('website_name_here') 

# src = results.content

src = open("index.html", encoding="utf8")     


soup = BeautifulSoup(src, 'lxml')

# match = soup.find("div", id='historic-aqidata-block').find_all("div", class_='whitebody')

# match = soup.find("div", id='historic-aqidata-block').find_all("tr")


x = pd.DataFrame([])

i = 0
date = start 

while True:
    if i==12:
        i=0
        date = date+88
        
        
    a = str(date)
    
    medu = []
    
    medu.append(a[0:4])
    
    match = soup.find(attrs={"key":a})
    
    month_name = match.find("td").text 
    
    medu.append(month_name)
    
    # print(match)
    
    g = match.find("td", class_="squares")
    
    # print(g)
    
    
    for text in g.find_all("text"):
        medu.append((text.text))
        
    print(medu)
    
    h = pd.DataFrame([medu])
    
    x = x.append(h)
    
    date = date+1
    i=i+1
    
    if date == end:
        break
        
    end 

title = soup.title.text[0:10]

filename = '%s.xlsx' % title

x.to_excel(title+'.xlsx', engine="xlsxwriter")


