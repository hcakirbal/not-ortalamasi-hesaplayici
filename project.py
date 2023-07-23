ders_limit = int(input("kaç ders gireceksiniz? \n"))
katsayi_array = []
ort_array = []
toplam = 0
for n in range(0, ders_limit):
  notlar = 0
  notlar_array = []
  katsayi = 0
  ders_ismi = input("dersin ismini girin \n")
  katsayi = int(input("dersin katsayısını girin \n"))
  katsayi_array.append(katsayi)
  not_limiti = int(input("kaç not gireceksiniz? \n"))
  for i in range(0, not_limiti):
    notlar = int(input("notu girin \n"))
    notlar_array.append(notlar)
    if i == (not_limiti-1):
      ort_array.append(sum(notlar_array)/(not_limiti))
      print(ders_ismi,"ortalamanız:\n", sum(notlar_array)/(not_limiti))
  if n == (ders_limit-1):
    for m in range(0, ders_limit):
      toplam += ort_array[m] * katsayi_array[m]
    genel_ortalama = toplam / sum(katsayi_array)
    print("Genel ortalamanız: \n", genel_ortalama)