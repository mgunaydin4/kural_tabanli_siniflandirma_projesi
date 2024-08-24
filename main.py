import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# GÖREV 1

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df = pd.read_csv('persona.csv')

def data_information(df_name):
    print(f"İlk 5 Gözlem\n{df_name.head()}")
    print(f"Hangi değişkende kaç tane boş değer var ?\n{df_name.isnull().sum()}")
    print(f"Veri setindeki sayısal değişkenlerin betimsel istatistikleri\n{df_name.describe()}")
    print(f"Veri seti hakkında bilgi?\n {df_name.info()}")


data_information(df)

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()


# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].nunique()
df["PRICE"].value_counts()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()


# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()
# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby('COUNTRY')['PRICE'].sum()

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

df['SOURCE'].value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby('COUNTRY')['PRICE'].mean()


# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby('SOURCE')['PRICE'].mean()

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(['COUNTRY', "SOURCE"])['PRICE'].mean()


# GÖREV 2
# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(['COUNTRY', "SOURCE", "SEX", "AGE"])['PRICE'].mean()


# Görev 3: Çıktıyı PRICE’a göre sıralayınız.
agg_df = df.groupby(['COUNTRY', "SOURCE", "SEX", "AGE"])['PRICE'].mean().sort_values(ascending=False)
agg_df.head()
agg_df.isnull().sum()

agg_df = pd.DataFrame(agg_df)
agg_df.isnull().sum()

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.

agg_df.reset_index(inplace=True)
agg_df.isnull().sum()

# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.

agg_df["AGE_CAT"] = pd.cut(
    agg_df["AGE"],
    bins=[0, 18, 23, 30, 40, 70],
    labels=['0_18', '19_23', '24_30', '31_40', '41_70']
)

agg_df.head()

# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df.info()
agg_df["AGE_CAT"] = agg_df["AGE_CAT"].astype("object")
agg_df["customers_level_based"] = agg_df['COUNTRY'].str.upper() + '_' + agg_df['SOURCE'].str.upper() + '_' + agg_df['SEX'].str.upper() + '_' + agg_df['AGE_CAT']


new_agg_df = agg_df[["customers_level_based","PRICE" ]]

new_agg_df.head()
new_agg_df["SEGMENT"] = pd.qcut(new_agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

new_user = "BRA_ANDROID_FEMALE_0_18"
new_user_2 = "FRA_IOS_FEMALE_31_40"

new_agg_df[new_agg_df["customers_level_based"] == new_user]