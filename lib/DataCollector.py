
import json
import sys
import io
import urllib.request as req
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from bs4 import BeautifulSoup
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
import matplotlib.pyplot as plt
#마커 찍으면서, 약국이름, 주소, 갱신시간, 입고시간, remain_stat
#type 1 : 약국, 2 : 우체국, 3 : 농협


#공릉역 :37.625782432083724,127.07302589022808

#위, 경도 기준
#https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat=34&lng=125&m=5000

class DataCollector :
    def __init__(self,parent):
            self.main=parent



#체크박스


    def get_data_by_latlng(self, lat, lng, ds) :
        remainP = {'plenty' : '100개 이상', 'some' : '30개 이상 100개 미만', 'few' : '2개 이상 30개 미만', 'empty' : '1개 이하', 'break' : '판매중지'}
        checkP = ['','break','empty','few','some','plenty']

        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat="+str(lat)+"&lng="+str(lng)+"&m="+str(ds)+""
        result = json.loads(req.urlopen(url).read()).get("stores")


        for i in range(len(result)-1, -1, -1) :
            if self.main.dataChecker > 0 :
                if not result[i].get('remain_stat') in checkP or checkP.index(result[i].get('remain_stat')) <= self.main.dataChecker :
                    print("데이터 제외, remain_stat :",result[i].get('remain_stat'))
                    result.pop(i)
                    continue
            if result[i].get('remain_stat') in remainP :
                result[i]['remain_stat'] = remainP[result[i]['remain_stat']]




        return result


    # 숫자만 가져오는것
    def numI(self,text) :
        textL=list(text)
        result = ''
        for i in range(len(textL)):
             if textL[i].isnumeric() :
                 result += textL[i]
        return int(result)

    def A(self):
        list_data=[]
        url = "http://ncov.mohw.go.kr/"

        res = req.urlopen(url).read()

        soup = BeautifulSoup(res, "html.parser")
        a = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.num ").text)
        b = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(1) > span.before").text
        c = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.num").text)
        d = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text
        e = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.num").text)
        f = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(3) > span.before").text
        g = self.numI(soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.num").text)
        h = soup.select_one("div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text
        for i in (a,b,c,d,e,f,g,h):
            list_data.append(i)

        return list_data
        # print("완치자 : ",c,d)
        # print("치료중 : ",e,f)
        # print("사망자 : ",g,h)

    def intro_graph(self):
        # data=[]
        data=self.A()
        a=data[0]
        c=data[2]
        e=data[4]
        g=data[6]

        font_name = font_manager.FontProperties(fname="c:/Windows/fonts/YTTE08.TTF").get_name()
        rc('font', family=font_name)
        labels = ('확진환자', '완치자', '치료중', '사망자') ## 라벨
        xs = [a,c,e,g] ## 값들, pie 차트에서 알아서 100% 기준으로 변경해서 정리해줌

        ## 그림
        fig=plt.figure(figsize=(60, 6))

        ## plt.pie로 생기는 요소를 다음처럼 리턴하여 값을 저장
        patches, texts, autotexts = plt.pie(
            labels=labels, ## label
            x = xs, ## 값
            startangle=90,## 어디에서 시작할지, 정해줌
            shadow=False, ##그림자
            counterclock=False, ## 시계방향으로 가는지, 시계 반대 방향으로 가는지 정해줌
            autopct='%1.1f%%', ## pi 위에 표시될 글자 형태, 또한 알아서 %로 변환해서 알려줌
            pctdistance=0.7, ## pct가 radius 기준으로 어디쯤에 위치할지 정함
            colors=['red', 'blue', 'green','grey'],
        )
        ## add circle
        ## 도넛처럼 만들기 위해서 아래처럼
        centre_circle = plt.Circle((0,0),0.40,color='white')
        plt.gca().add_artist(centre_circle)
        #######
        ## label만 변경해주기
        for t in texts:
            t.set_color("black")
            t.set_fontsize(15)
        ## pie 위의 텍스트를 다른 색으로 변경해주기
        for t in autotexts:
            t.set_color("white")
            t.set_fontsize(10)
        plt.tight_layout()
        plt.savefig("D:/umbrella/200330_pie_chart.svg")
        #위젯그래프에 그래프 표시하기
        canvas=FigureCanvas(fig)
        canvas.draw()
        lay=QHBoxLayout(self.main.widget_graph)


        lay.addWidget(canvas)
        canvas.show()

    def show_intro_list(self):
        data=self.A()
        print("show_intro_list")
        _translate = QtCore.QCoreApplication.translate

        self.main.patient = QtWidgets.QLabel(self.main.widget_1)
        self.main.patient.setStyleSheet('color:white; font-size:20px')
        self.main.patient.setGeometry(QtCore.QRect(0,0,210,125))
        self.main.patient.setText(_translate("MainWindow",
        "<html><head/><body><p align=\"center\">확진환자<br/> "+
        "<span style='font-size:50px'>"
        +str(data[0])+"</span><br/>"+
        "<span style='font-size:15px'>"+str(data[1])+
        "</span></p></body></html>"))

        # self.patient.setGeometry(QtCore.QRect())
        self.main.perfect = QtWidgets.QLabel(self.main.widget_2)
        self.main.perfect.setStyleSheet('color:white; font-size:20px')
        self.main.perfect.setGeometry(QtCore.QRect(0,0,210,125))
        self.main.perfect.setText(_translate("MainWindow",
        "<html><head/><body><p align=\"center\">완치자<br/> "+
        "<span style='font-size:50px'>"
        +str(data[2])+"</span><br/>"+
        "<span style='font-size:15px'>"+str(data[3])+
        "</span></p></body></html>"))

        # self.widget_3.setText(str(data[4])+" "+str(data[5]))
        self.main.care = QtWidgets.QLabel(self.main.widget_3)
        self.main.care.setStyleSheet('color:white; font-size:20px')
        self.main.care.setGeometry(QtCore.QRect(0,0,210,125))
        self.main.care.setText(_translate("MainWindow",
        "<html><head/><body><p align=\"center\">치료중<br/> "+
        "<span style='font-size:50px'>"
        +str(data[4])+"</span><br/>"+
        "<span style='font-size:15px'>"+str(data[5])+
        "</span></p></body></html>"))
        # self.widget_4.setText(str(data[6])+" "+str(data[7]))
        self.main.dead = QtWidgets.QLabel(self.main.widget_4)
        self.main.dead.setStyleSheet('color:white; font-size:20px')
        self.main.dead.setGeometry(QtCore.QRect(0,0,210,125))
        self.main.dead.setText(_translate("MainWindow",
        "<html><head/><body><p align=\"center\">사망<br/> "+
        "<span style='font-size:50px'>"
        +str(data[6])+"</span><br/>"+
        "<span style='font-size:15px'>"+str(data[7])+
        "</span></p></body></html>"))
