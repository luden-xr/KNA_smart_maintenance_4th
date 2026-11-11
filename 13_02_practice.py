import pandas as pd

F_SHOT = 'practice/13_diecasting_shot.csv'

# df = pd.read_csv(F_SHOT)
# print(df.shape)
# print("-----실습1-----")
# df = pd.read_csv(F_SHOT)
# print(df.shape)
# con = df['비스킷두께'] >= 16
# # print(con)
# con_true = con.sum()
# df_over = df[con]
# len_over = len(df_over)
# print(len_over)

# con_und = df['비스킷두께'] < 16
# df_under = df[con_und]
# # print(df_under)
# len_under = len(df_under)
# print(len_under)

# nan_cnt = len(df) - (len_over + len_under)
# print(nan_cnt)

# print("-----실습2-----")
# df = pd.read_csv(F_SHOT)
# df_con = df[(df['비스킷두께']>=16) & (df['사이클타임']>=25)]
# print(len(df_con))
# df_con_1 = df[(df['비스킷두께']>=16) | (df['사이클타임']>=25)]
# print(len(df_con_1))
# con_bad = df[~(df['품질등급']== '불량')]
# print(len(con_bad))

# print("-----실습3-----")
# df = pd.read_csv(F_SHOT)
# df_isin = df[df['품질등급'].isin(['주의','불량'])]
# print(len(df_isin))

# df_between = df[df['비스킷두께'].between(10, 16)]
# cnt_between = len(df_between)
# print(cnt_between)
# print(len(df[df["설비ID"].str.contains("A")]))
# A_one = df[df['설비ID'] == 'DIE-A-01']
# print(len(A_one))


print("-----실습4-----")
df = pd.read_csv(F_SHOT)
df_sort = df.sort_values('비스킷두께', ascending=False).head(5)
df_sort_1 = df['샷'].head(5).tolist()
print(df_sort_1)
# print(df_sort)
# df_sort_2 = df.sort_values(['품질등급','사이클타임'], ascending=[True,False]).head(5)
# print(df_sort_2)

# # print("-----실습5-----")
# df = pd.read_csv(F_SHOT)
# df_con = df[(df['품질등급'] != '양품') & (df['비스킷두께'] >= 16)]
# df_sort = df_con.sort_values('비스킷두께', ascending = False)
# result = df_sort[['샷','비스킷두께','품질등급']].head(5)
# print(result)
# print(df_sort.shape)
# nan_not = df[(df['품질등급'] != '양품')&(df['비스킷두께'].isna())]
# print(nan_not)
# print(len(nan_not))