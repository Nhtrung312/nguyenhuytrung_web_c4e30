import requests 
import bs4
url =' https://dantri.com.vn/suc-khoe.htm'
response = requests.get(url)
# print(response.content)
bs = bs4.BeautifulSoup(response.content,'html.parser')
print(bs.title)
# all_a_tag = bs.find_all('img',{})

all_a_tag = bs.find_all('div',{'data-boxtype':'timelineposition'})
data_crawled = []
print(len(all_a_tag))
for v in all_a_tag :
    post = {}
    post['title'] = v.div.h2.a['title']
    post['image'] = v.a.img.attrs['src']
    post['text'] = v.div.div.text
    # print(v.div.h2.a['title'])
    # # print(v.div.h2.attrs['title'])
    # print(v.a.img.attrs['src'])
    # print(v.div.div.text)
    data_crawled.append(post)
import json
with open('data.json','wt',encoding='utf-8') as f:
    f.write(json.dumps(data_crawled,ensure_ascii = False,indent=2))

    print()
    print()
