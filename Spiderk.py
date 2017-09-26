# -*- coding: utf-8 -*-
from ui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QListView, QInputDialog, QProgressDialog
from spiders import google, weibo, tumblr, mzitu
from canvas import Canvas
import os, json, shutil, sys


global picSavePath, imagePath, imagesPath, mzituEmitCount, ctrlPressed, IMAGE_SIZE, setting_imageClass
IMAGE_SIZE = QSize(300, 300)
imagePath = ''
imagesPath = ''
mzituEmitCount = 0



with open('resources/settings.json') as f:
    settingsFile = f.read()
try:
    settings = json.loads(settingsFile)
    setting_imageClass = settings.get('imageClass')
    picSavePath = settings.get('picSavePath')
except:
    setting_imageClass = []
    picSavePath = 'D:/Spiderk'

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)

        self.currentImg = ''
        _translate = QtCore.QCoreApplication.translate
        self.ctrlPressed = False
        # Code below is mine
        # Spider
        self.spiderButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.classButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.markButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.settingButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))


        self.pushButton_Google.clicked.connect(self.toGoogleSpider)
        self.pushButton_Weibo.clicked.connect(self.toWeiboSpider)

        self.pushButton_PathSelect.clicked.connect(self.pathSelect)

        self.picFlag = True
        self.videoFlag = False
        self.picFlagCheckBox.stateChanged.connect(self.picFlagState)
        self.videoFlagCheckBox.stateChanged.connect(self.videoFlagState)
        self.pushButton_Tumblr.clicked.connect(self.toTumblrSpider)

        self.getData_pushButton.clicked.connect(self.toMzituSpider)
        self.plainTextEdit_path.setPlainText(picSavePath)
        self.tableWidget_Mztu.setRowCount(5)
        # 标注页面添加图片
        cwd = os.getcwd()
        try:
            directory1 = cwd + '\\resources\demoImages'
            for file in os.listdir(directory1):
                if '.jpg' or '.png' or '.jpeg' or '.bmp' or '.JPG' or '.JPEG' or '.PNG' or '.BMP' in file:
                    fileName = directory1 + '\\' + file
                    # print(fileName)
                    item = QtWidgets.QListWidgetItem()
                    self.fileList_listWidget.addItem(item)
                    item.setText(fileName)
        except:
            pass


        self.fileList_listWidget.setCurrentItem(self.fileList_listWidget.item(0))
        if self.fileList_listWidget.item(0):
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


        self.images_listWidget.setIconSize(IMAGE_SIZE)
        self.images_listWidget.setResizeMode(QListView.Adjust)
        self.images_listWidget.setViewMode(QListView.IconMode)
        self.images_listWidget.setMovement(QListView.Static)
        self.images_listWidget.setLayoutMode(QListView.Batched)
        self.images_listWidget.setSpacing(8)
        #
        self.images_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)



        # 分类页面中添加图片
        try:
            dir = cwd + '\\resources\demoImages'
            for file in os.listdir(dir):
                if  '.jpg' or '.png' or '.jpeg' or '.bmp' or '.JPG' or '.JPEG' or '.PNG' or '.BMP' in file:
                    fileName = dir + '\\' + file
                    # print(fileName)

                    item = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(fileName), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    item.setIcon(icon)
                    item.setToolTip(fileName)

                    self.images_listWidget.addItem(item)
            for imageClass in setting_imageClass:
                self.addClass(imageClass)
        except:
            pass

        try:
            self.addClass_pushButton.clicked.connect(self.addClass)
        except:
            pass
        self.addFolder_pushButton.clicked.connect(self.addClassFolder)

        self.big_pushButton.clicked.connect(self.bigPic)
        self.small_pushButton.clicked.connect(self.smallPic)


    def closeEvent(self, a0: QtGui.QCloseEvent):
        setting_imageClass = []
        for child in self.classFrame.findChildren(QtWidgets.QPushButton):
            if child.objectName() == 'labelPushButton':
                labelText = child.text()
                labelText = labelText.split('-')[0]
                setting_imageClass.append(labelText)

        settings["imageClass"] = setting_imageClass
        settings['picSavePath'] = picSavePath
        content = settings

        with open('resources/settings.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(content))



    def bigPic(self):
        global IMAGE_SIZE
        IMAGE_SIZE = QSize(IMAGE_SIZE.width() + 10, IMAGE_SIZE.height() + 10)
        self.images_listWidget.setIconSize(IMAGE_SIZE)

    def smallPic(self):
        global IMAGE_SIZE
        IMAGE_SIZE = QSize(IMAGE_SIZE.width() - 10, IMAGE_SIZE.height() - 10)
        self.images_listWidget.setIconSize(IMAGE_SIZE)


    def wheelEvent(self, a0: QtGui.QWheelEvent):
        if self.ctrlPressed:
            global IMAGE_SIZE
            deltaY = a0.angleDelta().y()/12
            IMAGE_SIZE = QSize(IMAGE_SIZE.width()+deltaY, IMAGE_SIZE.height()+deltaY)
            self.images_listWidget.setIconSize(IMAGE_SIZE)


    def keyReleaseEvent(self, a0: QtGui.QKeyEvent):
        if a0.key() == QtCore.Qt.Key_Control:
            self.ctrlPressed = False
            print('ctrl is release')
        return super().keyReleaseEvent(a0)

    def keyPressEvent(self, a0: QtGui.QKeyEvent):
        if a0.key() == QtCore.Qt.Key_Control:
            self.ctrlPressed = True
            print('Ctrl is holding down')
        return super().keyPressEvent(a0)


    def addClassFolder(self):
        try:
            dir = QFileDialog.getExistingDirectory(self.centralwidget, "选取文件夹")
            for file in os.listdir(dir):
                if '.jpg' or '.png' or '.jpeg' or '.bmp' or '.JPG' or '.JPEG' or '.PNG' or '.BMP' in file:
                    fileName = dir + '\\' + file
                    # print(fileName)

                    item = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(fileName), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    item.setIcon(icon)
                    item.setToolTip(fileName)
                    self.images_listWidget.addItem(item)
                    QCoreApplication.processEvents()
            print('添加完毕')
            self.classImagePath.setText(dir + ' count:' + str(self.images_listWidget.count()))
        except:
            pass


    def updatelabelPushButton(self):
        count = 1
        children = self.classFrame.findChildren(QtWidgets.QPushButton)
        for child in children:
            if child.objectName() == 'labelPushButton':
                child.setShortcut(str(count))
                text = child.text().split('-')[0]
                print(child)
                print(child.text())
                print("text: " + text)
                print("count: "+ str(count))
                # child.setText( text + '-' + str(count))   操操操，加了这行最后一个label的快捷键就bug
                count += 1


    def closeLabel(self, frame):
        frame.deleteLater()
        self.updatelabelPushButton()


    def gotoClassFolder(self, folder):
        folder = folder.split('-')[0]
        print(folder)
        items = self.images_listWidget.selectedItems()
        imageLabel = QtWidgets.QLabel()
        imageLabel.setText(folder)
        classiPath = picSavePath + '\\' + folder + '\\'
        if not os.path.exists(classiPath):
            os.makedirs(classiPath)
        for item in items:
            print(item.toolTip())
            fileName = classiPath + item.toolTip().split('\\')[-1]
            shutil.move(item.toolTip(), fileName)
            row = self.images_listWidget.row(item)
            self.images_listWidget.takeItem(row)

        # self.classImagePath.setText(dir + ' count:' + str(self.images_listWidget.count()))


    def addClass(self, folder):
        # children = self.classFrame.findChildren(QtWidgets.QPushButton)
        # count = 1
        # for child in children:
        #     if child.objectName() == 'labelPushButton':
        #         print(child.text())
        #         count += 1

        if folder:
            self.labelsFrame = QtWidgets.QFrame(self.classFrame)
            self.labelsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.labelsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.labelsFrame.setObjectName("labelsFrame")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.labelsFrame)
            self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.labelPushButton = QtWidgets.QPushButton(self.labelsFrame)
            self.labelPushButton.setObjectName("labelPushButton")
            self.labelPushButton.setText(folder)
            self.labelPushButton.clicked.connect(lambda: self.gotoClassFolder(folder))
            self.horizontalLayout_3.addWidget(self.labelPushButton)
            self.closePushButton = QtWidgets.QPushButton(self.labelsFrame)
            self.closePushButton.setMaximumSize(QtCore.QSize(50, 16777215))
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("resources/close-circled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.closePushButton.setIcon(icon4)
            self.closePushButton.setObjectName("closePushButton")
            frame = self.labelsFrame
            self.closePushButton.clicked.connect(lambda : self.closeLabel(frame))
            self.horizontalLayout_3.addWidget(self.closePushButton)
            self.horizontalLayout_4.addWidget(self.labelsFrame)

        elif folder == '':
            pass
        else:
            text, ok = QInputDialog.getText(self, '分类名称',
                                            '输入分类名称')
            if ok:
                self.labelsFrame = QtWidgets.QFrame(self.classFrame)
                self.labelsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.labelsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.labelsFrame.setObjectName("labelsFrame")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.labelsFrame)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.labelPushButton = QtWidgets.QPushButton(self.labelsFrame)
                self.labelPushButton.setObjectName("labelPushButton")
                self.labelPushButton.setText(text)
                self.labelPushButton.clicked.connect(lambda: self.gotoClassFolder(text))
                self.horizontalLayout_3.addWidget(self.labelPushButton)
                self.closePushButton = QtWidgets.QPushButton(self.labelsFrame)
                self.closePushButton.setMaximumSize(QtCore.QSize(50, 16777215))
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("resources/close-circled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.closePushButton.setIcon(icon4)
                self.closePushButton.setObjectName("closePushButton")
                frame = self.labelsFrame
                self.closePushButton.clicked.connect(lambda: self.closeLabel(frame))
                self.horizontalLayout_3.addWidget(self.closePushButton)
                self.horizontalLayout_4.addWidget(self.labelsFrame)

        self.updatelabelPushButton()


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

    file = open('resources/style.qss', 'r')
    styleSheet = file.read()
    app.setStyleSheet(styleSheet)

    mainWindow = main()
    mainWindow.setWindowIcon(QIcon('resources/logo.ico'))
    # mainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # mainWindow.setWindowOpacity(0.925)
    mainWindow.show()

    sys.exit(app.exec_())