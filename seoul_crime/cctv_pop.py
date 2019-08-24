import pandas as pd
import numpy as np
"""
Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
--------------------------
Index(['자치구', '계', '계.1', '계.2', '65세이상고령자'], dtype='object')
"""

from seoul_crime.data_reader import DataReader

class CCTVModel:
    def __init__(self):
        self.dr = DataReader()

    def hook_process(self):
        print("-------1.cctv 파일 df 생성--------")
        self.get_cctv()

    def get_cctv(self):
        self.dr.context = "./data/"

        #setter의 메소드명과 일치해야 한다.
        #@fname.setter
        #def fname(self, fname):
        self.dr.fname = 'cctv_in_seoul.csv'
        cctv = self.dr.csv_dframe()
        #print(cctv)
        #print(cctv.columns)
        self.dr.fname = "population_in_seoul.xls"
        pop = self.dr.xls_to_dframe(2, "B,D,G,J,N")
        #print(pop)
        #print(pop.header())
        #print(pop.columns)
        cctv.rename(columns={cctv.columns[0]:"구 별"}, inplace=True)
        pop.rename(columns={
            pop.columns[0]:"구 별",
            pop.columns[1]:"인구수",
            pop.columns[2]:"한국인",
            pop.columns[3]:"외국인",
            pop.columns[4]:"고령인"

        }, inplace=True)
        #pop.drop([0], True)
        print(pop["구 별"].isnull())
        pop.drop([26], inplace=True)
        pop["외국인비율"] = pop["외국인"] / pop["인구수"] * 100
        pop["고령자비율"] = pop["고령인"] / pop["인구수"] * 100
        #pop.drop([26], inplace=True)

        cctv.drop(["2013년도 이전", "2014년", "2015년", "2016년"], 1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on="구 별")
        #상관관계를 찾는것
        #가설을 세운 후 증명하는 과정
        cor1 = np.corrcoef(cctv_pop["고령자비율"], cctv_pop["소계"])
        cor2 = np.corrcoef(cctv_pop["외국인비율"], cctv_pop["소계"])

        #가공된 데이터 다시 저장
        cctv_pop.to_csv("./saved_data/cctv_pop.csv")
        #print("고령자 비율과 CCTV의 상관계수는 {} \n"
        #      "외국인 비율과 CCTV의 상관계수는 {}".format(cor1, cor2))


