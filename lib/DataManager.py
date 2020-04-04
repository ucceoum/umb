from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from matplotlib import font_manager, rc
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class DataManager :
    def __init__(self, parent=None) :
        self.main = parent

    def intro_graph(self, data):
        # data=[]
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
        plt.savefig("data/200330_pie_chart.svg")
        #위젯그래프에 그래프 표시하기
        canvas=FigureCanvas(fig)
        canvas.draw()
        lay=QHBoxLayout(self.main.widget_graph)


        lay.addWidget(canvas)
        canvas.show()

    def show_intro_list(self, data):


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
