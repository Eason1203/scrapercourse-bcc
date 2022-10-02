import requests
from bs4 import BeautifulSoup
import time
'''response = requests.get('https://www.taiwannews.com.tw/en/index')'''

start_time = time.time()
for page in range(1,4):
    # print((f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}'))
    response= requests.get(f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}')
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'}) 

    title_list=[]
    for title in titles:
        title_list.append(title.getText())
        urls = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})

    tag_list=[]
    for url in urls:

        sub_response = requests.get(url.get('href'))
        sub_soup = BeautifulSoup(sub_response.text,'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e2o6ii40'})
    
        for tag in tags:
            tag_list.append(tag.getText())
        
    print(title_list)
    print(tag_list) 

   

end_time = time.time()
print(f'花費秒數={end_time-start_time}')  
