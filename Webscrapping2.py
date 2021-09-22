import bs4
import requests

request = requests.get('https://github.com/wyatt-bentley/Web-Scraping')
soup = bs4.BeautifulSoup(request.text, 'html.parser')
programmingName = soup.select('#repo-content-pjax-container > div > div.gutter-condensed.gutter-lg.flex-column.flex-md-row.d-flex > div.flex-shrink-0.col-12.col-md-9.mb-4.mb-md-0 > div.Box.mb-3')
for elem in programmingName:
    print(elem.getText())