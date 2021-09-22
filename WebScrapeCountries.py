import requests
import bs4
request = requests.get("https://www.biographyonline.net/people/famous-100.html")
soup = bs4.BeautifulSoup(request.text, "html.parser")
progNames = soup.select("#p6641 > section > ul:nth-child(22)")
for elem in progNames:
    print(elem.getText())