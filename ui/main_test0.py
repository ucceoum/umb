# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 820)
        MainWindow.setMinimumSize(QSize(920, 820))
        MainWindow.setMaximumSize(QSize(920, 820))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 920, 820))
        self.stackedWidget.setObjectName("stackedWidget")

        # #page0
        # self.page0 = QtWidgets.QWidget()
        # self.page0.setObjectName("page0")
        # self.loading = QtWidgets.QWidget(self.page0)
        # self.loading.setGeometry(QtCore.QRect(0, 0, 920, 820))
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("D:/Umbrella/dahyoung/umbrella2/logo/umbrella11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.loading.setIcon(icon)
        # self.loading.setStyleSheet("background-color : #ffffff")
        # self.loading.setObjectName("loading")
        # self.stackedWidget.addWidget(self.page0)

        #page1
        #Intro_frame
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")


        self.intro_frame = QtWidgets.QFrame(self.page)
        self.intro_frame.setGeometry(QtCore.QRect(0, 0, 920, 820))
        self.intro_frame.setStyleSheet("background-color : #000000")
        self.intro_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.intro_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.intro_frame.setObjectName("intro_frame")

        self.intro_button= QtWidgets.QPushButton(self.intro_frame)
        self.intro_button.setGeometry(QtCore.QRect(0, 0, 920, 820))
        self.intro_button.setObjectName("intro_button")

        # self.widget_main = QtWidgets.QWidget(self.intro_frame)
        # self.widget_main.setGeometry(QtCore.QRect(20, 480, 420, 250))
        # self.widget_main.setObjectName("widget_main")
        # self.widget_1 = QtWidgets.QWidget(self.widget_main)
        # self.widget_1.setGeometry(QtCore.QRect(0, 0, 210, 125))
        # self.widget_1.setStyleSheet("background-color : #ff0000")
        # self.widget_1.setObjectName("widget_1")
        # self.widget_2 = QtWidgets.QWidget(self.widget_main)
        # self.widget_2.setGeometry(QtCore.QRect(210, 0, 210, 125))
        # self.widget_2.setStyleSheet("background-color : #0000ff")
        # self.widget_2.setObjectName("widget_2")
        # self.widget_3 = QtWidgets.QWidget(self.widget_main)
        # self.widget_3.setGeometry(QtCore.QRect(0, 125, 210, 125))
        # self.widget_3.setStyleSheet("background-color : #ff8c00")
        # self.widget_3.setObjectName("widget_3")
        # self.widget_4 = QtWidgets.QWidget(self.widget_main)
        # self.widget_4.setGeometry(QtCore.QRect(210, 125, 210, 125))
        # self.widget_4.setStyleSheet("background-color : #808080")
        # self.widget_4.setObjectName("widget_4")



        self.widget_main = QtWidgets.QWidget(self.intro_frame)
        self.widget_main.setGeometry(QtCore.QRect(20, 480, 420, 250))
        self.widget_main.setObjectName("widget_main")
        self.widget_1 = QtWidgets.QPushButton(self.widget_main)
        self.widget_1.setGeometry(QtCore.QRect(0, 0, 210, 125))
        self.widget_1.setStyleSheet("background-color : #ff0000")
        self.widget_1.setObjectName("widget_1")
        self.widget_2 = QtWidgets.QPushButton(self.widget_main)
        self.widget_2.setGeometry(QtCore.QRect(210, 0, 210, 125))
        self.widget_2.setStyleSheet("background-color : #0000ff")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QPushButton(self.widget_main)
        self.widget_3.setGeometry(QtCore.QRect(0, 125, 210, 125))
        self.widget_3.setStyleSheet("background-color : #ff8c00")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QPushButton(self.widget_main)
        self.widget_4.setGeometry(QtCore.QRect(210, 125, 210, 125))
        self.widget_4.setStyleSheet("background-color : #808080")
        self.widget_4.setObjectName("widget_4")












        # self.listView_3 = QtWidgets.QListView(self.intro_frame)
        # self.listView_3.setGeometry(QtCore.QRect(20, 480, 420, 251))
        # self.listView_3.setStyleSheet("background-color : #ffffff")
        # self.listView_3.setObjectName("listView_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.intro_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 100, 301, 300))
        # self.pushButton_3.setGeometry(QtCore.QRect(170, 0, 601, 321))
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("D:/Umbrella/dahyoung/umbrella2/logo/rolling_umb.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.movie=QMovie("logo/rolling_umb.gif")
        self.movie.setScaledSize(QtCore.QSize(200,200))
        self.label_23 = QtWidgets.QLabel(self.pushButton_3)
        self.label_23.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.label_23.setMovie(self.movie)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.movie.start()
        # self.pushButton_3.setIcon(icon)
        # self.pushButton_3.setIconSize(QtCore.QSize(600, 231))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.intro_frame)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 57, 400, 200))
        icon_text = QtGui.QIcon()
        icon_text.addPixmap(QtGui.QPixmap("logo/text1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon_text)
        self.pushButton_4.setIconSize(QtCore.QSize(400, 200))
        self.pushButton_4.setObjectName("pushButton_4")
        #마스크 보유 현황
        self.pushButton_5 = QtWidgets.QPushButton(self.intro_frame)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 200, 350, 200))
        icon_text1 = QtGui.QIcon()
        icon_text1.addPixmap(QtGui.QPixmap("logo/mask2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon_text1)
        self.pushButton_5.setIconSize(QtCore.QSize(400, 200))
        self.pushButton_5.setObjectName("pushButton_5")

        self.widget_graph = QtWidgets.QWidget(self.intro_frame)
        self.widget_graph.setGeometry(QtCore.QRect(460, 480, 420, 250))
        self.widget_graph.setStyleSheet("background-color : #ffffff")
        self.widget_graph.setObjectName("listView_5")
        self.stackedWidget.addWidget(self.intro_frame)
        #page2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 921, 630))
        self.frame.setStyleSheet("background-color : #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame)
        self.webEngineView.setGeometry(QtCore.QRect(-1, 0, 921, 601))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")

        #stack1로 돌아가는 버튼
        self.pushButton__image = QtWidgets.QPushButton(self.frame)
        self.pushButton__image.setGeometry(QtCore.QRect(0, 0, 30, 30))
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("logo/umbrella.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton__image.setIcon(icon)
        # self.pushButton__image.setIconSize(QtCore.QSize(30, 30))
        # self.pushButton__image.setObjectName("pushButton__image")

        self.movie2=QMovie("logo/rolling_umb.gif")
        self.movie2.setScaledSize(QtCore.QSize(30,30))
        self.label_24 = QtWidgets.QLabel(self.pushButton__image)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.label_24.setMovie(self.movie2)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.movie2.start()





        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 600, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(281, 601, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.frame)
        self.pushButton2.setGeometry(QtCore.QRect(381, 601, 101, 31))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.frame)
        self.pushButton3.setGeometry(QtCore.QRect(481, 601, 101, 31))
        self.pushButton3.setObjectName("pushButton3")
        #1개 미만
        self.radio1 = QtWidgets.QRadioButton(self.frame)
        self.radio1.setGeometry(QtCore.QRect(600, 600, 71, 31))
        self.radio1.setObjectName("radio1")
        self.radio2 = QtWidgets.QRadioButton(self.frame)
        self.radio2.setGeometry(QtCore.QRect(670, 600, 71, 31))
        self.radio2.setObjectName("radio2")
        self.radio3 = QtWidgets.QRadioButton(self.frame)
        self.radio3.setGeometry(QtCore.QRect(750, 600, 71, 31))
        self.radio3.setObjectName("radio3")
        self.radio4 = QtWidgets.QRadioButton(self.frame)
        self.radio4.setGeometry(QtCore.QRect(830, 600, 81, 31))
        self.radio4.setObjectName("radio4")
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 630, 921, 191))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.stackedWidget.addWidget(self.page_2)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.radio1.setChecked(True)

        #graph
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")


        self.frame2 = QtWidgets.QFrame(self.page_3)
        self.frame2.setGeometry(QtCore.QRect(0, 0, 920, 820))
        self.frame2.setStyleSheet("background-color : #ffffff")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")

        self.comboBox = QtWidgets.QComboBox(self.frame2)
        self.comboBox.setGeometry(QtCore.QRect(29, 0, 201, 30))
        self.comboBox.setObjectName("comboBox")

        self.graph2 = QtWidgets.QWidget(self.frame2)
        self.graph2.setGeometry(QtCore.QRect(0, 30, 920, 790))
        self.graph2.setObjectName("graph2")
        # self.webEngineView2 = QtWebEngineWidgets.QWebEngineView(self.frame2)
        # self.webEngineView2.setGeometry(QtCore.QRect(200, 120, 720, 700))
        # self.webEngineView2.setUrl(QtCore.QUrl("about:blank"))
        # self.webEngineView2.setObjectName("webEngineView2")

        #stack1로 돌아가는 버튼
        self.pushButton__image2 = QtWidgets.QPushButton(self.frame2)
        self.pushButton__image2.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.pushButton__image2.setObjectName("pushButton__image")
        self.movie3=QMovie("logo/rolling_umb.gif")
        self.movie3.setScaledSize(QtCore.QSize(30,30))
        self.label_25 = QtWidgets.QLabel(self.pushButton__image2)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.label_25.setMovie(self.movie2)
        self.label_25.setText("")
        self.label_25.setObjectName("label_24")
        self.movie3.start()

        self.stackedWidget.addWidget(self.page_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "이동"))
        self.pushButton2.setText(_translate("MainWindow", "판매처 탐색"))
        self.pushButton3.setText(_translate("MainWindow", "내 위치"))
        self.radio1.setText(_translate("MainWindow", "전체"))
        self.radio2.setText(_translate("MainWindow", "1개 ↑"))
        self.radio3.setText(_translate("MainWindow", "30개 ↑"))
        self.radio4.setText(_translate("MainWindow", "100개 ↑"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
