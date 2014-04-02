#!/usr/bin/python
'''
Created on Apr 4, 2014

@author: madedia
'''


from SimpleXMLRPCServer import SimpleXMLRPCServer

import urllib
from elementtree.ElementTree import parse

class RPCServer:
    '''
    classdocs
    '''
    
    #def getRSS(self,url):
        #feeds = feedparser.parse(url)
        
        #print "Channel/Feed title : " + str(feeds.feed.title).encode('utf-8')
        #print "Channel link : " + str(feeds.feed.link).encode('utf-8')
        
        #for feed in feeds['entries']:
            #print "Title : "+str(feed.title).encode('utf-8')
            #print "Authors : "+str(feed.authors).encode('utf-8')
            #print "Pub. Date : "+str(feed.published).encode('utf-8')
            #print "Links : "+str(feed.links).encode('utf-8')
            #print "Summary : "+str(feed.summary).encode('utf-8')
            #print "--------------------------------"
        
        
        #xml = {}
        #xml['channel_title'] = "Channel/Feed title : " + str(feeds.feed.title).encode('utf-8')
        #xml['channel_links'] = "Channel link : " + str(feeds.feed.link).encode('utf-8')
        #collection = []
        #i = 0
        #for feed in feeds['entries']:
            #data = {}
            #data['title'] = str(feed.title).encode('utf-8')
            #data['authors'] = str(feed.authors).encode('utf-8')
            #data['published'] = str(feed.published).encode('utf-8')
            #data['links'] = str(feed.links).encode('utf-8')
            #data['summary'] = str(feed.summary).encode('utf-8')
            #collection.append(data)
            #i+=1
        #xml['entries'] = collection
        #return xml
        
    def getRSS(self, url):
        informasi=[]
        rss = parse(urllib.urlopen(url)).getroot()
        
        for data in rss.findall('gempa'):
            magnitude = data.find('Magnitude').text
            jumlah = data.find('Jumlah').text
            informasi.append([magnitude,jumlah])
           
            print 'Magnitude\t: '+magnitude+'\n'+'Jumlah\t\t: '+jumlah+'\n'
            print'\n================================'
        return informasi
        
        

    def __init__(self):
        '''
        Constructor
        '''
        self.server = SimpleXMLRPCServer(('localhost',65530))
        print "listening at 65530"
        self.server.register_function(self.getRSS, 'getRSS')
        #self.server.allow_none = True
        self.server.serve_forever()
        
        
if __name__ == "__main__":
    server = RPCServer()