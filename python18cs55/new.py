
from bs4 import BeautifulSoup
import requests

content = requests.get("https://www.teachmint.com/tfile/studymaterial/soumyabhat/computerscience/ch-15-word-processordocx/5f6f6da1-d6bc-4907-a644-39d09a025412")
soup = BeautifulSoup(content.content,"html.parser")

print(soup.title)

