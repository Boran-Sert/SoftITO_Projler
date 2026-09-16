# ------------1------------------
print("python öğreniyorum")
isim, soyisim = "boran","sert"
print(isim,soyisim)
print(5)
print("python öğreniyorum")

# ------------2-------------------
print("selam") # Ekrana selam yazdırır
"""Boran Sert 22 İstanbul"""

#--------------3-------------------
sehir = "İstanbul"
print(sehir)
puan = 50
print(puan)
puan = 75
print(puan)

# -------------4------------------
sayı = 10
ondalık = 10.0
yazı = "selam"
evet_mi = True

print(type(sayı))
print(type(ondalık))
print(type(yazı))
print(type(evet_mi))

# -------------5-------------------
toplam = 15+4
çıkarma = 15-4
çarpma = 15*4
bölme = 15/4
kalan = 17%5
üst = 2^8

print(toplam)
print(çıkarma)
print(çarpma)
print(bölme)
print(kalan)
print(üst)

# ---------------6--------------------
isim = input("İsim gir")
print(f"Merhaba {isim}")

yas = int(input("yas"))
print(f"10 yıl sonra {yas +10 } yaşındasınız")

# ---------------7---------------------
a = 8
b = 12

print(a<b)
print(a>b)
print(a==b)

sayı = input("Bir sayı giriniz")
if int(sayı) == 100: print("Sayı 100'dür")

# ---------------8---------------------
yas = 22
ogrenci_mi = False

print(yas > 18 and ogrenci_mi)
print(yas > 18 or ogrenci_mi)
print(not ogrenci_mi)

kayitli_mi = True
print(yas > 18 and kayitli_mi)

# ---------------9---------------------
sayi = int(input("Bir sayı giriniz: "))
if sayi >= 0:
    print("Sayı pozitif")
else:
    print("Sayı negatif")

not_degeri = int(input("Notunuzu giriniz: "))
if not_degeri >= 50:
    print("Geçti")
else:
    print("Kaldı")

# ---------------10--------------------
ad = "Boran"
soyad = "Sert"
tam_ad = ad + " " + soyad
print(tam_ad)

kelime = "python"
print(len(kelime))

mesaj = "Merhaba Dünya"
print(mesaj.upper())
print(mesaj.lower())

# ---------------11--------------------
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
carpim = sayi1 * sayi2
print(f"Çarpım: {carpim}")

kare_sayi = int(input("Karesi alınacak sayıyı giriniz: "))
kare = kare_sayi * kare_sayi
print(f"Sayının karesi: {kare}")

# ------------------------------- 2. KISIM ----------------------------------------------


# ---------------12--------------------
# Değişkenlerle Basit Hesaplamalar
birim_fiyat = 45.5
adet = 3
toplam_tutar = birim_fiyat * adet
print(f"Toplam Tutar: {toplam_tutar} TL")

maas = 8000
maas += 1500
print(f"Yeni Maaş: {maas} TL")

# ---------------13--------------------
# İç İçe (Nested) if-else
yas = int(input("Yaşınızı giriniz: "))
ogrenci_cevap = input("Öğrenci misiniz? (e/h): ")

if yas > 65:
    print("Ücretsiz")
else:
    if ogrenci_cevap == "e":
        print("İndirimli")
    else:
        print("Tam ücret")

sayi = int(input("Bir sayı giriniz: "))
if sayi > 0:
    if sayi % 2 == 0:
        print("Sayı hem pozitif hem de çifttir.")
    else:
        print("Sayı pozitif ama tek.")
else:
    print("Sayı pozitif değil.")

# ---------------14--------------------
# elif ile Çoklu Koşullar
sicaklik = float(input("Sıcaklık değerini giriniz: "))
if sicaklik > 30:
    print("Sıcak")
elif sicaklik >= 15:
    print("Ilıman")
else:
    print("Soğuk")

ay = int(input("Ay numarasını giriniz (1-12): "))
if ay in [12, 1, 2]:
    print("Kış")
elif ay in [3, 4, 5]:
    print("İlkbahar")
elif ay in [6, 7, 8]:
    print("Yaz")
elif ay in [9, 10, 11]:
    print("Sonbahar")
else:
    print("Geçersiz ay numarası")

# ---------------15--------------------
# for Döngüsü ile Liste Üzerinde İşlem
sayilar = [5, 15, 8, 22, 3, 19]

en_buyuk = sayilar[0]
for s in sayilar:
    if s > en_buyuk:
        en_buyuk = s
print(f"En büyük sayı: {en_buyuk}")

on_ustu_sayac = 0
for s in sayilar:
    if s > 10:
        on_ustu_sayac += 1
