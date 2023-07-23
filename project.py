ders_limit = int(input("kaç ders gireceksiniz? \n"))
for n in range(0, ders_limit):
  notlar = 0
  ders_ismi = input("dersin ismini girin \n")
  not_limit = int(input("kaç not gireceksiniz? \n"))
  for i in range(0, not_limit):
    notlar += int(input("notu girin \n"))
    if i == (not_limit-1):
      print(ders_ismi,"ortalamanız:\n",notlar/not_limit)