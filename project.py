not_limit = int(input("kaç not gireceksiniz? \n"))
notlar = 0
for i in range(0, not_limit):
  notlar += int(input("notu girin \n"))
  if i == (not_limit-1):
    print("ortalamanız:\n",notlar/not_limit)