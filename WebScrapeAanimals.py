import requests
import bs4
request = requests.get("https://animals.net/")
soup = bs4.BeautifulSoup(request.text, 'html.parser')
prgnames = soup.select("#gti_div_A > ul")
for elem in prgnames:
    print(elem.getText())