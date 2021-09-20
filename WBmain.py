# Wyatt Bentley
# 9-20-21
# Web Scraping EVIT
import requests
import bs4
request = requests.get("https://evit.com/high_school_career_training/hs")
soup = bs4.BeautifulSoup(request.text, 'html.parser')
prognames = soup.select('#ctl00_ContentPlaceHolder1_ctl11_divContent > ul')
for elem in prognames:
    print(elem.getText())