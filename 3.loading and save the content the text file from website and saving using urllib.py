import urllib.request
import ssl
import os

# Disable SSL certificate verification
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Make the request with SSL certificate verification disabled
content = urllib.request.urlopen('https://www.samsclub.com/robots.txt', context=ssl_context).read()


# Define the directory path
directory_path = os.path.join(os.getcwd(), 'contents')

# Create the 'contents' directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

file = open(os.getcwd()+os.sep+"contents"+os.sep+"robots.txt","wb") #Creating a file robots.txt inside directory 'contents' that exist under current working directory (os.getcwd())

file.write(content) #writing content to file robots.txt opened in line above. If the file doesn't exist inside directory 'contents', Python will throw exception "File not Found"

file.close() #closes the file handle