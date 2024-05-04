import requests
import bs4

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
response = requests.get(url)
tree = bs4.BeautifulSoup(response.text, 'html.parser')


for heading in tree.find_all("h2"):
  print(heading.text)


# print(tree.prettify())

