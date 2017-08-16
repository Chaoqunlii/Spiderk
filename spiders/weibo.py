# -*- coding: utf-8 -*-
from urllib.parse import quote
from bs4 import BeautifulSoup
import time
import datetime
# from pymongo import MongoClient
import requests
import os
from PyQt5.QtCore import pyqtSignal, QThread


class WeiboThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, keywords, picSavePath):
        super(WeiboThread, self).__init__()
        self.keywords = keywords
        self.picSavePath = picSavePath

        client = MongoClient()
        db = client['weibo_crawl']  ## select one database
        self.weibo_crawl_collection = db['weibo_toid']  ## select one collection in database weibo_crawl
        self.url = ''  ## page url
        self.tweet = ''
        self.pics = ''

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.1836.400 QQBrowser/9.5.9947.400",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

        self.cookies = {
            "_T_WM": "e3006125d49c0982c40920f46cd512ee",
            "ALF": "1501138943",
            "SCF": "AtpcEWrcqyERH4ziHedDp6YFU6BVjRYp1dVyicd2bKewCC7kN3rCURSekE7CuMJAiyAabwJn288NyvkKQx-fVCc.",
            "SUB": "_2A250VnNQDeRhGeRM4lcY8i7Jzz-IHXVXuR0YrDV6PUJbktBeLXPxkW2KfuluZHPBnePDZ-BowbNfe3GPwA..",
            "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WFpeveC0exhhKqESnUynUzr5JpX5o2p5NHD95QEeo.f1Kz7SKB0Ws4Dqcj6i--Ri-8si-2fi--NiK.Xi-2Ri--ciKnRi-zNi--fi-zNi-zEi--ci-z0i-2Ri--4iK.XiKn7i--fiK.0iKnR",
            "SUHB": "0LcTU64iDbDX6h",
            "SSOLoginState": "1498546944",
        }

    def request(self, url):
        # cookies = random.choice(self.cookieslist)
        time.sleep(2)
        request = requests.get(url, cookies=self.cookies, headers=self.headers)
        # print('Now parsing:'),
        # print url
        return request

    # def nextPage(soup):
    #     soup.find(class_='tc')

    def img_Url_Maker(self, img_url_):
        url_1 = img_url_.split('=', 3)
        url_2 = url_1[2].split('&', 1)
        url_3 = url_2[0]
        img_prefix = "http://ww3.sinaimg.cn/large/"
        img_tail = ".jpg"
        img_url = img_prefix + url_3 + img_tail
        return img_url

    def get_url_soup(self, url):
        soup = BeautifulSoup(self.request(url).text, 'lxml')
        return soup

    def next_Page_Maker(self, page_soup):
        # print('pagesoup')
        # s
        spl1 = page_soup.split('>', 3)[1]
        spl2 = spl1.split('"', 2)[1]
        spl3 = spl2.split(';', 1)[0]
        next_page_prefix = 'http://weibo.cn/'
        next_page = next_page_prefix + spl3
        return next_page

    def get_imggroup_url(self, soup):
        class_ib = soup.find(class_='ib')
        return class_ib

    def get_index_num(self, soup):
        pa = soup.find(class_='pa').input
        print(pa)
        pa_split = str(pa).split('"', 7)[5]
        print(pa_split)
        return pa_split

    # 点击每个微博的配图（非 共x张图 那个），则进入组图的每一张图片的一个页面，
    def get_img_url(self, page_soup):
        img_url_ = page_soup.find(class_='c').next_sibling.next_sibling
        print('sibling')
        print(img_url_)
        img_url = self.img_Url_Maker(img_url_.a.get('href'))
        # print('img is: '),
        # print img_url
        return img_url

    def get_page_num(self, group_soup):
        tc = group_soup.find(class_='tc')
        if tc:
            print('tc')
            print(tc)
            page_num_split1 = str(tc).split('/', 1)[1]
            page_num = page_num_split1.split('<')[0]
            return int(page_num)

    def get_next_page_url(self, page_soup):
        tc = page_soup.find_all(class_='tc')
        # class tc is the container of next-page
        if tc:
            next_page = self.next_Page_Maker(str(tc[1]))
            return next_page

    def mkdir(self, path):
        isExists = os.path.exists(path)
        if not isExists:
            print('Created one folder named: ', path)
            os.makedirs(path)
            return True
        else:
            print(path, "has already been existed")
            return False

    # iterate contents of one picture group,the group will has one or more pics
    def ite_group(self, group_url):
        img_group_Soup = self.get_url_soup(group_url)
        print('***************************************img_group_soup')
        print(img_group_Soup)
        # Get the img url of this page
        img_url = self.get_img_url(img_group_Soup)
        print('img_url')
        print(img_url)
        self.save(img_url)
        pics = ''
        name = img_url[28:]
        pics = name + ', '

        page_num = self.get_page_num(img_group_Soup)
        print(page_num)

        cur_page_soup = img_group_Soup
        if page_num:
            p = 2
            while p < page_num + 1:
                next_page_url = self.get_next_page_url(cur_page_soup)
                # print("next page url:")
                # print next_page_url
                next_page_soup = self.get_url_soup(next_page_url)
                print('next img')
                next_page_img = self.get_img_url(next_page_soup)
                print(next_page_img)

                name = next_page_img[28:]
                pics = pics + name + ', '

                self.save(next_page_img)
                p += 1
                cur_page_soup = next_page_soup

        return pics

    def save(self, img_url):
        # name = img_url[10:]
        # f = open(name, 'ab')
        # f.write(self.request(img_url).content)
        # f.close()
        name = img_url[28:]
        with open(name, 'ab') as f:
            f.write(self.request(img_url).content)

        print(name + ' was saved')
        self.trigger.emit(img_url)

    def run(self):
        # keyword = raw_input("Please input user-id: ")
        # keyword ='3669102477'
        # 三生三世十里桃花、微微一笑很倾城、花千骨、 青云志、蜜月转、欢乐颂、步步惊心，绝迹, 神雕侠侣,半数传奇，他来了请闭眼, 伪装者,盗墓笔记
        # '5639143988','3899509744','5099675590', '5603168736','5369040666', '5452486353', '5558298656'
        # keyword_pool_u = [
        #     # 'u/5640905483',
        #     # 'xuezhiqian',
        #     # 'u/1890263833',
        #     'livezx',
        # ]

        for keyword in self.keywords:

            keyword_quote = quote(keyword)
            path = self.picSavePath + '\\weibo_' + keyword
            self.mkdir(path)
            os.chdir(path)

            url_prefix = 'http://weibo.cn/'
            url_tail = "?page="
            # indexNum is the number of search index page
            indexNum = str(1)

            # each page
            url = url_prefix + keyword_quote + url_tail + indexNum
            print(url)

            index_soup = self.get_url_soup(url)
            # print(index_soup)

            max_Num = int(self.get_index_num(index_soup))
            print('max_Num')
            print(max_Num)

            i = 1

            while i <= max_Num:
                # iterate every index_page's content
                print('now prepare to print html:'),
                # print(url)
                # time.sleep(3)
                index_soup = self.get_url_soup(url)
                contents = index_soup.find_all(class_='c')
                for c in contents:
                    tweet = c.get_text()
                    print('tweet?')
                    print(tweet)
                    self.tweet = tweet

                    try:
                        ib = c.find(class_='ib')
                        # a is the container of picture group`s href which means the first page of picture-group-url
                        a = ib.parent
                        # group url is also the first page of group
                        group_url = a.get('href')
                        self.url = group_url
                        print(self.url)
                    except:
                        self.url = u'None:这条微博没有配图'
                        group_url = ''

                    if group_url:
                        print(group_url)
                        self.pics = self.ite_group(group_url)
                    else:
                        self.pics = ''

                    #
                    #
                    # try:
                    #     self.weibo_crawl_collection.find_one({'Tweet': tweet})
                    # except:
                    #     print('MondoDB罢工了')
                    #     self.trigger.emit('MondoDB罢工了')
                    #     break
                    #
                    # if self.weibo_crawl_collection.find_one({'Tweet': tweet}):
                    #     print('This page group has been crawled.')
                    # else:
                    #     if group_url:
                    #         print(group_url)
                    #         self.pics = self.ite_group(group_url)
                    #     else:
                    #         self.pics = ''
                    #     post = {
                    #         'PicGroupUrl': self.url,
                    #         'Tweet': self.tweet,
                    #         'Pics': self.pics,
                    #         'Time': datetime.datetime.now()
                    #     }
                    #     self.weibo_crawl_collection.save(post)

                    i += 1
                    indexNum = str(i)
                    url = url_prefix + keyword + url_tail + indexNum

        self.trigger.emit('任务已完成')