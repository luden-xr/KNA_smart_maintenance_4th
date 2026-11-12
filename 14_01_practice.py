F='practice/14_hydraulic.csv'
F_QC = 'practice/14_hydraulic_qc.csv' 
import pandas as pd


# print("-----실습1-----")
# df = pd.read_csv(F)
# print(df.shape)

# count = df['밸브상태'].value_counts()
# ratio = df['밸브상태'].value_counts(normalize=True)
# print(count,'/',round(ratio,2))


# count_1 = df['운전부하'].value_counts()
# ratio_1 = df['운전부하'].value_counts(normalize=True)
# print(count_1,'/',round(ratio_1,2))


#for counts in [value_counts, load_counts]:
      #print(counts[counts == counts.max()])
      #print(counts[counts == counts.max()])
# print("밸브 최다:", count[count == count.max()].index.tolist())
# print("밸브 최소:", count[count == count.min()].index.tolist())
# print("운전 부하 동률:", count_1[count_1 == count_1.max()].index.tolist())

# print("-----실습2-----")
# df = pd.read_csv(F_QC)
# print(df.shape)
# count = df['검사결과'].value_counts()
# ratio = df['검사결과'].value_counts(normalize=True)
# print(count)
# print(round(ratio,3))

# pct = ratio['불합격']*100
# print(pct,"%")

# print("-----실습3-----")
# df = pd.read_csv(F)
# df_min = df['진동'].min()
# df_max = df['진동'].max()
# spdf = pd.cut(df['진동'],bins=[0,0.6,0.7,10],labels=['낮음','보통','강함'], right=True)
# sp_na = spdf.isna().sum()
# cnt_spdf= spdf.value_counts()
# print(sp_na,cnt_spdf)
# print("최대구간:", cnt_spdf[cnt_spdf == cnt_spdf.max()].index.tolist())
# print("최소구간:", cnt_spdf[cnt_spdf == cnt_spdf.min()].index.tolist())

print("-----실습4-----")
df = pd.read_csv(F)
cnt_1 = df[df['냉각기상태'] == '고장']
cnt_2 = df[df['냉각기상태'] == '저하']
cnt_3 = df[df['냉각기상태'] == '정상']
print(len(cnt_1),len(cnt_2),len(cnt_3))
group_mean = df.groupby('냉각기상태')['온도'].mean().round(2)
group_max = df.groupby('냉각기상태')['온도'].max().round(2)
print(group_mean,"\n",group_max)
gap = group_mean.max() - group_mean.min()
print(gap)


print("-----실습5-----")
df = pd.read_csv(F)
total = df['밸브상태'].value_counts()
print(total)
broken = df[df['result'] == '고장']
broken_counts = broken.groupby('밸브상태').size()
print(broken_counts)

broken_counts = broken_counts.reindex(total.index, fill_value =0)
ratio = broken_counts / total
print(ratio.sort_values(ascending=False).round(3))
# cnt_1 = df[df['냉각기상태'] == '고장']
# cnt_2 = df[df['냉각기상태'] == '저하']
# cnt_3 = df[df['냉각기상태'] == '정상']
# # cr = cnt_1.groupby('밸브상태').size()
# print(cr)
# df_1 = cnt_1[cnt_1['밸브상태'] == '정상']
# df_2 = cnt_1[cnt_1['밸브상태'] == '지연']
# df_3 = cnt_1[cnt_1['밸브상태'] == '경미']
# df_4 = cnt_1[cnt_1['밸브상태'] == '심각']
# print(len(df_1),len(df_2),len(df_3),len(df_4))



