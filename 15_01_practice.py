import pandas as pd

F_PROC = 'practice/15_사출성형_공정.csv'
F_LOG = 'practice/15_사출성형_로그.csv'

#결측 처리
#-종류: NaN, None, NA,NaT
# 표현은 달라도 isna()로 결측 여부 확인 가능

# s = pd.Series([10, None, 20])
# print(s.mean()) #15.0 ->NaN 값이 있따고 해서 계산이 멈춘다!



# print("-----실습1-----")
# df = pd.read_csv(F_LOG)
# print(df.shape)

# nan_col = df.isna().sum()
# nan_total = nan_col.sum()
# print("한 열에 몇개?\n", nan_col)
# print("NaN 전체 개수\n", nan_total)

# cnt_zero = (df['사출압력'] == 0).sum()
# cnt_vel = (df['스크루속도'] == -999).sum()
# cnt_nine = (df['배럴온도'] == 999).sum()

# print(cnt_zero, cnt_vel, cnt_nine)


print("-----실습2-----")
df=pd.read_csv(F_PROC)
print(df.shape, df.head(3))
df.info()
max_vel=df['최대사출속도'].describe()
print(max_vel[['count','min','max']])