import bs4
import requests

request = requests.get('https://www.evit.com/high_school_career_training/hs')
soup = bs4.BeautifulSoup(request.text, 'html.parser')
programmingName = soup.select('#ctl00_ContentPlaceHolder1_ctl11_divContent > ul')
for elem in programmingName:
    print(elem.getText())
