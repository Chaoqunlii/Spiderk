import sys, random
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QPainter, QPixmap, QImage, QPen
from PyQt5.QtCore import Qt
import json

class Canvas(QWidget):
    def __init__(self, p, imageDir):
        super().__init__(parent=p)
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 0
        self.top = 10
        self.imageDir = imageDir
        self.image = QImage()
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.setAutoFillBackground(True)
        self.point_press = None
        self.point_painted_1 = None
        self.point_painted_4 = None
        self.rectPressed = False
        self.pointPressed_1 = False
        self.pointPressed_4 = False
        self.pixmapWidth = 0
        self.pixmapHeight = 0
        self.initUI()

    def changePic(self):
        self.point_press = None
        self.point_painted_1 = None
        self.point_painted_4 = None
        self.rectPressed = False
        self.pointPressed_1 = False
        self.pointPressed_4 = False
        self.showImage()
        # self.pixmapWidth = self.pixmap.width()
        # self.pixmapHeight = self.pixmap.Height()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.image.load(self.imageDir)
        self.pixmap = QPixmap.fromImage(self.image)
        self.setGeometry(self.left, self.top, self.pixmap.width(), self.pixmap.height())
        # Create widget

        self.vbox = QVBoxLayout()

        self.scroll = QScrollArea()

        self.setLayout(self.vbox)
        self.showImage()

        self.scroll.setWidget(self.label)

        self.scroll.setAutoFillBackground(True)
        self.scroll.setWidgetResizable(True)
        self.vbox.addWidget(self.scroll)

        self.qp = QPainter(self)
        self.qp.setCompositionMode(QPainter.CompositionMode_Source)
        self.qp.setRenderHint(QPainter.Antialiasing)
        self.qp.setRenderHint(QPainter.HighQualityAntialiasing)
        self.qp.setRenderHint(QPainter.SmoothPixmapTransform)


    def loadPoints(self):
        pointFile = self.imageDir.split('.')[0] + '.json'
        try:

            with open(pointFile, 'r') as f:
                content = f.read()
            # print(content)
            points = json.loads(content)
            self.point_painted_1 = points['Point_1'][0], points['Point_1'][1]
            self.point_painted_4 = points['Point_4'][0], points['Point_4'][1]
            # print(self.point_painted_1)
            # print(self.point_painted_4)
            self.qp.begin(self.image)
            self.qp.setPen(QPen(Qt.green, 2))
            self.qp.drawLine(self.point_painted_1[0], self.point_painted_1[1], self.point_painted_4[0], self.point_painted_1[1])
            self.qp.drawLine(self.point_painted_1[0], self.point_painted_1[1], self.point_painted_1[0], self.point_painted_4[1])
            self.qp.drawLine(self.point_painted_4[0], self.point_painted_1[1], self.point_painted_4[0], self.point_painted_4[1])
            self.qp.drawLine(self.point_painted_1[0], self.point_painted_4[1], self.point_painted_4[0], self.point_painted_4[1])
            self.qp.drawLine(self.point_painted_1[0], self.point_painted_1[1], self.point_painted_4[0], self.point_painted_4[1])
            self.qp.setPen(QPen(Qt.blue, 20))
            self.qp.drawPoint(self.point_painted_1[0], self.point_painted_1[1])
            self.qp.drawPoint(self.point_painted_4[0], self.point_painted_4[1])
            self.qp.end()
            self.label.setPixmap(QPixmap.fromImage(self.image))
        except:
            print('没有point数据')


    def showImage(self):
        self.image.load(self.imageDir)
        pixmap = QPixmap.fromImage(self.image)
        # if pixmap.width() > self.width():
        #     pixmap = pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    # def wheelEvent(self, ev):
    #     self.image.load(self.imageDir)
    #     pixmap = QPixmap.fromImage(self.image)
    #     self.pixmapWidth -= 1
    #     self.pixmapHeight -= 1
    #     pixmap = pixmap.scaled(self.pixmapWidth, self.pixmapHeight, Qt.KeepAspectRatio)
    #     self.label.setPixmap(pixmap)

    def mousePressEvent(self, ev):
        self.point_press = ev.x(), ev.y()
        if self.point_painted_1 \
                and self.point_press[0] < self.point_painted_1[0] + 15 \
                and self.point_press[0] > self.point_painted_1[0] - 15 \
                and self.point_press[1] < self.point_painted_1[1] + 15 \
                and self.point_press[1] > self.point_painted_1[1] - 15:
            self.pointPressed_1 = True


        elif self.point_painted_4 \
                and self.point_press[0] < self.point_painted_4[0] + 15 \
                and self.point_press[0] > self.point_painted_4[0] - 15 \
                and self.point_press[1] < self.point_painted_4[1] + 15 \
                and self.point_press[1] > self.point_painted_4[1] - 15:
            self.pointPressed_4 = True

        elif (self.point_painted_1 and self.point_painted_4 \
                and self.point_press[0]<self.point_painted_4[0]\
                and self.point_press[0]>self.point_painted_1[0]\
                and self.point_press[1]<self.point_painted_4[1]\
                and self.point_press[1]>self.point_painted_1[1])\
            or (self.point_painted_1 and self.point_painted_4\
                and self.point_press[0] > self.point_painted_4[0]\
                and self.point_press[0] < self.point_painted_1[0]\
                and self.point_press[1] > self.point_painted_1[1]\
                and self.point_press[1] < self.point_painted_4[1])\
            or (self.point_painted_1 and self.point_painted_4\
                and self.point_press[0] > self.point_painted_1[0]\
                and self.point_press[0] < self.point_painted_4[0]\
                and self.point_press[1] > self.point_painted_4[1]\
                and self.point_press[1] < self.point_painted_1[1])\
            or (self.point_painted_1 and self.point_painted_4\
                and self.point_press[0] > self.point_painted_4[0]\
                and self.point_press[0] < self.point_painted_1[0]\
                and self.point_press[1] > self.point_painted_4[1]\
                and self.point_press[1] < self.point_painted_1[1]):
            self.rectPressed = True
        else:
            self.showImage()
    def mouseReleaseEvent(self, ev):
        self.rectPressed = False
        self.pointPressed_1 = False
        self.pointPressed_4 = False


    def mouseMoveEvent(self, ev):
        self.showImage()
        if self.pointPressed_1:
            self.point_painted_1 = ev.x(), ev.y()
        elif self.pointPressed_4:
            self.point_painted_4 = ev.x(), ev.y()
        elif self.rectPressed:
            deltaX = ev.x() - self.point_press[0]
            deltaY = ev.y() - self.point_press[1]
            self.point_painted_1 = self.point_painted_1[0]+deltaX, self.point_painted_1[1]+deltaY

            self.point_painted_4 = self.point_painted_4[0]+deltaX, self.point_painted_4[1]+deltaY
            self.point_press = ev.x(), ev.y()

        else:
            self.point_painted_1 = self.point_press[0], self.point_press[1]
            self.point_painted_4 = ev.x(), ev.y()
            if ev.x() > self.image.width():
                self.point_painted_4 = self.image.width(), ev.y()
            if ev.y() > self.image.height():
                self.point_painted_4 = ev.x(), self.image.height()
            if ev.x() > self.image.width() and ev.y() > self.image.height():
                self.point_painted_4 = self.image.width(), self.image.height()
            if ev.x() < 0:
                self.point_painted_4 = 0, ev.y()
            if ev.y() < 0:
                self.point_painted_4 = ev.x(), 0
            if ev.x() < 0 and ev.y() < 0:
                self.point_painted_4 = 0, 0

        self.qp.begin(self.image)
        self.qp.setPen(QPen(Qt.green, 2))
        self.qp.drawLine(self.point_painted_1[0], self.point_painted_1[1], self.point_painted_4[0], self.point_painted_1[1])
        self.qp.drawLine(self.point_painted_1[0], self.point_painted_1[1], self.point_painted_1[0], self.point_painted_4[1])
        self.qp.drawLine(self.point_painted_4[0], self.point_painted_1[1], self.point_painted_4[0], self.point_painted_4[1])
        self.qp.drawLine(self.point_painted_1[0], self.point_painted_4[1], self.point_painted_4[0], self.point_painted_4[1])
        self.qp.drawLine(self.point_painted_1[0], self.point_painted_1[1], self.point_painted_4[0], self.point_painted_4[1])
        self.qp.setPen(QPen(Qt.blue, 20))
        self.qp.drawPoint(self.point_painted_1[0], self.point_painted_1[1])
        self.qp.drawPoint(self.point_painted_4[0], self.point_painted_4[1])
        self.qp.end()
        self.label.setPixmap(QPixmap.fromImage(self.image))


