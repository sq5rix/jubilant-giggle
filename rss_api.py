from bs4 import BeautifulSoup
import requests
url = requests.get('https://realpython.com/atom.xml')

soup = BeautifulSoup(url.content, 'xml')
entries = soup.find_all('entry')

for i in entries:
  title = i.title.text
  link = i.link['href']
  summary = i.summary.text
  print(f'Title: {title}\n\nSummary: {summary}\n\nLink: {link}\n\n------------------------\n')
