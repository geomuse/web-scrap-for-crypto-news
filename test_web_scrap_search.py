import requests
from bs4 import BeautifulSoup
import time

# url = 'https://www.coindesk.com/search?s=bitcoin'

class cryptonews_scrap :
    '''
    requests 没有延迟读取功能.
    用于发送HTTP请求和处理响应的库,主要用于获取网页内容或进行API调用.
    '''
    def __init__(self,keywords) -> None:
        # self.url = 'https://cryptonews.com/'
        self.url = f'https://cryptonews.com/search/?q={keywords}'

    def get_text(self,text):
        soup = BeautifulSoup(text,'html.parser')
        p_tags = soup.select('p')
        p = BeautifulSoup(str(p_tags),'html.parser')
        return p.get_text().replace("A quick 3min read about today's crypto news!", "")

    def get_link(self,link):
        response = requests.get(link)
        if response.status_code == 200 :
            print('Link getting.')
            return self.get_text(response.text)

    def beauty_soup(self):
        df = requests.get(self.url)
        print(self.url)
        if df.status_code == 200 :
            txts = []
            soup = BeautifulSoup(df.text, 'html.parser')
            # a_tags = soup.find_all('a')
            a_tags = soup.select('[class~=article__title]')
            print(a_tags)
            # a_tags = a_tags[0:10+1]
            # for a_tag in a_tags:
            #     link = a_tag.get("href").replace('/news',f'{self.url}/news')
            #     print(f'{a_tag.text} : {link} ')
            #     txt = self.get_link(link)
            #     print(f'Link have been scraped. {time.strftime("%Y-%m-%d %H:%M:%S")}')
            #     txts.append(txt)
        return txts

if __name__ == '__main__':

    ws = cryptonews_scrap('meme')    
    txt = ws.beauty_soup()
    print(txt)

