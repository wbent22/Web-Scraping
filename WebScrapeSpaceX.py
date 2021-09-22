import requests
import bs4
request = requests.get("https://en.wikipedia.org/wiki/SpaceX")
soup = bs4.BeautifulSoup(request.text, 'html.parser')
prgnames = soup.select('#toc > ul')
for elem in prgnames:
    print(elem.getText())