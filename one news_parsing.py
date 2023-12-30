import requests as rq
from bs4 import BeautifulSoup
import requests

page = rq.get("https://sysblok.ru/interviews/zlachnye-oblasti-nauki-mihail-gelfand-o-plagiate-lishenii-stepeni-i-nejeffektivnyh-chinovnikah/")
print(page)

soup = BeautifulSoup(page.text, features="html.parser")

print(soup.find('time'))

print(soup.find('h1'))

for i in soup.find_all('p'):
  print(i.text.strip())

print(soup.find_all('meta', {'name' : 'author'}))

#наверное, так нельзя искать атрибут, поэтому и не ищет:((
for i in soup.find_all("rel"):
 if i.get("rel") == ["category", "tag"]:
    print(i.get("rel"))
