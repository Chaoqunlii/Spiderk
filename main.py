from ui import *
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from spiders import google, weibo, tumblr, mzitu
from canvas import Canvas
import os, json


global picSavePath, imagePath, imagesPath, mzituEmitCount
picSavePath = 'D:\QtSpiderPics'
imagePath = ''
imagesPath = ''
mzituEmitCount = 0

import sys

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)

        self.currentImg = ''

        # Code below is mine
        # Spider
        self.spiderButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.markButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.settingButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.pushButton_Google.clicked.connect(self.toGoogleSpider)
        self.pushButton_Weibo.clicked.connect(self.toWeiboSpider)

        self.pushButton_PathSelect.clicked.connect(self.pathSelect)

        self.picFlag = True
        self.videoFlag = False
        self.picFlagCheckBox.stateChanged.connect(self.picFlagState)
        self.videoFlagCheckBox.stateChanged.connect(self.videoFlagState)
        self.pushButton_Tumblr.clicked.connect(self.toTumblrSpider)

        self.getData_pushButton.clicked.connect(self.toMzituSpider)

        self.tableWidget_Mztu.setRowCount(5)



        directory1 = 'C:/Users/Cloud/Pictures/Camera Roll'
        for file in os.listdir(directory1):
            if '.jpg' in file:
                fileName = directory1 + '/' + file
                print(fileName)
                item = QtWidgets.QListWidgetItem()
                self.fileList_listWidget.addItem(item)
                item.setText(fileName)

        directory2 = 'D:/QtSpiderPics/TextOnPics/renminribao'
        for file in os.listdir(directory2):
            if '.jpg' in file:
                fileName = directory2 + '/' + file
                print(fileName)
                item = QtWidgets.QListWidgetItem()
                self.fileList_listWidget.addItem(item)
                item.setText(fileName)


        self.fileList_listWidget.setCurrentItem(self.fileList_listWidget.item(0))
        self.canvas = Canvas(self.page_mark, imageDir=self.fileList_listWidget.item(0).data(0))
        self.canvas.loadPoints()
        self.canvas.setObjectName("canvas")
        self.horizontalLayout_2.addWidget(self.canvas)



        self.imageSelect_pushButton.clicked.connect(self.imageSelect)
        self.imagesSelect_pushButton.clicked.connect(self.imagesSelect)
        self.currentItem = self.fileList_listWidget.currentItem()
        self.fileList_listWidget.itemClicked.connect(self.listSelect)

        self.nextPic_pushButton.clicked.connect(self.nextPic)
        self.prePic_pushButton.clicked.connect(self.prePic)



    def nextPic(self):
        try:
            currentItem = self.fileList_listWidget.currentItem()
            if self.canvas.point_painted_4:
                name = currentItem.text().split('.')[0] + '.json'
                print(name)
                content = {
                    "Path": currentItem.text(),
                    "Point_1": self.canvas.point_painted_1,
                    "Point_4": self.canvas.point_painted_4
                }
                with open(name, 'w') as f:
                    f.write(json.dumps(content))

            currentItemRow = self.fileList_listWidget.row(currentItem)
            nextItem = self.fileList_listWidget.item(currentItemRow + 1)
            self.canvas.imageDir = nextItem.text()
            self.canvas.changePic()
            self.canvas.loadPoints()
            self.fileList_listWidget.setCurrentItem(self.fileList_listWidget.item(currentItemRow + 1))
        except:
            print('failed')


    def prePic(self):
        try:
            currentItem = self.fileList_listWidget.currentItem()
            if self.canvas.point_painted_4:
                name = currentItem.text().split('.')[0] + '.json'
                print(name)
                content = {
                    "Path": currentItem.text(),
                    "Point_1": self.canvas.point_painted_1,
                    "Point_4": self.canvas.point_painted_4
                }
                with open(name, 'w') as f:
                    f.write(json.dumps(content))

            currentItemRow = self.fileList_listWidget.row(currentItem)
            nextItem = self.fileList_listWidget.item(currentItemRow - 1)
            self.canvas.imageDir = nextItem.text()
            self.canvas.changePic()
            self.canvas.loadPoints()
            self.fileList_listWidget.setCurrentItem(self.fileList_listWidget.item(currentItemRow - 1))
        except:
            print('failed')

    def listSelect(self, item):
        try:
            # self.currentItem是点击listSelect之前的item
            # print(self.currentItem.text())
            currentItem = self.currentItem
            if self.canvas.point_painted_4:
                name = currentItem.text().split('.')[0] + '.json'
                # print(name)
                content = {
                    "Path": currentItem.text(),
                    "Point_1": self.canvas.point_painted_1,
                    "Point_4": self.canvas.point_painted_4
                }
                with open(name, 'w') as f:
                    f.write(json.dumps(content))
            print('file ok')
            self.canvas.title = item.text()
            self.canvas.imageDir = item.text()
            print('item ok')
            self.canvas.changePic()
            print('changpic ok')
            self.canvas.loadPoints()
            print('loadPoint ok')
            self.currentItem = self.fileList_listWidget.currentItem()
        except:
            print('failed')


    def imagesSelect(self):
        directory = QFileDialog.getExistingDirectory(self.centralwidget, "选取文件夹")
        if directory:
            # print(directory)
            for file in os.listdir(directory):
                fileName = directory + '/' + file
                # print(fileName)
                item = QtWidgets.QListWidgetItem()
                self.fileList_listWidget.addItem(item)
                item.setText(fileName)



    def imageSelect(self):
        directory = QFileDialog.getOpenFileName(self.centralwidget, "选取文件")
        if directory:
            print(directory[0])
            item = QtWidgets.QListWidgetItem()
            self.fileList_listWidget.addItem(item)
            item.setText(directory[0])


    def mzituTable(self, string):
        item = QtWidgets.QTableWidgetItem()
        global mzituEmitCount

        self.tableWidget_Mztu.setRowCount(mzituEmitCount+1)
        print(mzituEmitCount)

        self.tableWidget_Mztu.setItem(mzituEmitCount, 0, item)
        item = self.tableWidget_Mztu.item(mzituEmitCount, 0)
        item.setText(string)
        print(string)
        mzituEmitCount += 1


    def toMzituSpider(self):
        self.mzituSpider = mzitu.MzituThread(picSavePath)
        self.mzituSpider.start()
        self.mzituSpider.picGrouptrigger.connect(self.mzituTable)
        self.mzituSpider.trigger.connect(self.taskStatus)


    def picFlagState(self, state):
        self.picFlag = state
        print(self.picFlag)

    def videoFlagState(self, state):
        self.videoFlag = state
        print(self.videoFlag)


    def pathSelect(self):
        global picSavePath
        directory = QFileDialog.getExistingDirectory(self.centralwidget, "选取文件夹", picSavePath)
        if directory:
            self.plainTextEdit_path.setPlainText(directory)
            picSavePath = directory
            print(picSavePath)


    def toGoogleSpider(self):
        keywords = []
        for keyword in self.plainTextEdit_Google.toPlainText().split('\n'):
            keywords.append(keyword)
        self.googleSpider = google.GoogleThread(keywords, picSavePath)
        self.googleSpider.start()
        self.googleSpider.trigger.connect(self.taskStatus)


    def toWeiboSpider(self):
        keywords = []
        for keyword in self.plainTextEdit_Weibo.toPlainText().split('\n'):
            keywords.append(keyword)
        print(keywords)
        self.weiboSpider = weibo.WeiboThread(keywords, picSavePath)
        self.weiboSpider.start()
        self.weiboSpider.trigger.connect(self.taskStatus)


    def toTumblrSpider(self):
        keywords = []
        for keyword in self.plainTextEdit_Tumblr.toPlainText().split('\n'):
            keywords.append(keyword)
        print(keywords)
        self.tumblrSpider = tumblr.TumblrThread(keywords, picSavePath, self.picFlag, self.videoFlag)
        self.tumblrSpider.start()
        self.tumblrSpider.trigger.connect(self.taskStatus)


    def taskStatus(self, string):
        self.outputText.appendPlainText(string)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    file = open('style.qss', 'r')
    styleSheet = file.read()
    app.setStyleSheet(styleSheet)

    mainWindow = main()
    mainWindow.setWindowIcon(QIcon('resources/spider.png'))
    # mainWindow.setWindowFlags(Qt.FramelessWindowHint)
    # mainWindow.setWindowOpacity(0.925)
    mainWindow.show()

    sys.exit(app.exec_())