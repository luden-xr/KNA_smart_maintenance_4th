import pandas as pd
# print("-----실습1-----")
# df = pd.read_csv('practice/13_diecasting_small.csv')
# print(df['형체력'].head(3), df['형체력'].shape)
# print(df[['형체력','실린더압력']].shape,df[['형체력','실린더압력']].astype)
# print(df[['형체력']].shape)

# print("-----실습2-----")
# df = pd.read_csv('practice/13_diecasting_small.csv')
# loc = df.loc[0, '샷']
# iloc = df.iloc[0,0]
# x = df.sort_values('형체력', ascending=False)

# re_loc = x.loc[0, '샷']
# re_iloc = x.iloc[0,0]

# print(f'{loc} / {iloc}')
# print(f'{re_loc} / {re_iloc}')

# print("-----실습3-----")
# df = pd.read_csv('practice/13_diecasting_small.csv')
# print(df.columns.tolist())
# print(df[['실린더압력','형체력']].shape)
# loc = df.loc[0:4, ['실린더압력','형체력']]
# print(loc)
# iloc = df.iloc[0:5, [2,6]]
# print(iloc)
# print(loc.shape)
# print(iloc.shape)

print("-----실습4-----")
df = pd.read_csv('practice/13_diecasting_shot.csv')
print(df.columns.tolist(), df.shape)
loc = df.loc[0:9, ['설비ID','비스킷두께','품질등급']]
print(loc,loc.shape)
loc_2 = df.iloc[-5:]
print(loc_2,loc_2.shape)