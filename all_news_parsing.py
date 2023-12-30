import requests as rq
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


page = rq.get('https://sysblok.ru')

print(page)
print(type(page))

def get_news_links(url, start=1, end=3): #решила парсить 3 стр., чтобы не сильно долго думал:)
   news_links = []
   for page in range(start, end+1):
       news_link = f"{url}/page/{page}"
       news_links.append(news_link)
   return news_links
start_url = 'https://sysblok.ru'
news_links = get_news_links(start_url)
for link in news_links: print(link)


all_links = []
for i in range(len(news_links)):
    all_links.append(news_links[i])

print(all_links)


urls_pages = []
for i in all_links:
    url_pages = i
    page = rq.get(url_pages)
    soup = BeautifulSoup(page.text, features="html.parser")
    for i in soup.find_all("a"):
     if i.parent.name == "h2":
         urls_pages.append(i.get('href'))

print(urls_pages)


def Top(url0):
      page0 = rq.get(url0)
      soup0 = BeautifulSoup(page0.text, features="html.parser")
      date = soup.find_all('time')[0].text
      title = soup0.find_all("h1")[0].text
      text_list = soup0.find_all('p')
      text = []
      for i in text_list:
          text.append(i.text)
      final_text = ' '.join(text)
      return url0, date, title, final_text


Top_news = []

for link in urls_pages:
    news = Top(link)
    Top_news.append(news)

print(Top_news)


df = pd.DataFrame(Top_news)
df.head()

df.columns = ['link','date', 'title', 'text']

df.head(1)

df.to_excel('news.xlsx')

read = pd.read_excel('news.xlsx')
print(read)
