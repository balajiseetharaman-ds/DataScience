import pandas as pd
import os as os
from AZ_Module import test_mod as k
class file_handle:
    def __init__(self,name,path):
        self.name=name
        self.path=path
        print("File name to be read:",self.name)
        print("File path to be read:",self.path)
## File Exists check
    def file_check(self):
        self.fpath=self.path+self.name
        if os.path.exists(self.fpath):
            print("\n **********file exists*************\n")
        else:
            print("*********File path or file doesn't exists************")
## File read
    def file_read(self):
        df=pd.read_excel(self.fpath)
        self.df=df

## Data Wrangling
    def data_stats(self):
        self.df['ServiceLine']=self.df['Service'].str.split('-').str[0]
        self.df['ServiceArea']=self.df['Service'].str.split('-').str[1]
        self.df.drop(['Service'],axis=1,inplace=True)
        self.df['Cert_year'] = pd.DatetimeIndex(self.df['Cert_Date']).year
        self.df=self.df[['Vendor','ServiceLine','ServiceArea','Geography','CIC_Geo','Certification Name','Cert_Date','Cert_year','Expiry Date','Active','Target']]
        print(self.df[self.df.Vendor=='IBM'])  ## Filter Dataframe for IBM

## Object Creation
a=file_handle('TEMPLATE.xlsx',"/Users/Balaji/Sandbox/Portfolio/DataScience/Python/py_first_principles/")
a.file_check()
a.file_read()
a.data_stats()
k=test_mod('end')  # calling a method in another python file
