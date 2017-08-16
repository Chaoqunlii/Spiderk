import requests
import os
import re
from PyQt5.QtCore import pyqtSignal, QThread

class TumblrThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, keywords, picSavePath, picFlag, videoFlag):
        super(TumblrThread, self).__init__()
        self.keywords = keywords
        self.picSavePath = picSavePath
        self.picFlag = picFlag
        self.videoFlag = videoFlag

    def run(self):

        print(self.picFlag)
        print(self.videoFlag)


        proxies = {
            "http": "http://127.0.0.1:1080",
            "https": "http://127.0.0.1:1080",
        }

        url_1 = 'https://api.tumblr.com/v2/blog/'
        url_2 = '.tumblr.com/posts/'
        url_3 = '?api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4&offset='



        for keyword in self.keywords:

            offset = 0
            postsNumber = 20
            i = 0
            print(keyword)
            path = self.picSavePath.replace('/', '\\') + '\\' + keyword
            if os.path.exists(path):
                os.chdir(path)
            else:
                os.mkdir(path)
                os.chdir(path)
            print('path')
            print(path)

            while (offset < postsNumber) and self.picFlag:
                html = requests.get(url_1 + keyword + url_2 + 'photo' + url_3 + str(offset), proxies=proxies).text
                try:
                    postsNumber = int((re.findall(r'total_posts":(.+?),"', html))[1])
                except:
                    break
                if postsNumber == 0:
                    print('nothing')
                    break
                # print(postsNumber)

                imgs = (re.findall(r'\[{"url":"(.+?)","width":', html))
                for img in imgs:
                    print(img)
                    content = requests.get(img, proxies=proxies).content
                    with open(img.split('/')[-1], 'wb') as f:
                        f.write(content)
                    self.trigger.emit(img)
                    i += 1
                print(i)
                offset += 20

            while offset < postsNumber and self.videoFlag:
                self.trigger.emit('视频下载速度较慢,请耐心等待')
                html = requests.get(url_1 + keyword + url_2 + 'video' + url_3 + str(offset), proxies=proxies).text
                try:
                    postsNumber = int((re.findall(r'total_posts":(.+?),"', html))[1])
                except:
                    break
                if postsNumber == 0:
                    print('nothing')
                    break
                # print(postsNumber)

                videos = (re.findall(r'"video_url":"(.+?)","html5', html))
                for video in videos:
                    print(video)
                    self.trigger.emit(video)

                    content = requests.get(video, proxies=proxies).content
                    with open(video.split('/')[-1], 'wb') as f:
                        f.write(content)

                    i += 1
                print(i)
                offset += 20

        self.trigger.emit('任务已完成')