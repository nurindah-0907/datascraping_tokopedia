import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/feed/explore'

req = requests.get(url)
html_parse = BeautifulSoup(req.text, "html.parser")

data = html_parse.find_all('h2', class_='style-scope ytd-shelf-renderer')


print(data)