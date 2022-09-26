import requests
from bs4 import BeautifulSoup
'''response = requests.get('https://www.taiwannews.com.tw/en/index')'''


response = requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')
soup = BeautifulSoup(response.text, 'lxml')
titles = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})

'''
for title in titles:
    print(title.getText())

print(title) '''

title_list=[]
for title in titles:
    title_list.append(title.getText())

print(title_list)   

'''title = soup.find('h3',{'class':'entry-title de_remove-link-color'})
titles = soup.find_all('a',{'class':'bbc-uk8dsi e1d658bg0'})

title_list=[]
for title in titles:
    title_list.append(title.getText())

print(titles)   '''


