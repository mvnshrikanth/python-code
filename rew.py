from bs4 import BeautifulSoup
import requests
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
html = response.text
soup = BeautifulSoup(html,'html.parser')
#print(soup.p.find_all('a'))
print(soup.find(id="image-gallery"))