import urllib.request

urllib.request.urlretrieve('https://www.samsclub.com/robots.txt') #urllib.request returns a tuple with the filename and HTTP headers
#('C:\\Users\\*****\AppData\\Local\\Temp\\tmpjs_cktnc', <http.client.HTTPMessage object at 0x04029110>)

urllib.request.urlretrieve(link,"testrobots.txt") #urlretrieve(url, filename=None)
#('testrobots.txt', <http.client.HTTPMessage object at 0x04322DF0>)

