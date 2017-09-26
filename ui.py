# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1373, 793)
        MainWindow.setAcceptDrops(True)
        MainWindow.setStyleSheet("*{\n"
"    font: 20px bold black;\n"
"    font-family: Microsoft Yahei;\n"
"}\n"
"QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 60px;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(2, 136, 209);\n"
"    height: 60px;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    background-color: rgba(0,0,0,10%);\n"
"    height: 60px;\n"
"    border: none;\n"
"}\n"
"QPushButton:checked{\n"
"    color: white;\n"
"    background-color: rgb(2, 136, 209);\n"
"    height: 60px;\n"
"    border: none;\n"
"}\n"
"QFrame{\n"
"    background-color: rgb(247, 250, 253);\n"
"}\n"
"QMainWindow{\n"
"    background-color: white;\n"
"}\n"
"QTabWidget{\n"
"    height: 20px;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    height: 30px;\n"
"    border-style:none;\n"
"    border-radius:5px;\n"
"    border:1px solid gray;\n"
"\n"
"}\n"
"QPlainTextEdit:focus\n"
"{\n"
"    border:1px solid rgb(2, 136, 209);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab { font-size:18px; background: rgb(247, 250, 253); color: black; padding:7px; text-align:center; min-width: 50px; border: 1px solid rgba(0, 0, 0, 0.0975);}\n"
"QTabBar::tab:selected { background: rgb(2, 136, 209); color: white; }\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    width:10px;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:9px;\n"
"    padding-bottom:9px;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,25%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,50%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/3.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/1.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
"{\n"
"    background:rgba(0,0,0,10%);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height:10px;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-left:9px;\n"
"    padding-right:9px;\n"
"}\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    height:8px;\n"
"    background:rgba(0,0,0,25%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"    height:8px;\n"
"    background:rgba(0,0,0,50%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/3.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/1.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:horizontal\n"
"{\n"
"    background:rgba(0,0,0,10%);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 10, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.spiderButton = QtWidgets.QPushButton(self.centralwidget)
        self.spiderButton.setEnabled(True)
        self.spiderButton.setMinimumSize(QtCore.QSize(130, 0))
        self.spiderButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.spiderButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/spiderOn.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("resources/spider.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spiderButton.setIcon(icon)
        self.spiderButton.setIconSize(QtCore.QSize(40, 40))
        self.spiderButton.setCheckable(True)
        self.spiderButton.setChecked(False)
        self.spiderButton.setAutoExclusive(True)
        self.spiderButton.setObjectName("spiderButton")
        self.verticalLayout.addWidget(self.spiderButton)
        self.classButton = QtWidgets.QPushButton(self.centralwidget)
        self.classButton.setMinimumSize(QtCore.QSize(130, 0))
        self.classButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/classiOn.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("resources/classi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.classButton.setIcon(icon1)
        self.classButton.setIconSize(QtCore.QSize(37, 37))
        self.classButton.setCheckable(True)
        self.classButton.setChecked(True)
        self.classButton.setAutoRepeat(False)
        self.classButton.setAutoExclusive(True)
        self.classButton.setObjectName("classButton")
        self.verticalLayout.addWidget(self.classButton)
        self.markButton = QtWidgets.QPushButton(self.centralwidget)
        self.markButton.setEnabled(True)
        self.markButton.setMouseTracking(False)
        self.markButton.setAcceptDrops(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/markerOn.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("resources/marker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.markButton.setIcon(icon2)
        self.markButton.setIconSize(QtCore.QSize(40, 40))
        self.markButton.setCheckable(True)
        self.markButton.setChecked(False)
        self.markButton.setAutoExclusive(True)
        self.markButton.setObjectName("markButton")
        self.verticalLayout.addWidget(self.markButton)
        self.settingButton = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/settingsOn.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("resources/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingButton.setIcon(icon3)
        self.settingButton.setIconSize(QtCore.QSize(35, 35))
        self.settingButton.setCheckable(True)
        self.settingButton.setAutoExclusive(True)
        self.settingButton.setObjectName("settingButton")
        self.verticalLayout.addWidget(self.settingButton)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(5, 10)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Spider = QtWidgets.QWidget()
        self.page_Spider.setObjectName("page_Spider")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_Spider)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outputText = QtWidgets.QPlainTextEdit(self.page_Spider)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputText.sizePolicy().hasHeightForWidth())
        self.outputText.setSizePolicy(sizePolicy)
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName("outputText")
        self.gridLayout_2.addWidget(self.outputText, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.page_Spider)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Google = QtWidgets.QWidget()
        self.tab_Google.setObjectName("tab_Google")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_Google)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Google = QtWidgets.QLabel(self.tab_Google)
        self.label_Google.setObjectName("label_Google")
        self.verticalLayout_2.addWidget(self.label_Google)
        self.plainTextEdit_Google = QtWidgets.QPlainTextEdit(self.tab_Google)
        self.plainTextEdit_Google.setObjectName("plainTextEdit_Google")
        self.verticalLayout_2.addWidget(self.plainTextEdit_Google)
        self.pushButton_Google = QtWidgets.QPushButton(self.tab_Google)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Google.sizePolicy().hasHeightForWidth())
        self.pushButton_Google.setSizePolicy(sizePolicy)
        self.pushButton_Google.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_Google.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_Google.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_Google.setObjectName("pushButton_Google")
        self.verticalLayout_2.addWidget(self.pushButton_Google)
        self.tabWidget.addTab(self.tab_Google, "")
        self.tab_Weibo = QtWidgets.QWidget()
        self.tab_Weibo.setObjectName("tab_Weibo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_Weibo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Weibo = QtWidgets.QLabel(self.tab_Weibo)
        self.label_Weibo.setObjectName("label_Weibo")
        self.verticalLayout_3.addWidget(self.label_Weibo)
        self.plainTextEdit_Weibo = QtWidgets.QPlainTextEdit(self.tab_Weibo)
        self.plainTextEdit_Weibo.setObjectName("plainTextEdit_Weibo")
        self.verticalLayout_3.addWidget(self.plainTextEdit_Weibo)
        self.pushButton_Weibo = QtWidgets.QPushButton(self.tab_Weibo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Weibo.sizePolicy().hasHeightForWidth())
        self.pushButton_Weibo.setSizePolicy(sizePolicy)
        self.pushButton_Weibo.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_Weibo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_Weibo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_Weibo.setObjectName("pushButton_Weibo")
        self.verticalLayout_3.addWidget(self.pushButton_Weibo)
        self.tabWidget.addTab(self.tab_Weibo, "")
        self.tab_Tumblr = QtWidgets.QWidget()
        self.tab_Tumblr.setObjectName("tab_Tumblr")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_Tumblr)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_Tumblr = QtWidgets.QLabel(self.tab_Tumblr)
        self.label_Tumblr.setObjectName("label_Tumblr")
        self.verticalLayout_4.addWidget(self.label_Tumblr)
        self.frame_3 = QtWidgets.QFrame(self.tab_Tumblr)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.videoFlagCheckBox = QtWidgets.QCheckBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFlagCheckBox.sizePolicy().hasHeightForWidth())
        self.videoFlagCheckBox.setSizePolicy(sizePolicy)
        self.videoFlagCheckBox.setObjectName("videoFlagCheckBox")
        self.horizontalLayout.addWidget(self.videoFlagCheckBox)
        self.picFlagCheckBox = QtWidgets.QCheckBox(self.frame_3)
        self.picFlagCheckBox.setChecked(True)
        self.picFlagCheckBox.setObjectName("picFlagCheckBox")
        self.horizontalLayout.addWidget(self.picFlagCheckBox)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.plainTextEdit_Tumblr = QtWidgets.QPlainTextEdit(self.tab_Tumblr)
        self.plainTextEdit_Tumblr.setObjectName("plainTextEdit_Tumblr")
        self.verticalLayout_4.addWidget(self.plainTextEdit_Tumblr)
        self.pushButton_Tumblr = QtWidgets.QPushButton(self.tab_Tumblr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Tumblr.sizePolicy().hasHeightForWidth())
        self.pushButton_Tumblr.setSizePolicy(sizePolicy)
        self.pushButton_Tumblr.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_Tumblr.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_Tumblr.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_Tumblr.setObjectName("pushButton_Tumblr")
        self.verticalLayout_4.addWidget(self.pushButton_Tumblr)
        self.tabWidget.addTab(self.tab_Tumblr, "")
        self.tab_Mztu = QtWidgets.QWidget()
        self.tab_Mztu.setObjectName("tab_Mztu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_Mztu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_Mztu = QtWidgets.QTableWidget(self.tab_Mztu)
        self.tableWidget_Mztu.setMaximumSize(QtCore.QSize(16777215, 16777214))
        self.tableWidget_Mztu.setObjectName("tableWidget_Mztu")
        self.tableWidget_Mztu.setColumnCount(1)
        self.tableWidget_Mztu.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Mztu.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Mztu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Mztu.setItem(0, 0, item)
        self.tableWidget_Mztu.horizontalHeader().setDefaultSectionSize(900)
        self.tableWidget_Mztu.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_Mztu.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.tableWidget_Mztu)
        self.getData_pushButton = QtWidgets.QPushButton(self.tab_Mztu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getData_pushButton.sizePolicy().hasHeightForWidth())
        self.getData_pushButton.setSizePolicy(sizePolicy)
        self.getData_pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.getData_pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.getData_pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.getData_pushButton.setObjectName("getData_pushButton")
        self.verticalLayout_5.addWidget(self.getData_pushButton)
        self.tabWidget.addTab(self.tab_Mztu, "")
        self.tab_Porn = QtWidgets.QWidget()
        self.tab_Porn.setObjectName("tab_Porn")
        self.pushButton_Porn = QtWidgets.QPushButton(self.tab_Porn)
        self.pushButton_Porn.setGeometry(QtCore.QRect(180, 190, 93, 28))
        self.pushButton_Porn.setObjectName("pushButton_Porn")
        self.tabWidget.addTab(self.tab_Porn, "")
        self.tab_Pornpics = QtWidgets.QWidget()
        self.tab_Pornpics.setObjectName("tab_Pornpics")
        self.pushButton_Pornpics = QtWidgets.QPushButton(self.tab_Pornpics)
        self.pushButton_Pornpics.setGeometry(QtCore.QRect(180, 190, 93, 28))
        self.pushButton_Pornpics.setObjectName("pushButton_Pornpics")
        self.tabWidget.addTab(self.tab_Pornpics, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 1)
        self.stackedWidget.addWidget(self.page_Spider)
        self.page_Classi = QtWidgets.QWidget()
        self.page_Classi.setObjectName("page_Classi")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_Classi)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.images_listWidget = QtWidgets.QListWidget(self.page_Classi)
        self.images_listWidget.setMinimumSize(QtCore.QSize(1204, 0))
        self.images_listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.images_listWidget.setObjectName("images_listWidget")
        self.gridLayout_3.addWidget(self.images_listWidget, 2, 0, 1, 1)
        self.ClassiFrame = QtWidgets.QFrame(self.page_Classi)
        self.ClassiFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.ClassiFrame.setMaximumSize(QtCore.QSize(16777215, 125))
        self.ClassiFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ClassiFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ClassiFrame.setObjectName("ClassiFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ClassiFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.ClassiFrame)
        self.frame_5.setMaximumSize(QtCore.QSize(10000, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addClass_pushButton = QtWidgets.QPushButton(self.frame_5)
        self.addClass_pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.addClass_pushButton.setObjectName("addClass_pushButton")
        self.horizontalLayout_5.addWidget(self.addClass_pushButton)
        self.addFolder_pushButton = QtWidgets.QPushButton(self.frame_5)
        self.addFolder_pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.addFolder_pushButton.setObjectName("addFolder_pushButton")
        self.horizontalLayout_5.addWidget(self.addFolder_pushButton)
        self.classImagePath = QtWidgets.QLabel(self.frame_5)
        self.classImagePath.setObjectName("classImagePath")
        self.horizontalLayout_5.addWidget(self.classImagePath)
        self.big_pushButton = QtWidgets.QPushButton(self.frame_5)
        self.big_pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.big_pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/bigger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.big_pushButton.setIcon(icon4)
        self.big_pushButton.setIconSize(QtCore.QSize(27, 27))
        self.big_pushButton.setObjectName("big_pushButton")
        self.horizontalLayout_5.addWidget(self.big_pushButton)
        self.small_pushButton = QtWidgets.QPushButton(self.frame_5)
        self.small_pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.small_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.small_pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/smaller.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.small_pushButton.setIcon(icon5)
        self.small_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.small_pushButton.setObjectName("small_pushButton")
        self.horizontalLayout_5.addWidget(self.small_pushButton)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.classFrame = QtWidgets.QFrame(self.ClassiFrame)
        self.classFrame.setMinimumSize(QtCore.QSize(0, 60))
        self.classFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.classFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.classFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.classFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.classFrame.setObjectName("classFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.classFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7.addWidget(self.classFrame)
        self.gridLayout_3.addWidget(self.ClassiFrame, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_Classi)
        self.page_mark = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_mark.sizePolicy().hasHeightForWidth())
        self.page_mark.setSizePolicy(sizePolicy)
        self.page_mark.setObjectName("page_mark")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_mark)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileList_widget = QtWidgets.QWidget(self.page_mark)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileList_widget.sizePolicy().hasHeightForWidth())
        self.fileList_widget.setSizePolicy(sizePolicy)
        self.fileList_widget.setMinimumSize(QtCore.QSize(200, 0))
        self.fileList_widget.setMaximumSize(QtCore.QSize(310, 16777215))
        self.fileList_widget.setObjectName("fileList_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fileList_widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fileList_label = QtWidgets.QLabel(self.fileList_widget)
        self.fileList_label.setObjectName("fileList_label")
        self.verticalLayout_6.addWidget(self.fileList_label)
        self.fileList_listWidget = QtWidgets.QListWidget(self.fileList_widget)
        self.fileList_listWidget.setAlternatingRowColors(True)
        self.fileList_listWidget.setObjectName("fileList_listWidget")
        self.verticalLayout_6.addWidget(self.fileList_listWidget)
        self.imageSelect_pushButton = QtWidgets.QPushButton(self.fileList_widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imageSelect_pushButton.setIcon(icon6)
        self.imageSelect_pushButton.setIconSize(QtCore.QSize(30, 20))
        self.imageSelect_pushButton.setObjectName("imageSelect_pushButton")
        self.verticalLayout_6.addWidget(self.imageSelect_pushButton)
        self.imagesSelect_pushButton = QtWidgets.QPushButton(self.fileList_widget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imagesSelect_pushButton.setIcon(icon7)
        self.imagesSelect_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.imagesSelect_pushButton.setObjectName("imagesSelect_pushButton")
        self.verticalLayout_6.addWidget(self.imagesSelect_pushButton)
        self.nextPic_pushButton = QtWidgets.QPushButton(self.fileList_widget)
        self.nextPic_pushButton.setIconSize(QtCore.QSize(10, 10))
        self.nextPic_pushButton.setObjectName("nextPic_pushButton")
        self.verticalLayout_6.addWidget(self.nextPic_pushButton)
        self.prePic_pushButton = QtWidgets.QPushButton(self.fileList_widget)
        self.prePic_pushButton.setObjectName("prePic_pushButton")
        self.verticalLayout_6.addWidget(self.prePic_pushButton)
        self.label = QtWidgets.QLabel(self.fileList_widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.fileList_widget)
        self.canvas = QtWidgets.QWidget(self.page_mark)
        self.canvas.setObjectName("canvas")
        self.horizontalLayout_2.addWidget(self.canvas)
        self.stackedWidget.addWidget(self.page_mark)
        self.page_Settings = QtWidgets.QWidget()
        self.page_Settings.setEnabled(True)
        self.page_Settings.setObjectName("page_Settings")
        self.label_PicSavePath = QtWidgets.QLabel(self.page_Settings)
        self.label_PicSavePath.setGeometry(QtCore.QRect(50, 80, 121, 21))
        self.label_PicSavePath.setObjectName("label_PicSavePath")
        self.plainTextEdit_path = QtWidgets.QPlainTextEdit(self.page_Settings)
        self.plainTextEdit_path.setGeometry(QtCore.QRect(210, 74, 411, 30))
        self.plainTextEdit_path.setAcceptDrops(True)
        self.plainTextEdit_path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_path.setOverwriteMode(True)
        self.plainTextEdit_path.setObjectName("plainTextEdit_path")
        self.pushButton_PathSelect = QtWidgets.QPushButton(self.page_Settings)
        self.pushButton_PathSelect.setGeometry(QtCore.QRect(660, 70, 51, 41))
        self.pushButton_PathSelect.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/openfiles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_PathSelect.setIcon(icon8)
        self.pushButton_PathSelect.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_PathSelect.setObjectName("pushButton_PathSelect")
        self.label_Proxy = QtWidgets.QLabel(self.page_Settings)
        self.label_Proxy.setGeometry(QtCore.QRect(50, 150, 121, 21))
        self.label_Proxy.setObjectName("label_Proxy")
        self.plainTextEdit_IP = QtWidgets.QPlainTextEdit(self.page_Settings)
        self.plainTextEdit_IP.setGeometry(QtCore.QRect(250, 140, 261, 30))
        self.plainTextEdit_IP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_IP.setObjectName("plainTextEdit_IP")
        self.label_IP = QtWidgets.QLabel(self.page_Settings)
        self.label_IP.setGeometry(QtCore.QRect(210, 150, 21, 16))
        self.label_IP.setObjectName("label_IP")
        self.label_Port = QtWidgets.QLabel(self.page_Settings)
        self.label_Port.setGeometry(QtCore.QRect(540, 150, 41, 21))
        self.label_Port.setObjectName("label_Port")
        self.plainTextEdit_Port = QtWidgets.QPlainTextEdit(self.page_Settings)
        self.plainTextEdit_Port.setGeometry(QtCore.QRect(600, 140, 121, 30))
        self.plainTextEdit_Port.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_Port.setObjectName("plainTextEdit_Port")
        self.stackedWidget.addWidget(self.page_Settings)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spiderk"))
        self.spiderButton.setText(_translate("MainWindow", "爬虫"))
        self.classButton.setText(_translate("MainWindow", "分类"))
        self.markButton.setText(_translate("MainWindow", "标注"))
        self.settingButton.setText(_translate("MainWindow", "设置"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_Google.setText(_translate("MainWindow", "请输入关键字，多个关键字请回车换行"))
        self.pushButton_Google.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Google), _translate("MainWindow", "谷歌"))
        self.label_Weibo.setText(_translate("MainWindow", "请输入关键字，多个关键字请回车换行"))
        self.pushButton_Weibo.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Weibo), _translate("MainWindow", "微博"))
        self.label_Tumblr.setText(_translate("MainWindow", "tumblr搜索太弱，请自行搜索并输入用户名"))
        self.videoFlagCheckBox.setText(_translate("MainWindow", "视频"))
        self.picFlagCheckBox.setText(_translate("MainWindow", "图片"))
        self.pushButton_Tumblr.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Tumblr), _translate("MainWindow", "Tumblr"))
        item = self.tableWidget_Mztu.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_Mztu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mzitu"))
        __sortingEnabled = self.tableWidget_Mztu.isSortingEnabled()
        self.tableWidget_Mztu.setSortingEnabled(False)
        item = self.tableWidget_Mztu.item(0, 0)
        item.setText(_translate("MainWindow", "点击‘提取’预览要下载的图片集"))
        self.tableWidget_Mztu.setSortingEnabled(__sortingEnabled)
        self.getData_pushButton.setText(_translate("MainWindow", "提取数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Mztu), _translate("MainWindow", "妹子图"))
        self.pushButton_Porn.setText(_translate("MainWindow", "查看分类"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Porn), _translate("MainWindow", "porn"))
        self.pushButton_Pornpics.setText(_translate("MainWindow", "查看分类"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Pornpics), _translate("MainWindow", "pornpics"))
        self.addClass_pushButton.setText(_translate("MainWindow", "添加分类"))
        self.addFolder_pushButton.setText(_translate("MainWindow", "添加文件夹"))
        self.classImagePath.setText(_translate("MainWindow", "图片文件夹"))
        self.fileList_label.setText(_translate("MainWindow", "文件列表"))
        self.imageSelect_pushButton.setText(_translate("MainWindow", "选择文件"))
        self.imagesSelect_pushButton.setText(_translate("MainWindow", "选择文件夹"))
        self.nextPic_pushButton.setText(_translate("MainWindow", "下一张(W)"))
        self.nextPic_pushButton.setShortcut(_translate("MainWindow", "Q"))
        self.prePic_pushButton.setText(_translate("MainWindow", "上一张(Q)"))
        self.prePic_pushButton.setShortcut(_translate("MainWindow", "W"))
        self.label.setText(_translate("MainWindow", "标注信息将自动保存"))
        self.label_PicSavePath.setText(_translate("MainWindow", "图片保存路径"))
        self.plainTextEdit_path.setPlainText(_translate("MainWindow", "D:\\QtSpiderPics"))
        self.label_Proxy.setText(_translate("MainWindow", "网络代理"))
        self.plainTextEdit_IP.setPlainText(_translate("MainWindow", "127.0.0.1\n"
""))
        self.label_IP.setText(_translate("MainWindow", "IP"))
        self.label_Port.setText(_translate("MainWindow", "端口"))
        self.plainTextEdit_Port.setPlainText(_translate("MainWindow", "1080\n"
""))

