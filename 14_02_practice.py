import pandas as pd
F='practice/14_hydraulic.csv'
F_QC = 'practice/14_hydraulic_qc.csv' 

# print("-----실습1-----")
# df = pd.read_csv(F_QC)
# print(df['검사결과'].value_counts())
# print(df.groupby("검사결과")['온도'].agg(['mean', 'std', 'max']).round(2))
# table = df.groupby('검사결과').agg(평균온도=('온도','mean'),
#                                평균냉각효율=('냉각효율', 'mean'),
#                                측정수=('온도','count')
#                                ).round(2)
# print(table)


# print("-----실습2-----")
# df = pd.read_csv(F).copy()
# df['상태별평균온도'] = df.groupby('냉각기상태')['온도'].transform('mean')

# df['온도편차'] = (df['온도']-df['상태별평균온도']).round(2)
# print(df[['냉각기상태','온도','상태별평균온도','온도편차']].head(3))
# max_idx = df['온도편차'].abs().idxmax()
# max_val = df.loc[max_idx]
# print(max_val)

# pt = df.pivot_table(index='밸브상태',columns='운전부하',values='온도',aggfunc='mean',margins=True,margins_name='전체').round(2)

# print(pt)

print("-----실습3-----")
df = pd.read_csv(F)
cor_vib = df['온도'].corr(df['진동']).round(3)
cor_pres = df['온도'].corr(df['압력']).round(3)
cor_effi = df['온도'].corr(df['냉각효율']).round(3)

print(f'{cor_vib}/{cor_pres}/{cor_effi}')
cor_tb=df[['온도','진동','압력','냉각효율']].corr().round(3)
print("네 열의 상관계수 표\n",cor_tb)

cor_col = cor_tb.unstack()
cor_col = cor_col[cor_col != 1.0]
pair_max = cor_col['냉각효율'].abs().idxmax()
pair_min = cor_col['냉각효율'].abs().idxmin()
print(pair_max,cor_col[pair_max], pair_min,cor_col[pair_min])
