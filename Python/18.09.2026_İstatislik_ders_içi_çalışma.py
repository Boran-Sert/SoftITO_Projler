import warnings

from scipy.stats import levene

warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF
from statsmodels.stats.multicomp import pairwise_tukeyhsd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv(r'C:\Users\boran\Documents\Projeler\SoftITO_Projeler\Python\Dataset\StudentsPerformance.csv')
sayisal_sutunlar = df.select_dtypes(include=np.number).columns

# KONTROL YERİ
def kontrol():
    print(df.head(5))
    print(df.info())

# OZET YERİ
def ozet():
    ozet = pd.DataFrame({
        "dtype": df.dtypes,
        "n_unique": df.nunique(),
        "eksik_değer": df.isnull().sum(),
        "eksik_değer_yüzdesi": (df.isnull().mean() * 100).round(2)
    })
    print(ozet)

# Betimsel İstatistik ve güven aralığı
def guven_araligi_tablosu(df, guven=0.95):

    print(f"{'değişken':20s},{'Ortalama':>12s},{'%95 Alt':>12s},{'%95 Üst':>12s}")
    for degisken in sayisal_sutunlar:
        veri = df[degisken].dropna()
        n = len(veri)
        ortalama = veri.mean()
        sem = stats.sem(veri)                        # standart error of the mean
        t_kritik = stats.t.ppf((1 + guven) / 2, df=n - 1)
        hata_payi = t_kritik * sem
        print(f"{degisken:20s},{ortalama:>12.2f},{ortalama - hata_payi:>12.2f},{ortalama + hata_payi:>12.2f}")

    betimsel = df[sayisal_sutunlar].describe().T
    betimsel["skew"] = df[sayisal_sutunlar].skew()
    betimsel["kurtosis"] = df[sayisal_sutunlar].kurtosis()
    betimsel.round(2)
    print(betimsel)

#Normallik Testleri
def normallik(df):
    print(f"{'Değişken':20s} {'Shapiro-Wilk p':>16s} {'DAgostino p'} Yorum ")
    for degisken in sayisal_sutunlar:
        veri = df[degisken].dropna()
        ornek = veri.sample(min(len(veri), 100),random_state=0)
        sw_stat, sw_p = stats.shapiro(veri)
        da_stat, da_p = stats.normaltest(veri)

        yorum = "Normallik varsayımı sağlanıyor." if sw_p > 0.05 else "Normallik varsayımı sağlanmıyor."
        print(f"{degisken:20s},{sw_p:>16.4f},{da_p:>16.4f},{yorum}")

    fig, axes = plt.subplots(1, len(sayisal_sutunlar), figsize=(18, 4))
    for ax, col in zip(axes, sayisal_sutunlar):
        stats.probplot(df[col].dropna(), dist="norm", plot=ax)
        ax.set_title(f"Q-Q Grafiği: {col}")
    plt.tight_layout()
    plt.show()


# İki Grup Karşılaştırması
grup0 = df.loc[df["gender"] == "female"].dropna()
grup1 = df.loc[df["gender"] == "male"].dropna()

levene_stat, levene()

if __name__ == "__main__":
    normallik(df)