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

print("----실습2-----")
data = col(1)
percent_25 = round(float(np.percentile(data,25)),2)
percent_75 = round(float(np.percentile(data,75)),2)
iqr = (percent_75-percent_25)
upper = round((percent_75 + iqr*1.5),2)
over_data = data[data > upper]

print(f'상항{upper} / 값 {over_data} / 개수 {np.sum(over_data)}')


