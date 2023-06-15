import pandas as pd

url = "https://raw.githubusercontent.com/comsciyorwor5/comsci/master/studentData-noHeader.csv"

print("\n[Note] : Read CsvData NO HEADDER")
#ตั้งชื่อ HEADDER ด้วย names=['','','']
RawData = pd.read_csv(url,names=['เลขประจำตัว','เพศ','Cs','height'])
#ไม่ใช้ url
#RawData = pd.read_csv(<Url>)
print(RawData)