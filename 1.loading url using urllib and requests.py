
#making a request to the link and willing to see the response returned by both libraries, that is, urllib and requests:


import urllib
import requests

import urllib.request as req #import module request from urllib
link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = req.urlopen(link)  #load the link using method urlopen()

print(type(response))   #print type of response object
    #<class 'http.client.HTTPResponse'>

print(response.read()) #read response content
#b'<!DOCTYPE html>\n<html class="client-nojs" lang="en"


import requests
link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = requests.get(link)

print(type(response))
    #<class 'requests.models.Response'>

content = response.content #response content received
print(content[0:150])  #print(content) printing first 150 character from content

#b'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title>List of most popular websites - Wikipedia</title>'

