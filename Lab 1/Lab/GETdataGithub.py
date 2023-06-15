import pandas as pd

url = "https://raw.githubusercontent.com/comsciyorwor5/comsci/master/studentData.csv"

print("\n[Note] : Read CsvData")
RawData = pd.read_csv(url)
#ไม่ใช้ url
#RawData = pd.read_csv(<Url>)
print(RawData)