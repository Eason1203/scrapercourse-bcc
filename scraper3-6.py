from token import GREATER
import grequests
from bs4 import BeautifulSoup
import time
'''response = requests.get('https://www.taiwannews.com.tw/en/index')'''

start_time = time.time()

links = [f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}' for page in range(1,4)]
# print(links)

reqs= (grequests.get(link) for link in links)
resps = grequests.imap(reqs, grequests.Pool(3))

for index, resp in enumerate(resps):
# 利用enumerate取得page頁數
    soup = BeautifulSoup(resp.text, 'lxml')
    titles = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'}) 

    title_list=[]
    for title in titles:
        title_list.append(title.getText())

    urls = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})
    
    sub_links = [url.get('href') for url in urls]

    sub_reqs= (grequests.get(sub_link) for sub_link in sub_links)
    sub_resps = grequests.imap(sub_reqs, grequests.Pool(10))

    tag_list=[]
    for sub_resp in sub_resps:
        sub_soup = BeautifulSoup(sub_resp.text,'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'})
    
        for tag in tags:
            tag_list.append(tag.getText())
        
    print(f"第{index+1}頁")
    print(title_list)
    print(f'Tag{tag_list}') 

   

end_time = time.time()
print(f'花費秒數={end_time-start_time}')  
