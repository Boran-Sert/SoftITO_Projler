import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

n = 1000

df = pd.DataFrame({
"musteri_id": range(1, n + 1),
"yas": np.random.normal(38, 12, n).round(0),
"gelir": np.random.lognormal(mean=10.5, sigma=0.6, size=n).round(2),
"sehir": np.random.choice(
["İstanbul", "Ankara", "İzmir", "Bursa", "istanbul", "ANKARA"],  # kasıtlı tutarsız yazım
size=n, p=[0.35, 0.2, 0.15, 0.1, 0.1, 0.1]
),
"abonelik_tipi": np.random.choice(["Temel", "Standart", "Premium"], size=n, p=[0.5, 0.35, 0.15]),
"kayit_tarihi": pd.date_range("2022-01-01", periods=n, freq="7h"),
"aylik_harcama": np.random.gamma(shape=2, scale=150, size=n).round(2),
"memnuniyet_puani": np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.05, 0.1, 0.2, 0.35, 0.3]),
"churn": np.random.choice([0, 1], size=n, p=[0.8, 0.2]),
})

df.loc[df.sample(frac=0.08, random_state=1).index, "gelir"] = np.nan
df.loc[df.sample(frac=0.05, random_state=2).index, "yas"] = np.nan
df.loc[df.sample(frac=0.03, random_state=3).index, "memnuniyet_puani"] = np.nan
outlier_idx = df.sample(frac=0.01, random_state=4).index
df.loc[outlier_idx, "gelir"] = df["gelir"].max() * np.random.uniform(3, 6, len(outlier_idx))
df = pd.concat([df, df.sample(5, random_state=7)], ignore_index=True)

print(df["sehir"].value_counts())
df["sehir"] = df["sehir"].replace({"istanbul": "İstanbul", "ANKARA": "Ankara"})
print(df["sehir"].value_counts())

print(df.query("yas < 0 or yas > 100")[["musteri_id", "yas"]])