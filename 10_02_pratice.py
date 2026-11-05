import numpy as np

# print("----실습1-----")
# data = np.array([4603,1200,2500,3100,4200,4603])
# first = data[0]
# last = data[-1]

# slice_data = data[1:4]
# step_data = data[::2]

# print(first,last,slice_data,step_data)

# print("-----실습2------")
# # import os
# # import csv
# # with open("practice/10_mct_tool.csv", "r", encoding = "utf-8") as f:
# #     read = csv.reader(f)
# #     header = next(read)
# #     list_read = list(read)
# #     print(list_read[2])
# data = np.array([[42, 2], [38,6],[40,3], [31,8]])
# third = data[2]
# rpm = data[:,0]
# torque = data[:,1]

# print(f'세 번째 시점 한 줄 :{third} / 회전수 열 네 개:{rpm} / 토크 열 네 개:{torque}')


# print("-----실습3-----")
# data = np.array([4602, 3685,1246,5432,1876,7445,2254,4756,3549,6876])
# data_max = np.max(data)
# data_min = np.min(data)
# data_ab = data - data_min
# data_di = data_ab / (data_max - data_min)
# print(np.round(data_di, 2))


# print("-----실습4-----")
# data = np.array([1602, 1685,1246,5432,1876,7445,2254,4756,3549,1876])
# torque = np.array([30,11,60,54,87,21,65,74,22,64])
# print(data[data < 2000])
# print(data[data < 2000], torque[ torque> 25])
# print(np.sum(data < 2000))
# print(np.sum((data < 2000 | (torque > 25)))



# print("-----실습5-----")
# torque = np.array([3,11,6,5,18,2,6,7,2,6])
# over_10 = torque > 10
# count = np.sum(over_10)
# ratio = np.mean(over_10)
# print(f'개수:{count} / 비율:{ratio}')

# data = np.loadtext('practice/10_mct_tool.csv',
#                    delimiter=","
#                    skiprows=1,
#                    usecols=4)  #usecols=(4,5)
# print("-----실습6-----")
# data = np.array([[4602, 30], [3367, 45], [4110, 27], [5321, 55]])
# data_column = np.round(data.mean(axis=0), 1)
# data_column_std = np.round(data.std(axis=0), 1)
# print(data_column, data_column_std)


# print("-----실습7-----")
# data = np.loadtxt('practice/10_mct_tool.csv',
#                    delimiter=",",
#                    skiprows=1,
#                    usecols=4)
# data_mean = np.mean(data)
# data_var = np.round(np.var(data), 1)
# data_max = np.max(data)
# data_min = np.min(data)
# print(data_mean,data_var,data_max,data_min)

# print("-----실습8-----")
# data = np.loadtxt('practice/10_mct_tool.csv',
#                    delimiter=",",
#                    skiprows=1,
#                    usecols=-1)
# over_10 = data[data > 10]
# print(over_10)
# print(np.mean(over_10))
# print(np.mean(data))


print("-----실습9-----")
data = np.loadtxt('practice/10_mct_tool.csv',
                   delimiter=",",
                   skiprows=1,
                   usecols=(-2,-1))
ds = data.shape
dt = data.dtype
print(ds,dt)
ds_r1 = data[:,0]
rpm = ds_r1[ ds_r1 < 2000]
print(np.mean(rpm),np.mean(ds_r1),rpm.size)
