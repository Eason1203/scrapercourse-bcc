import requests
from bs4 import BeautifulSoup
'''response = requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt')'''
response = requests.get('https://www.taiwannews.com.tw/en/index')
soup = BeautifulSoup(response.text, 'lxml')
'''title = soup.find('h3',{'class':'entry-title de_remove-link-color'})'''
titles = soup.find_all('h3',{'class':'entry-title de_remove-link-color'})

title_list=[]
for title in titles:
    title_list.append(title.getText())

print(title_list)