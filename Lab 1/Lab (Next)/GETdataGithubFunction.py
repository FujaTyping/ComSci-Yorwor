import pandas as pd

url = "https://raw.githubusercontent.com/comsciyorwor5/comsci/master/studentData-noHeader.csv"

#ตั้งชื่อ HEADDER ด้วย names=['','','']
RawData = pd.read_csv(url,names=['เลขประจำตัว','เพศ','Cs','height'])

print('\n[Note] : Read CsvData Function Count')
#นับจำนวนข้อมูล
print(RawData.count())

print('\n[Note] : Read CsvData Function Mean')
#หาค่าเฉลี่ย
print(RawData.Cs.mean())

print('\n[Note] : Read CsvData Function Max')
#แสดงจำนวนค่ามากที่สุด
print(RawData.Cs.max())

print('\n[Note] : Read CsvData Function Min')
#แสดงจำนวนค่าน้อยที่สุด
print(RawData.Cs.min())

print('\n[Note] : Read CsvData Function Group')
#จัดกลุ่ม แล้วหา ค่าเฉลี่ย
print(RawData.groupby('เพศ').Cs.mean())

print('\n[Note] : Read CsvData Function Group and Sort')
#จัดกลุ่ม แล้วเรียงจากมากไปหาน้อย
print(RawData.sort_values(by=['height'],ascending=False))