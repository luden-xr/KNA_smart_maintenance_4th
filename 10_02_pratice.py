import numpy as np

# print("----실습1-----")
# data = np.array([4603,1200,2500,3100,4200,4603])
# first = data[0]
# last = data[-1]

# slice_data = data[1:4]
# step_data = data[::2]

# print(first,last,slice_data,step_data)

print("-----실습2------")
# import os
# import csv
# with open("practice/10_mct_tool.csv", "r", encoding = "utf-8") as f:
#     read = csv.reader(f)
#     header = next(read)
#     list_read = list(read)
#     print(list_read[2])
data = np.array([[42, 2], [38,6],[40,3], [31,8]])
third = data[2]
rpm = data[:,0]
torque = data[:,1]

print(f'세 번째 시점 한 줄 :{third} / 회전수 열 네 개:{rpm} / 토크 열 네 개:{torque}')
