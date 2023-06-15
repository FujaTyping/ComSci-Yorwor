#ใช้ Replit ถนัดกว่าใช้ Colab
#ใช้ Replit ถนัดกว่าใช้ Colab
#ใช้ Replit ถนัดกว่าใช้ Colab

print("[Python] : Importing module")
#อย่าลืม Import Module ก่อน เดี่ยวใช้ไม่ได้นะ !!!
import pandas as pd
print("[Python] : All module imported\n")

def menu() :
  print("\n----- MENU -----\n1 = Serise\n2 = DataFrame\n3 = GET Csv_data\n4 = GET Csv_data2\nAll = Run AllFile\n")
  Choose = str(input("Select Number : "))
  if Choose == "1" :
    exec(open("Lab/Serise.py").read())
  elif Choose == "2" :
    exec(open("Lab/DataFrame.py").read())
  elif Choose == "3" :
    exec(open("Lab/GETdataGithub.py").read())
  elif Choose == "4" :
    exec(open("Lab/GETdataGithub 2.py").read())
  elif Choose == "All" :
    exec(open("Lab/Serise.py").read())
    exec(open("Lab/DataFrame.py").read())
    exec(open("Lab/GETdataGithub.py").read())
    exec(open("Lab/GETdataGithub 2.py").read())
  else :
    print("Please choose number in menu only !")
  
  print("\n[Author] : 18_10_สิรภพ สุขชู")

print("----- MENU -----\n1 = ของสัปดาห์แรก\n2 = ของสัปดาห์นี้")
choose = int(input("\nSelect number : "))

if choose == 1 :
  menu()
elif choose == 2 :
  exec(open("Next.py").read())
else :
  print("Please choose number in menu only !")