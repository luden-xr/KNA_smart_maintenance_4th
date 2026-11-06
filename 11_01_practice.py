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

# print("-----실습2-----")
# data_1 = np.genfromtxt('practice/11_diecasting_series.csv',
#                    delimiter=",",
#                    skip_header=1,
#                    usecols=(0))
# data_2 = np.genfromtxt('practice/11_diecasting_series.csv',
#                    delimiter=",",
#                    skip_header=1,
#                    usecols=(1))
# difference = np.diff(data_2)
# ex_val = np.abs(difference)
# j = int(np.argmax(ex_val))
# print(j)
# print(data_2[j], data_2[j+1],difference[j])


# print
# ("-----실습3-----")
# data_2 = np.genfromtxt('practice/11_diecasting_series.csv',
#                    delimiter=",",
#                    skip_header=1,
#                    usecols=(2))
# print(np.mean(data_2))
# data_2[0] = 9999
# wrd_mean = np.round(np.mean(data_2), 1)
# print(wrd_mean)
# fixed = np.clip(data_2,100,300)
# print(np.mean(fixed))

# print("-----실습4-----")
# data_2 = np.genfromtxt('practice/11_diecasting_series.csv',
#                    delimiter=",",
#                    skip_header=1,
#                    usecols=(1))
# status = np.where(data_2 >= 1000, 2, np.where(data_2 >=50,1,0))
# val, count = np.unique(status, return_counts = True)
# ratio = count / len(data_2)
# print(val)
# print(count)
# print(f'정상{count[0]} / 경고{count[1]} / 잼{count[2]} / 비율{ratio}')

# print("-----실습5-----")
# def col(c) :
#     return np.genfromtxt('practice/11_diecasting_series.csv',
#                     delimiter=",",
#                     skip_header=1,
#                     usecols=(c))    #c=1,2,3,4
    
# newstack = np.stack([col(1),col(2),col(3),col(4)])
# newshape = np.stack([col(1),col(2),col(3),col(4)]).shape
# print(newshape)
# stack_10 = newstack[:,-10:]
# print(stack_10.shape)

print("-----실습6-----")
def col(c) :
    return np.genfromtxt('practice/11_diecasting_series.csv',
                    delimiter=",",
                    skip_header=1,
                    usecols=(c))    #c=0,1,2
num = col(0)
ct = col(1)
cyn = col(2)
i = np.argmax(ct)
num_max = int(num[i])
ct_max = ct[i]

dif = np.diff(col(1))
j = int(np.argmax(dif))
diff_max_1 = int(num[j])
diff_max_2 = int(num[j+1])

ct_con =np.mean( (ct >= 50) | (cyn < 150))

top3_ct = np.argsort(ct)[::-1][:3]
top3_num = num[top3_ct].astype(int)
print(f'최대{num_max}번 {ct_max} 급변 {diff_max_1}->{diff_max_2} 경고비율 {ct_con} 상위 세 시점{top3_num}')