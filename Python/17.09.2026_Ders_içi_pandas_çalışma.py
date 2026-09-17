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

okunan = pd.read_csv("takimlar.csv")
print(okunan)

# index=False kullanmadan kaydetme -> dosyaya fazladan index sütunu yazılır
takimlar.to_csv("takimlar_indexli.csv")
print(pd.read_csv("takimlar_indexli.csv"))


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
