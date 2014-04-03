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
           
    def getRSS(self, url):
        informasi=[]
        message =''
        rss = parse(urllib.urlopen(url)).getroot()
        
        for data in rss.findall('gempa'):
            magnitude = data.find('Magnitude').text
            jumlah = data.find('Jumlah').text
            informasi.append([magnitude,jumlah])
           
            message = message + 'Magnitude\t: '+magnitude+'\n'+'Jumlah\t\t: '+jumlah+'\n'
            print'\n================================'
      
        return message;
        
        

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