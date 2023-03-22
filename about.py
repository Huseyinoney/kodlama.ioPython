#python veri tipleri

PYTHON’DA VERİ TİPLERİ
Python programlama dilinde; Numeric (Sayısal), Sequence (Sıralı), Boolean (Mantıksal),  Dictionary (Sözlük) ve Binary (İkili) olmak üzere 6 ana veri tipi bulunmaktadır. 
-Numeric veri tipi integer (tam ), floar (ondalıklı) ve Complex (karmaşık) sayılardan oluşur. 
-Sequence veri tipi ise string (metin), list(liste) ve tuple(demet) yapılarında oluşur.
-Boolean veri tipinde sadece bir yapı bulunur. Bu yapıda mantık kurarken true yada false yapılarını tutar.


mailBase = ""
passwordBase= ""

mail = input("Lütfen mail adresinizi giriniz: ")
password = input("Lütfen şifrenizi giriniz: ")

if mail == (mailBase) and password == (passwordBase):
    print("Giriş yapıldı.")
else:
    print("Mail veya şifre yanlış.")




courses = []

course = input("katılmak istediğiniz kursun ismini giriniz")
if course:
     courses.append(course)
else:
     print("geçerli bir kurs ismi girmediniz")
