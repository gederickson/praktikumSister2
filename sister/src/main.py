'''
Created on Apr 2, 2014

@author: Rah Desta
'''
import urllib
from elementtree.ElementTree import parse

WEATHER_URL = 'http://data.bmkg.go.id/statistiksrgempa2012-01.xml'
rss = parse(urllib.urlopen(WEATHER_URL)).getroot()

print 'Info gempa'
arrayGempa = []
for gempa in rss.findall('gempa'):
    magnitude = gempa.find('Magnitude').text
    arrayGempa.append(magnitude)
    jumlah = gempa.find('Jumlah').text
    arrayGempa.append(jumlah)
    print 'magnitude : ' +magnitude+ ' Jumlah : ' +jumlah