import requests
from bs4 import BeautifulSoup

url = "https://www.teamrankings.com/nfl/stat/yards-per-game"

resp = requests.get(url)
soup = BeautifulSoup(resp.content)

# soup.table finds the first <table> tag in the html
table_headings = soup.table.find_all('th') 
print(table_headings)

# we're usually interested in the text of the element
headings_text = [th.text for th in table_headings]
print(headings_text)

# same example but now for the table rows
table_rows = soup.table.find_all('tr')
row_text = [tr.text for tr in table_rows]