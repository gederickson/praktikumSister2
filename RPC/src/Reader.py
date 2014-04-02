'''
Created on Apr 2, 2014

@author: Rickson
'''
import urllib
from elementtree.ElementTree import parse

url = 'http://data.bmkg.go.id/Tes_cuaca_wisata_Bali.xml'

rss = parse(urllib.urlopen(url)).getroot()
forecasts = []
for date in rss.findall('Date'):
    ValidStart = date.find('ValidStart').text
    ValidTimeStart = date.find ('ValidTimeStart').text
    ValidEnd = date.find ('ValidEnd').text
    ValidTimeEnd = date.find ('ValidTimeEnd').text
    print ValidTimeStart, ValidStart+'\n'+  ValidTimeEnd, ValidEnd 