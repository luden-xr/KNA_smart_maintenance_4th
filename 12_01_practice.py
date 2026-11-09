import numpy as np
import pandas as pd


#Pandas
# 표 형태의 데이터를 잘 다루기 위해
# series(열)
# dataframe

F = 'practice/12_metro_compressor.csv'

# print("-----실습1-----")
# df = pd.read_csv(F)
# df.head()
# df.shape

# print(df.head(),df.shape)

# print("-----실습2-----")
# data = pd.read_csv(F,usecols=['측정시각','압축압력','배출압력']) #측정시각,압축압력,배출압력
# print(data.shape)

# data_1 = pd.read_csv(F,nrows=20)
# print(data_1.shape)

# data_x = pd.read_csv(F,usecols=['측정시각','압축압력','배출압력'],nrows=20)
# print(data_x.shape)
# print(data_x.head())


# print("-----실습3-----")
# df = pd.read_csv('practice/12_metro_compressor_semicolon.csv',sep=";",encoding ="utf-8")
# df_none = pd.read_csv('practice/12_metro_compressor_semicolon.csv')
# print(df_none.shape)
# print(df.shape)
# print(df.head())

print("-----실습4-----")
df = pd.read_csv('practice/12_metro_compressor_semicolon.csv',sep=";",usecols=['측정시각','오일온도','모터전류'],nrows=50,encoding ="utf-8")

print(df.shape)
print(df.head(3))

