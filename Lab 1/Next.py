def menu() :
  print("\n----- MENU -----\n1 = ReadCsvDataline\n2 = ReadCsvDatacolum\n3 = ReadCsvDataFunction\n4 = Merge\nAll = Run AllFile")
  Choose = str(input("\nSelect Number : "))
  if Choose == "1" :
    exec(open("Lab (Next)/GETdataGithubLINE.py").read())
  elif Choose == "2" :
    exec(open("Lab (Next)/GETdataGithubColum.py").read())
  elif Choose == "3" :
    exec(open("Lab (Next)/GETdataGithubFunction.py").read())
  elif Choose == "4" :
    exec(open("Lab (Next)/Mergedata.py").read())
  elif Choose == "All" :
    exec(open("Lab (Next)/GETdataGithubLINE.py").read())
    exec(open("Lab (Next)/GETdataGithubColum.py").read())
    exec(open("Lab (Next)/GETdataGithubFunction.py").read())
    exec(open("Lab (Next)/Mergedata.py").read())
  else :
    print("Please choose number in menu only !")
  print("\n[Author] : 18_10_สิรภพ สุขชู")

menu()