
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
import requests
#마커 찍으면서, 약국이름, 주소, 갱신시간, 입고시간, remain_stat
#type 1 : 약국, 2 : 우체국, 3 : 농협


#공릉역 :37.625782432083724,127.07302589022808

#위, 경도 기준
#https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat=34&lng=125&m=5000


#https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6

class DataCollector :
    def __init__(self,parent=None):
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

    # def get_confirmed_by_country(self) :
    #     url = "https://www.arcgis.com/apps/opsdashboard/index.html"
    #     res = requests.get(url)
    #     # soup = BeautifulSoup(res, "html.parser")
    #     # list = soup.select("div")
    #     return res.text


    #return
    #key : 80이상, 70~79 ....
    #value : [확진자(%), 사망자(%), 치명률(%)]
    def get_confirmed_by_age(self) :
        url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
        res = req.urlopen(url).read()
        soup = BeautifulSoup(res, "html.parser")
        list_title = soup.select("#content > div > div:nth-child(19) > table > tbody > tr > th:nth-child(1)")
        list_confirmed = soup.select("#content > div > div:nth-child(19) > table > tbody > tr > td:nth-child(2)")
        list_dead = soup.select("#content > div > div:nth-child(19) > table > tbody > tr > td:nth-child(3)")
        list_cri = soup.select("#content > div > div:nth-child(19) > table > tbody > tr > td:nth-child(4)")
        result = {}
        for i in range(len(list_title)) :
            cf = ''.join(list(map(lambda x : x if x.isnumeric() or x in ('(',')','-','.') else '',list(list_confirmed[i].text.strip()))))
            dd = ''.join(list(map(lambda x : x if x.isnumeric() or x in ('(',')','-','.') else '',list(list_dead[i].text.strip()))))
            cr = ''.join(list(map(lambda x : x if x.isnumeric() or x in ('(',')','-','.') else '',list(list_cri[i].text.strip()))))
            result[list_title[i].text.strip()] = [cf,dd,cr]
        return result


    #return
    #key : 남자, 여자
    #value : [확진자(%), 사망자(%), 치명률(%)]
    def get_confirmed_by_sex(self) :
        url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
        res = req.urlopen(url).read()
        soup = BeautifulSoup(res, "html.parser")
        list_sex = soup.select("#content > div > div:nth-child(16) > table > tbody > tr > th")
        list_confirmed = soup.select("#content > div > div:nth-child(16) > table > tbody > tr > td:nth-child(2)")
        list_dead = soup.select("#content > div > div:nth-child(16) > table > tbody > tr > td:nth-child(3)")
        list_cri = soup.select("#content > div > div:nth-child(16) > table > tbody > tr > td:nth-child(4)")
        result = {}
        for i in range(len(list_sex)) :
            cf = ''.join(list(map(lambda x : x if x.isnumeric() or x in ('(',')','-','.') else '',list(list_confirmed[i].text.strip()))))
            dd = ''.join(list(map(lambda x : x if x.isnumeric() or x in ('(',')','-','.') else '',list(list_dead[i].text.strip()))))
            cr = ''.join(list(map(lambda x : x if x.isnumeric() or x in ('(',')','-','.') else '',list(list_cri[i].text.strip()))))
            result[list_sex[i].text.strip()] = [cf,dd,cr]
        return result

    def html_test(self) :
        url = "https://terms.naver.com/entry.nhn?docId=5912275&cid=43667&categoryId=43667#TABLE_OF_CONTENT5"
        res = req.urlopen(url).read()
        soup = BeautifulSoup(res, "html.parser")
        img = soup.select("div.se_component.se_image.default > div > div > div > a >img")
        return img

    def get_data_by_location(self) :
        pass






#"https://search.naver.com/search.naver?&where=news&query=%EB%A7%88%EC%8A%A4%ED%81%AC&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=4&docid=&nso=so:r,p:1d,a:all&mynews=1&cluster_rank=116&refresh_start=0&start=1"


if __name__ == "__main__" :
    dc = DataCollector()
    rs = dc.get_rank_data()
    for i in rs :
        print(i, rs[i])
        print()
