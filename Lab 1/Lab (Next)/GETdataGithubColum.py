import pandas as pd

url = "https://raw.githubusercontent.com/comsciyorwor5/comsci/master/studentData-noHeader.csv"

#ตั้งชื่อ HEADDER ด้วย names=['','','']
RawData = pd.read_csv(url,names=['เลขประจำตัว','เพศ','Cs','height'])

print('\n[Note] : Read CsvData Colum')
#อ่านข้อมูล ตามชื่อคอลัมน์ เติม [['','']]
print(RawData[['เลขประจำตัว','Cs']])

print('\n[Note] : Read CsvData Single Colum By Name')
#อ่านข้อมูล ตามชื่อคอลัมน์ เติม ['']
print(RawData['Cs'])

print('\n[Note] : Read CsvData Colum and Line')
#อ่านข้อมูล ตามชื่อคอลัมน์ และจำนวนแถว เติม .head(<จำนวนแถว>)
print(RawData[['เลขประจำตัว','Cs']].head(2))

print('\n[Note] : Read CsvData Value')
#อ่านข้อมูล ตามข้อมูลในคอลัมน์ เติม .<ชื่อ HEADDER>==<ข้อมูล>
print(RawData[RawData.เพศ==2])
print('\n',RawData[RawData.Cs>=18])