import urllib
import re

urls=["http://google.com","https://cnn.com","https://nytimes.com"]
regex='<title>(.+?)</title>'
pattern=re.compile(regex) #coverts so that it can be read by the regex lib

i=0
while i<len(urls):
    htmlfile=urllib.urlopen(urls[i])
    htmltext=htmlfile.read()
    titles=re.findall(pattern,htmltext)
    print titles

    i+=1
    

    
