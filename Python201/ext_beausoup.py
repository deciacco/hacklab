from urllib import request
import requests
from bs4 import BeautifulSoup

page =  requests.get("https://247ctf.com/scoreboard")
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table")
tbody = table.find("tbody")
rows = tbody.find_all("tr")

for row in rows:
    cols = [x.text.strip() for x in row.find_all("td")]
    print(cols[0], cols[2], cols[4])