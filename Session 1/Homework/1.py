import requests
import bs4
url = 'https://www.apple.com/itunes/charts/songs/'


response = requests.get(url)
# print(response.content)
bs = bs4.BeautifulSoup(response.content,'html.parser')
print(bs.title)
all_a_tag = bs.find_all('li')
data_crawled = []
print(len(all_a_tag))
for v in all_a_tag :
    
    post = {}
    post['title'] = v.h3
    post['artist'] = v.h4

    data_crawled.append(post)
print(data_crawled)
import json
with open('data.json','wt',encoding='utf-8') as f:
    f.write(json.dumps(data_crawled,ensure_ascii = False,indent=2))

    print()
    print()

