#!/usr/bin/python
'''
Created on Apr 4, 2014

@author: madedia
'''
import xmlrpclib

if __name__ == '__main__':
    proxy = xmlrpclib.ServerProxy("http://localhost:65530")
    
    print "Informasi Gempa Indonesia tahun 2011"
    print "===================================="
    print "Pilih bulan gempa (1-12)"
    print "0 untuk semua"
    var = input("Input : ")
    if var == 0:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011.xml'
    elif var == 1:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-01.xml'
    elif var == 2:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-02.xml'
    elif var == 3:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-03.xml'
    elif var == 4:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-04.xml'
    elif var == 5:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-05.xml'
    elif var == 6:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-06.xml'
    elif var == 7:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-07.xml'
    elif var == 8:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-08.xml'
    elif var == 9:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-09.xml'
    elif var == 10:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-10.xml'
    elif var == 11:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-11.xml'
    elif var == 12:
        url = 'http://data.bmkg.go.id/statistiksrgempa2011-12.xml'
    #url = raw_input("input feed link >> ")
    #url = 'http://data.bmkg.go.id/statistiksrgempa2012.xml'
    feeds = ''
    feeds = proxy.getRSS(url)
    #print feeds['channel_title']
    #print feeds['channel_links']
    #print ""
    #for feed in feeds['entries']:
        #print feed['title']
        #print feed['authors']
        #print feed['published']
        #print feed['links']
        #print feed['summary']
        #print "----------------------------------------------"
    print feeds