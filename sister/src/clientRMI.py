'''
Created on Apr 3, 2014

@author: Rah Desta
'''
import rpyc

class client():
    def start(self):
        self.connecting()
    
    # function connecting
    # connect to server
    # load function from connection to getData       
    def connecting(self):
        client.server = rpyc.connect('localhost',5000, config = {'allow_public_attrs':True}) 
        self.getData()
        

    def getData(self):
        print "Informasi Gempa Indonesia tahun 2011"
        print "===================================="
        print "Pilih bulan gempa (1-12)"
        print "0 untuk semua"
        var = input("Input : ")
        print "Mengambil data dari server... "
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
        
        # call function in server 
        informasiCuaca = client.server.root.getRSS(url)
        info = informasiCuaca
        print info
        
# start client program
temp = client()
temp.start()
