#python veri tipleri

PYTHON’DA VERİ TİPLERİ
Python programlama dilinde; Numeric (Sayısal), Sequence (Sıralı), Boolean (Mantıksal), Set(Takım), Dictionary (Sözlük) ve Binary (İkili) olmak üzere 6 ana veri tipi bulunmaktadır. 
-Numeric veri tipi integer (tam ), floar (ondalıklı) ve Complex (karmaşık) sayılardan oluşur. 
-Sequence veri tipi ise string (metin), list(liste) ve tuple(demet) yapılarında oluşur.
-Boolean veri tipinde sadece bir yapı bulunur. Bu yapıda mantık kurarken true yada false yapılarını tutar.
-Son olarak set veri tipi ise tektir. Sıralı olmayan, elemanı arttırılabilen ama ikinci kez tekrar etmeyen verileri oluşturmayı sağlar.




mailadress = ""
şifre = ""
kullanıcıadı = input("Kullanıcı Adı : ")
şifre  =  input( "Şifre : " )

if mailadress == kullanıcıadı and şifre == şifre : 
     print("Giriş Başarılı")
elif mailadress != kullanıcıadı and şifre == şifre :
     print("Kullanıcı Adı Hatalı")
elif mailadress == kullanıcıadı and şifre != şifre :
     print("Şifre Hatalı")
else :
   print("Kullanıcı Adı ve Şifre Hatalı")

KursaKayıt = mailadress == kullanıcıadı and şifre == şifre 
if KursaKayıt :
    KursaKayıt = True 
    print("Kursa Başarıyla Kayıt Oldunuz.")
else : 
    KursaKayıt = False 
    print("İçeriği Görmek İçin Kayıt Olun ve Giriş Yapın.")
       
kurslar = [" 2023 Java Yazılım Geliştirme Yetiştirme Kampı", "Pyhton&Selenium Geliştirme Yetiştirme Kampı"]
öğretmenler = ["Engin Demirog", "Halit Kalaycı"]

if mailadress == kullanıcıadı and şifre == şifre :
    KursaKayıt = True
    print (kurslar)
    print(öğretmenler)
