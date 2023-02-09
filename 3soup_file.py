from bs4 import BeautifulSoup
import requests

website = 'https://www.biography.com/authors-writers/ayn-rand'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
""" print(soup.prettify()) """
box = soup.find('div', class_="css-1lr08az e12wtocy0")

title = soup.find('h1').get_text()

content = soup.find('div', class_="article-body-content article-body standard-body-content css-z6i669 ewisyje5").get_text(strip=True, separator='\n')

with open(f'{title}.txt', 'w') as file:
	file.write(title)
	file.write(content)

print(title)
print(content)