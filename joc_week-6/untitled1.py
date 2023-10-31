# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:20:26 2023

@author: User
"""


import csv
from gmplot import gmplot
gmap =gmplot.GoggleMapPlotter(28.)
with open ('route.csv','r') as f:
    reader =csv.reader(f)
    k=0
    for row in reader:
        lat =float(row[0])
        long =float(row[1])
        print(lat)
        print(long)
        print(lat+long)
        
        if(k==0):
            gmap.marker(lat,long,'yellow')
            k=1
        else:
            gmap.marker(lat,long,'blue')