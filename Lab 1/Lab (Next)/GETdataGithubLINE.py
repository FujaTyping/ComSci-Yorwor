import pandas as pd

url = "https://raw.githubusercontent.com/comsciyorwor5/comsci/master/studentData-noHeader.csv"

#ตั้งชื่อ HEADDER ด้วย names=['','','']
RawData = pd.read_csv(url,names=['เลขประจำตัว','เพศ','Cs','height'])

print('\n[Note] : Read CsvData 5 line (Top)')
#อ่านข้อมูล ตามจำนวนแถว เติม .head(<จำนวนแถว>)
#อ่านข้อมูล ตามจำนวนแถวจากด้านบน เติม .head
print(RawData.head(5))

print('\n[Note] : Read CsvData 5 line (Bottom)')
#อ่านข้อมูล ตามจำนวนแถวจากด้านล่าง เติม .tail
print(RawData.tail(5))