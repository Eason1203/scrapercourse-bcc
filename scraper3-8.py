import requests
from bs4 import BeautifulSoup

headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
try:
    response = requests.get('https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt', headers = headers, timeout =5, )
    if response.status_code ==200:
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('a',{'class':'bbc-uk8dsi e1d658bg0'})
        if title:
            result =title.getText()
            print(result)
        else:
            print('元素不存在')
    else:
        print("No connection")
except Exception as e:
    print(str(e))