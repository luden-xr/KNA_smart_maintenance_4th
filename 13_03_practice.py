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


print("------실습2------")
df_log = pd.read_csv(F_s)
df_eq = pd.read_csv(F_m)

m_inner = pd.merge(df_log, df_eq, on = '설비ID', how='inner')
print("inner",m_inner.shape)

m_left = pd.merge(df_log, df_eq, on = '설비ID', how='left')
m_outer = pd.merge(df_log, df_eq, on = '설비ID', how='outer')

print("left",m_left.shape,"outer", m_outer.shape)

unmatched = m_left[m_left['라인'].isna()]
print(len(unmatched['설비ID']),unmatched['설비ID'])

unmatched_ot = m_outer[m_outer['샷'].isna()]
print(len(unmatched_ot['설비ID']),unmatched_ot['설비ID'])