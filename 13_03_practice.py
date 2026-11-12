import pandas as pd
F_m='practice/13_diecasting_master.csv'
F_s='practice/13_diecasting_shot.csv'

# print("------실습1------")
# df_1 = pd.read_csv(F_m)
# df_2 = pd.read_csv(F_s)
# print(df_1.shape,df_2.shape)

# log_m = df_1.columns.tolist
# print(log_m)
# log_s = df_2.columns.tolist
# print(log_s)

# df_merge = pd.merge(df_1, df_2, on='설비ID')
# print(df_merge.shape)

# print(df_merge.head(2))

# print(len(log))
# print(len(master), master['설비ID'].nunique())

# m_left = log.merge(master, on='설비ID', how="left")
# print(len(m_left))
# print(len(m_left)["라인"].isna().sum())


# unmatched = m_left[m_left['라인'].isna]
# print(unmatched['설비ID'].head(1).tolist(), len(unmatched))


# print("------실습2------")
# df_log = pd.read_csv(F_s)
# df_eq = pd.read_csv(F_m)

# m_inner = pd.merge(df_log, df_eq, on = '설비ID', how='inner')
# print("inner",m_inner.shape)

# m_left = pd.merge(df_log, df_eq, on = '설비ID', how='left')
# m_outer = pd.merge(df_log, df_eq, on = '설비ID', how='outer')

# print("left",m_left.shape,"outer", m_outer.shape)

# unmatched = m_left[m_left['라인'].isna()]
# print(len(unmatched['설비ID']),unmatched['설비ID'])

# unmatched_ot = m_outer[m_outer['샷'].isna()]
# print(len(unmatched_ot['설비ID']),unmatched_ot['설비ID'])




# print("-----실습3-----")
# df_log = pd.read_csv(F_s)
# part_1 = df_log.iloc[:100].reset_index(drop=True)
# part_2 = df_log.iloc[100:].reset_index(drop=True)

# cc = pd.concat([part_1,part_2])
# print(cc.shape,"/",len(cc.loc[0]),"행")

# df = pd.concat([part_1,part_2], ignore_index=True)
# lasd_df = df.index[-1]
# print(lasd_df)

print("------실습4------")
df_log = pd.read_csv(F_s)
df_eq = pd.read_csv(F_m)
print(df_log.shape, df_eq.shape)
df_merge = pd.merge(df_log, df_eq, on='설비ID', how='left')
df_valid = df_merge[df_merge['라인'].notna()]
print(df_valid.shape)
df_na = df_valid[df_valid['품질등급'] != '양품']
print(len(df_na))
top5 = df_na.sort_values('비스킷두께', ascending=False)[['샷','설비ID','라인','비스킷두께','품질등급']].head()
print(top5)