from bs4 import BeautifulSoup 
import requests
url = "" #<--- URL ARTICOLO
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
match = soup.text
print(match)