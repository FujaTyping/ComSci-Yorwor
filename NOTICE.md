# Code review จำก่อนสอบ

1. รวมข้อมูล (ใช้ข้อมูล 2 ฐานข้อมูลขึ้นไป)
```
Url = ""
Url2 = ""

Data = pd.read_csv(Url)
Data2 = pd.read_csv(Url2)

MergeData = Data.merge(Data2)
print(MergeData) << แสดงข้อมูลที่รวมแล้ว
```

2. แสดงข้อมูลตามที่ต้องการ
```
print(MergeData[['','','']]) << ตรง '' ให้ใส่ HEADER
```
> print(MergeData[['Class','Name','BloodType']])

3. การจัดเรียงข้อมูลตาม HEADER
- ascending (จากมากไปน้อย - น้อยไปมาก)
- ascending | true (น้อยไปมาก) , false (มากไปน้อย)
```
NewData = RawData.sort_values(by=[''],ascending=False) << ตรง '' ให้ใส่ HEADER
```
> NewData = RawData.sort_values(by=['Height'],ascending=False)

4. จัดกลุ่ม โดย HEADER
- .<HEADER> แยกตาม HEADER
- .<HEADER>.mean/.max หาค่ามากสุด / ค่าน้อยสุด
```
print(NewData.groupby('')) << ตรง '' ให้ใส่ HEADER
print(NewData.groupby('').<HEADER>.mean/.max())
```
> print(NewData.groupby('BloodType').Weight.mean())
  
5. ดูจำนวนข้อมูลทั้งหมด
```
print(MergeData.count())
```
  
6. แสดงข้อมูลตามเงื่อนไข
```
print(NewData[NewData.Weight<เงื่อนไข>])
```
> print(NewData[NewData.Weight>=60])
