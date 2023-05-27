from bs4 import BeautifulSoup 
import requests
url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
match = soup.text
print(match)