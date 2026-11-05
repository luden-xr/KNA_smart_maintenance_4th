import numpy as np
# print("-----실습1-----")
# data_1 = np.genfromtxt('practice/11_diecasting_series.csv',
#                    delimiter=",",
#                    skip_header=1,
#                    usecols=(0))
# data_2 = np.genfromtxt('practice/11_diecasting_series.csv',
#                    delimiter=",",
#                    skip_header=1,
#                    usecols=(1))
# i = np.argmax(data_2)
# print(i)
# shot_i = int(data_1[i])
# ct_i = data_2[i]
# print(f'{shot_i}번 샷 사이클 타임{ct_i}초')

print("-----실습2-----")
data_1 = np.genfromtxt('practice/11_diecasting_series.csv',
                   delimiter=",",
                   skip_header=1,
                   usecols=(0))
data_2 = np.genfromtxt('practice/11_diecasting_series.csv',
                   delimiter=",",
                   skip_header=1,
                   usecols=(1))
difference = np.diff(data_2)
ex_val = np.abs(difference)
j = int(np.argmax(ex_val))
print(j)
print(data_2[j], data_2[j+1],difference[j])