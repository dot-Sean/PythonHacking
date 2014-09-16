import urllib2
response = urllib2.urlopen('http://python.org/')
print "Response:", response

#print "URL:", response.geturl()

#print "This gets the code:", response.code

#print "the headers are:", response.info()

#print "Date:", response.info()['date']

#print "Server:", response.info()['server']
