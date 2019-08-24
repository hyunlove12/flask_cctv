import pandas as apd
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
