"""
Futbol Maç Veri Seti Sütun Sözlüğü (T1_2425.csv - Süper Lig 2024/25)

Bu modül, veri setindeki Türkçe sütun adlarının açıklamalarını dokümante eder.
Veri seti 100 maç içerir ve yalnızca maç istatistiklerinden oluşur.

Sütunlar:
    Temel Bilgiler:
        Lig (str): Lig kodu.
        Tarih (str): Maçın oynandığı tarih.
        Saat (str): Maçın başlama saati.
        EvTakım (str): Ev sahibi takımın adı.
        DepTakım (str): Deplasman takımının adı.

    Skor Bilgileri:
        EvGol (int): Maç sonu ev sahibi takımın gol sayısı.
        DepGol (int): Maç sonu deplasman takımının gol sayısı.
        Sonuç (str): Maç sonucu ('H': Ev, 'D': Beraberlik, 'A': Deplasman).
        EvYarıGol (int): İlk yarı ev sahibi takımın gol sayısı.
        DepYarıGol (int): İlk yarı deplasman takımının gol sayısı.
        YarıSonuç (str): İlk yarı sonucu ('H': Ev, 'D': Beraberlik, 'A': Deplasman).

    Maç İçi İstatistikler:
        EvŞut (int): Ev sahibi takımın toplam şut sayısı.
        DepŞut (int): Deplasman takımının toplam şut sayısı.
        Evİsabet (int): Ev sahibi takımın isabetli şut sayısı.
        Depİsabet (int): Deplasman takımının isabetli şut sayısı.
        EvFaul (int): Ev sahibi takımın yaptığı faul sayısı.
        DepFaul (int): Deplasman takımının yaptığı faul sayısı.
        EvKorner (int): Ev sahibi takımın kullandığı korner sayısı.
        DepKorner (int): Deplasman takımının kullandığı korner sayısı.
        EvSarı (int): Ev sahibi takımın gördüğü sarı kart sayısı.
        DepSarı (int): Deplasman takımının gördüğü sarı kart sayısı.
        EvKırmızı (int): Ev sahibi takımın gördüğü kırmızı kart sayısı.
        DepKırmızı (int): Deplasman takımının gördüğü kırmızı kart sayısı.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.show_versions()

# --- 1 ---------- Series - Tek Boyutlu Veri Yapısı ----------

s = pd.Series([100, 200, 300, 400])
print(s)

goller = pd.Series([65, 58, 52, 44], index=["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"])
print(goller)

print(goller["Galatasaray"])

print(goller.sum())


# --- 2 ---------- DataFrame - Tablo Yapısı ----------

maclar = pd.DataFrame({
    "maç": ["GS-FB", "BJK-TS", "FB-BJK", "TS-GS", "GS-BJK"],
    "gol": [3, 2, 4, 1, 2],
    "şut": [15, 11, 18, 9, 13]
})
print(maclar)

takimlar = pd.DataFrame({
    "isim": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor"],
    "kuruluş": [1905, 1907, 1903, 1967],
    "şehir": ["İstanbul", "İstanbul", "İstanbul", "Trabzon"]
})
print(takimlar)

# Tahmin: 4 satır, 3 sütun
print(takimlar.shape)


# --- 3 ---------- CSV Dosyası Okuma ve Yazma ----------

takimlar.to_csv("takimlar.csv", index=False)

okunan = pd.read_csv("Dataset/takimlar.csv")
print(okunan)

# index=False kullanmadan kaydetme -> dosyaya fazladan index sütunu yazılır
takimlar.to_csv("takimlar_indexli.csv")
print(pd.read_csv("Dataset/takimlar_indexli.csv"))


# --- 4 ---------- Veriyi İnceleme (İlk Bakış) ----------

df = pd.read_csv("Dataset/T1_2425.csv", encoding="utf-8-sig")

print(df.head(3))
print(df.tail(2))

print(df.shape)

print(df.info())

print(df[["EvGol", "DepGol", "EvŞut"]].describe())


# --- 5 ---------- Sütun ve Satır Seçme ----------

print(df["EvTakım"])

print(df[["EvTakım", "EvGol"]])

print(df.loc[0:2])

print(df.iloc[1, 1])


# --- 6 ---------- Filtreleme (Koşullu Seçim) ----------

print(df[df["EvGol"] > 2])

print(df[(df["EvŞut"] > 10) & (df["EvŞut"] < 20)])

print(df[df["EvTakım"] == "Galatasaray"])

print(df[(df["EvKorner"] < 2) | (df["EvKorner"] > 10)])


# --- 7 ---------- Yeni Sütun Ekleme ve Güncelleme ----------

df["ToplamGol"] = df["EvGol"] + df["DepGol"]
print(df[["EvTakım", "DepTakım", "ToplamGol"]])

df["EvŞut"] = df["EvŞut"] * 1.10
print(df["EvŞut"])

df["MaçTipi"] = df["ToplamGol"].apply(lambda x: "Gollü" if x > 2 else "Az Gollü")
print(df[["EvTakım", "DepTakım", "ToplamGol", "MaçTipi"]])


# --- 8 ---------- Sıralama ----------

print(df.sort_values("ToplamGol"))

print(df.sort_values("EvŞut", ascending=False))

print(df.sort_values(["EvTakım", "EvGol"]))

# --- 9 ----------- Contact ----------
df1 = pd.DataFrame({"isim": ["Boran","Deniz"], "yas": [23,14]})
df2 = pd.DataFrame({"isim": ["Zeynep","Elif"], "yas": [20,15]})

toplam = pd.concat([df1,df2],ignore_index=True)

# --- 10 ---------- Pivot ------------
df= pd.DataFrame({
    "sehir":["İstanbul","Ankara","Erzincan","Manisa","Denizli"],
    "urun" :["forma","top","kazak","krampon","bilet"],
    "satis":[1000,1500,2000,23000,21232]
})

pivot= pd.pivot_table(df,index="sehir",columns="urun",values="satis")

# --- 11 ---------- Veri tipi değiştirme ------------
df = pd.DataFrame ({
    "id" :["1","2","3"],
    "fiyat":["19.99","25.50","30.21"]
})

df.info()

df["id"] = df["id"].astype(int)

df.info()

# --- 12 ----------- Görselleştirme ------------------
df = pd.DataFrame({"ay": ["Ocak","Şubat","Mart","Nisan"], "satis": [1200,1444,5006,1340]})

#Çizgi grafik
df.plot(x="ay", y="satis", kind="line", marker="o")
plt.title("Ay Bazlı Satış")
plt.xlabel("Ay")
plt.ylabel("Satış Miktarı")
plt.show()

#Pasta grafiği
df.set_index("ay").plot(kind="pie",y="satis",autopct="%1.1f%%")
plt.title("Ay Bazlı Satış")
plt.show()


#Bar grafik
df.plot(x="ay", y="satis", kind="bar", color="Red")
plt.title("Ay Bazlı Satış")
plt.xlabel("Ay")
plt.ylabel("Satış Miktarı")
plt.show()

# ================================================================================
# =========================== DERS İÇİ SORULAR ==================================
# ================================================================================

# --------------------------- SORU 1 (Series) ---------------------------
# 1.1
stok = pd.Series([300, 150, 80, 45], index=['Kalem', 'Defter', 'Silgi', 'Cetvel'])
print("1.1 Stok Series:")
print(stok)

# 1.2
silgi_stok = stok['Silgi']
print("\n1.2 Silgi Stoğu:", silgi_stok)

# 1.3
en_az_urun = stok.idxmin()
print("\n1.3 Stoğu En Az Ürün:", en_az_urun)

# 1.4
toplam_stok = stok.sum()
print("\n1.4 Toplam Stok:", toplam_stok)


# --------------------------- SORU 2 (DataFrame) ---------------------------
# 2.1
uyeler = pd.DataFrame({
    "uye_adi": ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali"],
    "paket_turu": ["Aylık", "Yıllık", "Aylık", "Yıllık", "Aylık"],
    "odenen_tutar": [150, 1200, 150, 1200, 150]
})

# 2.2
print("\n2.2 DataFrame Şekli:", uyeler.shape)

# 2.3
print("\n2.3 Sütun İsimleri:", uyeler.columns)


# --------------------------- SORU 3 (Dosya Okuma Hataları) ---------------------------
# 3.1
try:
    df_csv = pd.read_csv("satislar.csv")
except Exception as e:
    print("3.1 Beklenen Hata:", e)

# 3.2
try:
    df_excel = pd.read_excel("rapor.xlsx")
except Exception as e:
    print("3.2 Beklenen Hata:", e)


# --------------------------- SORU 4 (Veriyi İnceleme) ---------------------------
df = pd.DataFrame({    "siparis_no": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
                       "kargo_suresi": [2, 5, 3, np.nan, 1, 4, 6],
                       "urun_adedi": [1, 3, 2, 5, 1, 2, 4],
                       "toplam_tutar": [150.0, 480.5, 220.0, 610.0, 90.0, 310.0, 720.0]})

# 4.1
print("--- İlk 3 Sipariş ---")
print(df.head(3))
print("--------------------------- Son 2 Sipariş ---------------------------------")
print(df.tail(2))

# 4.2
print("-------------------------- Veri Bilgisi (Eksik Veri Tespiti) ---------------")
df.info()

# 4.3
print("-------------------------- İstatistiki Özet -------------------------------")
print(df.describe())


# --------------------------- SORU 5 (Sütun/Satır Seçme) ---------------------------
# 5.1
print("--- Belirli Sütunlar ---")
print(df[['siparis_no', 'toplam_tutar']])

# 5.2
print("------------------------ loc ile 0-3 Satırlar -----------------------")
print(df.loc[0:3])

# 5.3
print("------------------------- iloc ile İlk 4 Satırın Son 2 Sütunu -----------")
print(df.iloc[:4, -2:])


# --------------------------- SORU 6 (Filtreleme ve Yeni Sütun) ---------------------------
# 6.1
filtre1 = df[df['toplam_tutar'] > 300]
print("--- 6.1 Toplam Tutarı 300'den Büyük Olanlar ---")
print(filtre1)

# 6.2
filtre2 = df[(df['urun_adedi'] > 2) & (df['toplam_tutar'] > 200)]
print("\n--- 6.2 Ürün Adedi > 2 ve Tutar > 200 Olanlar ---")
print(filtre2)

# 6.3
df['birim_fiyat'] = df['toplam_tutar'] / df['urun_adedi']
print("\n--- 6.3 Birim Fiyat Sütunu Eklendi ---")
print(df)

# 6.4
df['kargo_durumu'] = df['kargo_suresi'].apply(lambda x: "Yavaş" if x > 3 else "Hızlı")
print("\n--- 6.4 Kargo Durumu Eklendi ---")
print(df)


# --------------------------- SORU 7 (Sıralama) ---------------------------
# 7.1
sirali_tutar = df.sort_values(by='toplam_tutar', ascending=False)
print("--- 7.1 Tutara Göre Büyükten Küçüğe ---")
print(sirali_tutar)

# 7.2
sirali_coklu = df.sort_values(by=['urun_adedi', 'kargo_suresi'])
print("\n--- 7.2 Ürün Adedi ve Kargo Süresine Göre ---")
print(sirali_coklu)


# Kontrol
print("\n--- Kontrol ---")
print(df)

# --------------------------- SORU 8 (Eksik Veri) ---------------------------
# 8.1
eksik_sayisi = df['kargo_suresi'].isnull().sum()
print("8.1 Kargo Süresi Eksik Değer Sayısı:", eksik_sayisi)

# 8.2
medyan_sure = df['kargo_suresi'].median()
df_dolu = df.copy()
df_dolu['kargo_suresi'] = df_dolu['kargo_suresi'].fillna(medyan_sure)
print("\n8.2 Medyan ile Doldurulmuş Veri:")
print(df_dolu)

# 8.3
df_temiz = df.dropna()
print(f"\n8.3 Eksikler Silindi. Eski Boyut: {df.shape}, Yeni Boyut: {df_temiz.shape}")
print(df_temiz)



# --------------------------- SORU 9 (Merge) ---------------------------
musteriler = pd.DataFrame({    "musteri_id": [1, 2, 3, 4],    "ad": ["Baran", "Ceylin", "Emre", "Fulya"]})
siparisler = pd.DataFrame({    "musteri_id": [1, 2, 5],    "urun": ["Kulaklık", "Şarj Kablosu", "Powerbank"],    "tutar": [450, 90, 320]})

print(musteriler)
print(siparisler)


# 9.1
inner = pd.merge(musteriler, siparisler, on='musteri_id', how='inner')
print("--- 9.1 Inner ---")
print(inner)

# 9.2
left = pd.merge(musteriler, siparisler, on='musteri_id', how='left')
print("\n--- 9.2 Left ---")
print(left)

# 9.3
outer = pd.merge(musteriler, siparisler, on='musteri_id', how='outer')
print("\n--- 9.3 Outer ---")
print(outer)


# --------------------------- SORU 10 (Concat) ---------------------------
# 10.1
hafta1 = pd.DataFrame({"gun":["Pzt","Sal"], "adet":[20,35]})
hafta2 = pd.DataFrame({"gun":["Çar","Per"], "adet":[28,40]})
alt_alta = pd.concat([hafta1, hafta2], ignore_index=True)
print("--- 10.1 Alt Alta Birleştirme ---")
print(alt_alta)

# 10.2
gelir = pd.DataFrame({"toplam_gelir":[1000,1750]})
yan_yana = pd.concat([hafta1, gelir], axis=1)
print("\n--- 10.2 Yan Yana Birleştirme ---")
print(yan_yana)


# --------------------------- SORU 11 (Groupby) ---------------------------
df_calisan = pd.DataFrame({    "sube": ["Kadıköy", "Beşiktaş", "Kadıköy", "Şişli", "Beşiktaş"],    "ad": ["Baran", "Ceylin", "Emre", "Fulya", "Gökhan"],    "satis": [12000, 18500, 9500, 21000, 16000]})
print(df_calisan)

# 11.1
toplam_satis = df_calisan.groupby('sube')['satis'].sum()
print("--- 11.1 Toplam Satış ---")
print(toplam_satis)

# 11.2
ortalama_satis = df_calisan.groupby('sube')['satis'].mean()
print("\n--- 11.2 Ortalama Satış ---")
print(ortalama_satis)

# 11.3
coklu_analiz = df_calisan.groupby('sube')['satis'].agg(['sum', 'mean', 'count'])
print("\n--- 11.3 Çoklu Analiz (.agg) ---")
print(coklu_analiz)


# --------------------------- SORU 12 (Pivot) ---------------------------
df_satis = pd.DataFrame({    "sehir": ["Bursa", "Adana", "Antalya", "Bursa", "Adana"],    "kategori": ["Elektronik", "Giyim", "Elektronik", "Giyim", "Elektronik"],    "satis": [5000, 3200, 4100, 2800, 3900]})
print(df_satis)

# 12.1
pivot1 = df_satis.pivot(index='sehir', columns='kategori', values='satis')
print("--- 12.1 Sade Pivot Tablo ---")
print(pivot1)

# 12.2
pivot2 = df_satis.pivot_table(index='sehir', columns='kategori', values='satis', aggfunc='sum', fill_value=0)
print("\n--- 12.2 Parametreli Pivot Tablo ---")
print(pivot2)


# --------------------------- SORU 13 (apply) ---------------------------
# 13.1
df_kullanici = pd.DataFrame({"kullanici_adi": ["baran23", "CEYLIN_K", "emre.y"]})

# 13.2
df_kullanici['kullanici_adi_kucuk'] = df_kullanici['kullanici_adi'].apply(str.lower)

# 13.3
df_kullanici['karakter_sayisi'] = df_kullanici['kullanici_adi'].apply(lambda x: len(x))

print(df_kullanici)



# --------------------------- SORU 14 (Tip Dönüşümü) ---------------------------
# 14.1
df_urun = pd.DataFrame({"urun_id":["10","11","12"], "agirlik_kg":["1.5","0.75","3.2"]})

# 14.2
print("--- 14.2 Başlangıç Tipleri ---")
df_urun.info()

# 14.3
df_urun['urun_id'] = df_urun['urun_id'].astype(int)
df_urun['agirlik_kg'] = df_urun['agirlik_kg'].astype(float)

print("\n--- 14.3 Dönüşüm Sonrası Tipler ---")
df_urun.info()


# --------------------------- SORU 15 (Görselleştirme) ---------------------------
df_gelir = pd.DataFrame({    "ceyrek": ["Ç1", "Ç2", "Ç3", "Ç4"],    "gelir": [42000, 55000, 48000, 61000],    "gider": [30000, 38000, 33000, 40000]})
print(df_gelir)

# 15.1
plt.figure(figsize=(6, 4))
plt.plot(df_gelir['ceyrek'], df_gelir['gelir'], marker='o', color='blue')
plt.title('Çeyreklik Gelir Grafiği')
plt.xlabel('Çeyrek')
plt.ylabel('Gelir')
plt.grid(True)
plt.show()

# 15.2
print("*" * 120)
plt.figure(figsize=(6, 4))
plt.bar(df_gelir['ceyrek'], df_gelir['gelir'], color='green')
plt.title('Çeyreklere Göre Gelir (Bar)')
plt.xlabel('Çeyrek')
plt.ylabel('Gelir')
plt.show()

# 15.3
print("*" * 120)
plt.figure(figsize=(5, 5))
plt.pie(df_gelir['gelir'], labels=df_gelir['ceyrek'], autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'orange', 'pink'])
plt.title('Gelirin Çeyreklik Dağılımı (Pie)')
plt.show()

# 15.4
print("*" * 120)
plt.figure(figsize=(6, 4))
plt.scatter(df_gelir['gelir'], df_gelir['gider'], color='red', s=100)
plt.title('Gelir ve Gider Karşılaştırması')
plt.xlabel('Gelir')
plt.ylabel('Gider')
plt.grid(True)
plt.show()
