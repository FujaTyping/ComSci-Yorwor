import pandas as pd

url = "https://github.com/comsciyorwor5/comsci/raw/master/sciScore.csv"
url2 = "https://github.com/comsciyorwor5/comsci/raw/master/studentData2.csv"
Data = pd.read_csv(url)
Data2 = pd.read_csv(url2)

print('\n[Note] : Read CsvData Url')
print(Data)
print('\n[Note] : Read CsvData Url1')
print(Data2)

NewData = Data.merge(Data2)
print('\n[Note] : Merge CsvData')
print(NewData)