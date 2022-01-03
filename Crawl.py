import requests
from bs4 import BeautifulSoup
import re
pages =['https://vnexpress.net/the-gioi']
take_content=[]
links = ['']
for page in range(2,400):
    url = 'https://vnexpress.net/the-gioi-p'+str(page)
    pages.append(url)

for eachPage in pages:
    res = requests.get(eachPage)
    soup = BeautifulSoup(res.text, 'html.parser')
    contents = soup.find_all('h3', attrs={'class': 'title-news'})
    for content in range(len(contents)):
        take_content.append(contents[content])
    links = [link.find('a').attrs["href"] for link in take_content]
print(len(links))
print(links)
i=0
for link in links:
        news = requests.get(link)
        soup = BeautifulSoup(news.content, "html.parser")
        title = soup.find_all('p',attrs='Normal')
        #title = re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?','', title)
        title = re.sub(r'<[^>]+>', '', str(title))
        file = open('Data/the_gioi/the_gioi '+str(i)+'.txt','w+',encoding='utf-8')
        file.write(title)
        file.close()
        i+=1


