from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# You need to adjust this code to 
# look for span tags and 
tags = soup('span')
count = 0
sum = 0

# pull out the text content of the span tag,
for tag in tags:
    count = count + 1
    
    # convert them to integers and  add them up to complete the assignment. 
    sum = sum + int(tag.contents[0])
    #print (tag.contents[0])

print('Count',count)
print('Sum', sum)

