# -*- coding: utf-8 -*-
"""Lab 2  การเชื่อมโยงและแสดงข้อมูล.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wLoEnwMUlU_8kDIFLDS8J1olLLcjfEm7

# Install all package
Run all cell press : `Ctrl+F9` or `Runtime > Run all`
"""

import pandas as pd

"""# Section 2.1 แสดงข้อมูลทั้งหมดของการรวมข้อมูล"""

Url = "https://github.com/comsciyorwor5/comsci/raw/master/Data1.csv"
Url2 = "https://github.com/comsciyorwor5/comsci/raw/master/Data2.csv"

Data = pd.read_csv(Url)
Data2 = pd.read_csv(Url2)

MergeData = Data.merge(Data2)
print(MergeData)

"""# Section 2.2 แสดงข้อมูล ชื่อชั้นเรียน ชื่อนักเรียน และหมู่เลือด"""

print(MergeData[['Class','Name','BloodType']])

"""# Section 2.3 แสดงข้อมูล ชื่อชั้นเรียน ชื่อนักเรียน ความสูง และเลขประจําตัว โดยเรียงลําดับตามความสูง จากมากไปน้อย"""

RawData = MergeData[['Class','Name','Height','ID']]
NewData = RawData.sort_values(by=['Height'],ascending=False)

print(NewData)

"""# Section 2.4 แสดงข้อมูล ชื่อชั้นเรียน เลขที่ ชื่อนักเรียน และ น้ําหนัก เรียงตามชื่อชั้นเรียน จาก น้อยไปมาก"""

RawData = MergeData[['Class','Number','Name','Weight']]
NewData = RawData.sort_values(by=['Class'],ascending=True)

print(NewData)

"""# Section 2.5 แสดงค่าน้ําหนักเฉลี่ยแยกตามหมู่เลือด"""

WeightData = MergeData[['Weight','BloodType']]
NewData = WeightData.sort_values(by=['Weight'],ascending=True)

print(NewData.groupby('BloodType').Weight.mean())

"""# Section 2.6 แสดงจํานวนข้อมูลทั้งหมด"""

print(MergeData.count())

"""# Section 2.7 แสดงค่าความสูงของคนที่สูงที่สุดในแต่ละ ชั้นเรียน"""

HeightData = MergeData[['Height','Class']]
NewData = HeightData.sort_values(by=['Height'],ascending=False)

print(NewData.groupby('Class').Height.max())

"""# Section 2.8 แสดงชื่อนักเรียนและน้ําหนักนักเรียนที่มีน้ําหนักตั้งแต่ 60 กิโลกรัมขึ้นไป"""

NameData = MergeData[['Name','Weight']]
NewData = NameData.sort_values(by=['Weight'],ascending=True)

print(NewData[NewData.Weight>=60])

"""#>> Original : 18_10_สิรภพ สุขชู (52647@hatyaiwit.ac.th) <<


"""