import bs4
import requests

request = requests.get('https://google.com')
soup = bs4.BeautifulSoup(request.text, 'html.parser')
programmingName = soup.select('html')
for elem in programmingName:
    print(elem.getText())