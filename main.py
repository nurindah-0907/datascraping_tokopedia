import requests
from bs4 import BeautifulSoup

url = 'http://sim.stikombanyuwangi.ac.id/'

req = requests.get(url)
html_parse = BeautifulSoup(req.text, "html.parser")

data = html_parse.find_all('h2', class_='form-signin-heading')

print(data)