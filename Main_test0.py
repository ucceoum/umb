import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, Qt
from ui.main_test0 import Ui_MainWindow
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from lib.ScriptRunner import Runner
from lib.DataCollector import DataCollector
from lib.DataManager import DataManager
from lib.item import Item
import requests
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib import font_manager, rc
from PyQt5 import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import uuid


from bb import *

#https://doc.qt.io/qtforpython/PySide2/QtGui/QMouseEvent.html
#https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qtcore-module.html
class Umbrella(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()


        self.init_my_location()
        self.setupUi(self)  # 초기화
        # self.url = "http://192.168.0.3:8080/umbrella"
        self.url = "http://localhost:8080/umbrella.html"
        self.webEngineView.load(QUrl(self.url))
        self.page = QWebEnginePage()
        self.page.setUrl(QUrl(self.url))
        self.page.setView(self.webEngineView)
        # self.webEngineView2.load(QUrl("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="))

        self.appLoaded = False
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--mute-audio")
        self.browser = webdriver.Chrome(chrome_options=chrome_option, executable_path="resources/chromedriver.exe")
        self.browser.get(self.url)
        self.user_uuid = uuid.uuid4()
        self.runner = Runner(self)
        self.dc = DataCollector(self)
        self.dm = DataManager(self)
        self.itemList = []
        self.rowList = []
        self.dataChecker = 0

        # self.webEngineView2.load(QUrl(self.dc.html_test()))

        self.initSignal()

        self.tboard = Board(self.page_3)
        self.tboard.msg2Statusbar.connect(self.test_1)
        self.tboard.start()
        self.setStyleSheet("background-color:#ffffff")
        self.tboard.setGeometry(460,0,460,820)


    def test_1(self, msg) :
        if msg == "Game over" :
            self.tboard.initBoard()
            self.tboard.start()


    def initSignal(self) :
        #page 변환
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.intro_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton__image.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton__image2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton.clicked.connect(self.runner.map_removeMarkers)
        #intro 데이터 입력
        self.lineEdit.returnPressed.connect(lambda: self.runner.search(self.lineEdit.text().strip()))
        self.pushButton.clicked.connect(lambda: self.runner.search(self.lineEdit.text().strip()))
        self.page.loadFinished.connect(lambda: self.runner.setMap(self.my_location_lat, self.my_location_lng))
        self.pushButton2.clicked.connect(self.mark_around)
        self.pushButton3.clicked.connect(lambda: self.runner.setMap(self.my_location_lat,self.my_location_lng))
        self.page.urlChanged.connect(self.setButton)
        self.listWidget.itemActivated.connect(self.activateRow)
        self.listWidget.itemClicked.connect(self.rowClicked)
        self.lineEdit.setText(self.runner.coord_to_address(self.my_location_lat,self.my_location_lng, 0))

        self.radio1.clicked.connect(lambda : self.setDataChecker(0))
        self.radio2.clicked.connect(lambda : self.setDataChecker(2))
        self.radio3.clicked.connect(lambda : self.setDataChecker(3))
        self.radio4.clicked.connect(lambda : self.setDataChecker(4))

        self.widget_1.pressed.connect(self.view_graph)
        self.widget_2.pressed.connect(self.view_graph)
        self.widget_3.pressed.connect(self.view_graph)
        self.widget_4.pressed.connect(self.view_graph)




    def view_graph(self) :
        self.stackedWidget.setCurrentIndex(2)


    def mark_around(self) :
        print("markaround")
        self.remove_list()
        if not self.page.url().toString().strip().startswith(self.url) :
            self.page.load(QUrl(self.url))
            return
        self.runner.map_removeMarkers()
        try :
            lat, lng = self.runner.map_getCenter()
        except :
            print("mark_arount exception")
            return
        data = self.dc.get_data_by_latlng(lat, lng, 1000)
        self.runner.marking(data)
        self.show_list(data)
        self.lineEdit.setText(self.runner.coord_to_address(lat, lng, 0))

    def setDataChecker(self, num) :
        self.dataChecker = num

    #표지
    def intro(self):
        data = self.dc.A()
        #Text
        self.dm.show_intro_list(data)
        #그래프
        self.dm.intro_graph(data)

    def init_my_location(self) :
        url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDQKxbTt0MrFNH85kTJXzickMD5s88UVaI'
        data = {
            'considerIp': True,
        }
        result = requests.post(url, data)
        my_location = json.loads(result.text)
        self.my_location_lat = str(my_location.get('location').get('lat'))
        self.my_location_lng = str(my_location.get('location').get('lng'))

    def setButton(self) :
        if self.page.url().toString().strip().startswith("http://localhost:8080/umbrella") :
            self.pushButton2.setText("판매처 탐색")
        else :
            self.pushButton2.setText("지도 새로고침")

    def show_list(self, data) :
        remainP = ['100개 이상', '30개 이상 100개 미만', '2개 이상 30개 미만','1개 이하', '판매중지']
        for i in range(len(data)) :
            item = QListWidgetItem(self.listWidget)
            row = Item(data[i])
            rs = data[i].get('remain_stat')
            if rs == None :
                row.remain_stat.setStyleSheet('color:red')
            elif remainP.index(rs) <= 1 :
                row.remain_stat.setStyleSheet('color:green')
            elif remainP.index(rs) == 2 :
                row.remain_stat.setStyleSheet('color:orange')
            else :
                row.remain_stat.setStyleSheet('color:red')
            item.setWhatsThis(str(i))
            item.setSizeHint(row.sizeHint())
            self.listWidget.setItemWidget(item, row)
            self.listWidget.addItem(item)
            self.itemList.append(item)
            self.rowList.append(row)

    def remove_list(self) :
        for i in range(len(self.itemList)) :
            self.itemList[i].setHidden(True)
        self.itemList = []
        self.rowList = []

    def activateRow(self, row) :
        self.runner.setMap(self.rowList[int(row.whatsThis())].lat,self.rowList[int(row.whatsThis())].lng)
        self.runner.info_open(self.rowList[int(row.whatsThis())].code)

    def rowClicked(self, row) :
        self.runner.info_close_all()
        self.runner.info_open(self.rowList[int(row.whatsThis())].code)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Umbrella()
    window.intro()
    window.show()

    app.exec_()
    window.browser.close()
    window.browser.quit()

    pass
