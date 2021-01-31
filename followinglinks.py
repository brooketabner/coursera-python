# extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name
# in the list, follow that link and repeat the process a number of times and report the last name you find. 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: M

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve all of the anchor tags
tags = soup('a')
#print(tags)
url = tags[position-1].get('href', None)
print(url)

for i in range(1, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print(url)


#for tag in tags:
#    print(tag.get('href', None))
    

