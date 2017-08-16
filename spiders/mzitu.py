import requests
import os
import time
from bs4 import BeautifulSoup
from PyQt5.QtCore import pyqtSignal, QThread

class MzituThread(QThread):
    picGrouptrigger = pyqtSignal(str)
    trigger = pyqtSignal(str)

    def __init__(self, picSavePath):
        super(MzituThread, self).__init__()
        self.picSavePath = picSavePath + '\mzitu'


        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1836.400 QQBrowser/9.5.9947.400",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Referer": "http://www.mzitu.com/99009/38",
        }

    def run(self):

        if os.path.exists(self.picSavePath):
            os.chdir(self.picSavePath)
        else:
            os.mkdir(self.picSavePath)
            os.chdir(self.picSavePath)

        html = requests.get('http://www.mzitu.com/all/')
        soup = BeautifulSoup(html.text, 'lxml')
        all = soup.find('div', class_='all')
        urls = all.findAll('a')
        for url in urls:
            print(url['href'])
            self.picGrouptrigger.emit(url.text)
            picUrl = url['href']
            while picUrl:
                picGroup = requests.get(picUrl).text
                groupSoup = BeautifulSoup(picGroup, 'lxml')
                try:
                    nextPage = groupSoup.find('span', text='下一页\xbb')
                    picUrl = nextPage.parent['href']
                    self.trigger.emit(picUrl)

                    imgContainer = groupSoup.find('div', class_='main-image')
                    img = imgContainer.find('img')['src']
                    print(img)
                    name = img.split('/')[-1]
                    with open(name, 'wb') as f:
                        f.write(requests.get(img, headers= self.headers).content)
                    time.sleep(1)
                except:
                    picUrl = None