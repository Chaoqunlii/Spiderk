import requests
import os
from PyQt5.QtCore import pyqtSignal, QThread

class GoogleThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, keywords, picSavePath):
        super(GoogleThread, self).__init__()
        self.keywords = keywords
        self.picSavePath = picSavePath

    def run(self):
        # print(self.keywords)
        # print(self.picSavePath)
        # print('entry googleSpider thread')
        # self.trigger.emit('jeha')
        #
        proxies = {
            "http": "http://127.0.0.1:1080",
            "https": "http://127.0.0.1:1080",
        }
        for keyword in self.keywords:
            print('start outside iterator')
            for page in range(6):
                print('start inside iterator')
                url = 'https://www.google.com/search?ei=9yhvWcT-PJSojQPMiYLACQ&yv=2&q=' + keyword + '&newwindow=1&tbm=isch&vet=10ahUKEwiE1ojXhpXVAhUUVGMKHcyEAJgQuT0InwEoAQ.9yhvWcT-PJSojQPMiYLACQ.i&ved=0ahUKEwiE1ojXhpXVAhUUVGMKHcyEAJgQuT0InwEoAQ&ijn=' + str(page) + '&start=' + str(page) + '00&asearch=ichunk&async=_id:rg_s,_pms:s'
                path = self.picSavePath.replace('/', '\\') + '\\' + keyword
                print(keyword)
                print('path')
                print(path)
                print('wtf')
                if os.path.exists(path):
                    os.chdir(path)
                else:
                    os.mkdir(path)
                    os.chdir(path)

                html = requests.get(url, proxies=proxies)

                source = html.text.replace('JPEG', 'jpg')
                source = source.replace('png', 'jpg')
                import re
                imgs = (re.findall(r"imgurl=(.+?)jpg", source))
                for img in imgs:
                    img = img + 'jpg'
                    img = img.replace('\\', '')
                    print(img)
                    self.trigger.emit(img)
                    name = img.split('/')[-1]
                    try:
                        with open(name, 'wb') as f:
                            f.write(requests.get(img, proxies=proxies).content)
                    except:
                        pass

        self.trigger.emit('任务已完成')