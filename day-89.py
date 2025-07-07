#Request module
import requests
from bs4 import BeautifulSoup

url = "https://manga-x.vercel.app/files/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

count = 0
for div in soup.find_all("div", class_='manga-home'):
    print(div['data-title'])
    count += 1

print(count)