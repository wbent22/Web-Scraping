import bs4
import requests
request = requests.get("https://www.healthywa.wa.gov.au/Healthy-living/Recipes/AZ-of-fruit")
soup = bs4.BeautifulSoup(request.text, 'html.parser')
Prognames = soup.select("#contentFull > div > ul")
for elem in Prognames:
    print(elem.getText())