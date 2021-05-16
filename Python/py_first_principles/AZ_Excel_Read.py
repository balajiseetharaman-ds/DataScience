import pandas as pd
import os as os
from AZ_Module import test_mod
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
        df=self.df.copy()  # copying a dataframe and retaining the original df undisturbed
        df['ServiceLine']=df['Service'].str.split('-').str[0]
        df['ServiceArea']=df['Service'].str.split('-').str[1]
        df.drop(['Service'],axis=1,inplace=True)
        df['Cert_year'] = pd.DatetimeIndex(df['Cert_Date']).year
        df=df[['Vendor','ServiceLine','ServiceArea','Geography','CIC_Geo','Certification Name','Cert_Date','Cert_year','Expiry Date','Active','Target']]
        df=df[(df.Vendor!= "Error")]  ## Filter specific row
        df=df.dropna()  # Dropping Na row
        df.shape
        df.info()
        #Renaming set of columns
        df.rename(columns={'Certification Name':'Certification_Name','Expiry Date':'Expiry_Date'},inplace=True)
        print(df.columns)

## Object Creation
a=file_handle('TEMPLATE.xlsx',"/Users/Balaji/Sandbox/Portfolio/DataScience/Python/py_first_principles/")
a.file_check()
a.file_read()
a.data_stats()
#k=test_mod('end')  # calling a method in another python file
