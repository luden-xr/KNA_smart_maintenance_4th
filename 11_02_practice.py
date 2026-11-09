import numpy as np
F= 'practice/11_hydraulic_cooler.csv'
def col(c):
    return np.genfromtxt(F, delimiter=",",skip_header=1, usecols=c)

# print("-----실습1-----")
# data = col(2)
# is_there_any_nan = np.isnan(data)
# nan_cnt = np.sum(is_there_any_nan)
# nan_ratio = nan_cnt / len(data)
# nan_mean = np.nanmean(data)
# real_mean = np.mean(data)

# print(nan_cnt,"/",nan_ratio,"/",round(nan_mean,1),"/",real_mean)

# print("----실습2-----")
# data = col(1)
# percent_25 = round(float(np.percentile(data,25)),2)
# percent_75 = round(float(np.percentile(data,75)),2)
# iqr = (percent_75-percent_25)
# upper = round((percent_75 + iqr*1.5),2)
# over_data = data[data > upper]

# print(f'상항{upper} / 값 {over_data} / 개수 {np.sum(over_data)}')


# print("-----실습3-----")
# data = col(0)
# temp = col(2)

# temp_mean = np.nanmean(temp)
# temp_std = np.nanstd(temp)

# z = (temp - temp_mean) / temp_std
# abs = np.abs(z)
# over_2 = abs > 2

# out = data[over_2].astype(int)
# max_z = np.nanmax(abs)

# print(f'이상 번호{out} / 최대 {max_z:.2f}')

# print("-----시습4-----")
# data = col(0)
# temp = col(1)

# temp_mean = np.nanmean(temp)
# temp_std = np.nanstd(temp)

# upper = temp_mean + 3*(temp_std)

# over = temp > upper
# data_out = data[over].astype(int)

# print(f'상한{upper:.2f} / 걸린 사이클 번호{data_out}')


# print("-----실습5-----")
# temp = col(1)
# ce = col(3)

# cor_matrix = np.corrcoef(temp, ce)

# r = cor_matrix[0,1]
# print(f'상관계수:{r:.2f}')


# print("-----실습6-----")
# s = np.stack([col(1), col(2), col(3), col(4)])
# print (s.shape)

# sensor_mean = np.nanmean(s, axis=1)
# sensor_std = np.nanstd(s, axis=1)

# mean = np.round(sensor_mean,1)
# std = np.round(sensor_std, 1)
# print(f'센서별 평균{mean} / 흩어진 정도{std}')

# print("-----실습7-----")
# data = col(0)
# t = col(1)

# t_mean = np.nanmean(t)
# sum = np.cumsum(t - t_mean)
# sum_min = np.argmin(sum)
# num = data[sum_min]
# print(f'{num}번 사이클 뒤가 경계 후보 / 47번은 경보 초과 시작')


print("-----실습8-----")
data = col(0)
t = col(1)
effi = col(3)
t_mean = np.nanmean(t)
effi_mean = np.nanmean(effi)
t_std = np.nanstd(t)
effi_std = np.nanstd(effi)

t_nor = np.abs((t-t_mean)/t_std)
effi_nor = np.abs((effi-effi_mean)/effi_std)

score = t_nor + effi_nor
score_max = np.nanargmax(score)
dm = int(data[score_max])
sm = score[score_max]

top3_idx = np.argsort(score)[::-1][:3]
top3 = data[top3_idx].astype(int)

# data_not = data[label > 0].astype(int)

print(f'최고접수{score_max}({sm:.2f})번 / 상위 세 지점{top3}')