print(f"10'dan büyük sayı adedi: {on_ustu_sayac}")

# ---------------16--------------------
# while Döngüsü ile Basit Sayaç
sayac = 10
while sayac >= 1:
    print(sayac)
    sayac -= 1

dogru_sifre = "1234"
girilen_sifre = ""
while girilen_sifre != dogru_sifre:
    girilen_sifre = input("Şifreyi giriniz: ")
print("Giriş başarılı!")

# ---------------17--------------------
# Döngü İçinde Koşul Kullanma
for i in range(1, 21):
    if i % 3 == 0:
        print(f"3'e bölünen: {i}")

karisik_sayilar = [-5, 12, 0, -8, 25, -1, 7]
print("Pozitif sayılar:")
for s in karisik_sayilar:
    if s > 0:
        print(s)

print("Negatif sayılar:")
for s in karisik_sayilar:
    if s < 0:
        print(s)

# ---------------18--------------------
# Basit Fonksiyon Tanımlama
def kup_al(x):
    return x ** 3

print(kup_al(3))

def topla(x, y):
    return x + y

print(topla(10, 20))

# ---------------19--------------------
# Fonksiyon + Koşul Birlikte
def sayi_durumu(n):
    if n > 0:
        return "Pozitif"
    elif n < 0:
        return "Negatif"
    else:
        return "Sıfır"

print(sayi_durumu(-7))

def en_buyuk_uc(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(en_buyuk_uc(15, 42, 28))

# ---------------20--------------------
# Liste Oluşturma ve İşleme
sehirler = []
for i in range(5):
    sehir = input(f"{i + 1}. şehri giriniz: ")
    sehirler.append(sehir)

for sira, sehir in enumerate(sehirler):
    print(f"{sira}. {sehir}")

urunler = ["elma", "ekmek", "süt", "peynir"]
print(f"Başlangıç ürünleri: {urunler}")
silinecek = input("Silmek istediğiniz ürünü yazınız: ")
if silinecek in urunler:
    urunler.remove(silinecek)
    print(f"Güncel liste: {urunler}")
else:
    print("Ürün listede bulunamadı.")

# ---------------21--------------------
# Kullanıcıdan Birden Fazla Veri Alma
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
dogum_yili = int(input("Doğum yılınız: "))
yas = 2026 - dogum_yili
print(f"Merhaba {ad} {soyad}, yaşınız: {yas}")

boy_cm = float(input("Boyunuzu cm olarak giriniz: "))
kilo = float(input("Kilonuzu kg olarak giriniz: "))
boy_m = boy_cm / 100
bmi = kilo / (boy_m ** 2)
print(f"Vücut Kitle İndeksiniz: {bmi:.2f}")

# ---------------22--------------------
# Küçük Bir Uygulama — Not Ortalaması Hesaplama
notlar = []
for i in range(4):
    not_degeri = float(input(f"{i + 1}. dersin notunu giriniz: "))
    notlar.append(not_degeri)

ortalama = sum(notlar) / len(notlar)
print(f"Ortalama: {ortalama:.2f}")

if ortalama >= 90:
    harf = "AA"
elif ortalama >= 85:
    harf = "BA"
elif ortalama >= 80:
    harf = "BB"
elif ortalama >= 70:
    harf = "CB"
elif ortalama >= 60:
    harf = "CC"
elif ortalama >= 50:
    harf = "DC"
else:
    harf = "FF"

print(f"Harf Notu: {harf}")

en_yuksek = notlar[0]
en_dusuk = notlar[0]
for n in notlar:
    if n > en_yuksek:
        en_yuksek = n
    if n < en_dusuk:
        en_dusuk = n

print(f"En Yüksek Not: {en_yuksek}")
print(f"En Düşük Not: {en_dusuk}")

# ---------------23--------------------
# Küçük Bir Uygulama — Basit Sepet/Alışveriş
sepet_fiyatlari = [45, 120, 80, 250, 95, 150]

yuz_tl_ustu = []
for fiyat in sepet_fiyatlari:
    if fiyat > 100:
        yuz_tl_ustu.append(fiyat)
print(f"100 TL üzeri ürünler: {yuz_tl_ustu}")

toplam_tutar = sum(sepet_fiyatlari)
print(f"Sepet Toplamı: {toplam_tutar} TL")

if toplam_tutar > 500:
    odenecek_tutar = toplam_tutar * 0.90
    print("%10 indirim kazandınız!")
    print(f"İndirimli Ödenecek Tutar: {odenecek_tutar} TL")
else:
    print(f"Ödenecek Tutar: {toplam_tutar} TL")
