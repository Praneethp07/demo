from bs4 import  BeautifulSoup
import requests
# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# playFile = open( 'RomeoAndJuliet.txt', 'wb')
# Saving Downloaded Files to the Hard Drive
# for chunk in res.iter_content(10000):
#     playFile.write(chunk)
#
# playFile.close()



# Creating Beautiful Soup Object from HTML
res = requests.get('http://nostarch.com')
soup = BeautifulSoup(res.content,'html.parser')
print(soup.prettify())

