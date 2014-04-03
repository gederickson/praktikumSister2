#!/usr/bin/python
'''
Created on Apr 4, 2014

@author: madedia
'''
import xmlrpclib

if __name__ == '__main__':
    proxy = xmlrpclib.ServerProxy("http://localhost:65530")
    url = raw_input("input feed link >> ")
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