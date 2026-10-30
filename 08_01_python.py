# print("------실습1------")
# import math
# print(math.sqrt(16))

# from math import sqrt
# print(sqrt(16))

# import math as mt
# print(mt.sqrt(16))



# print("-----실습2-----")
# import math
# import random
# x= random.randint(0,10)
# print(x)
# print(math.sqrt(x))

# print("-----실습3-----")
# import os
# print(os.getcwd())

# files = os.listdir("practice")
# print(files)
# for x in files:
#     if x.endswith(".csv"):
#         print(x)


# print("-----실습4-----")
# import os
# path = os.path.join("practice", "08_press_13_261029_3.csv")
# if os.path.exists(path):
#     print(True)

# print("-----실습5-----")
# import os
# import datetime
# dic = len(os.listdir("practice"))
# time = datetime.datetime.now()
# print(f'파일{dic}개, 점검 시각{time}')


# print("-----실습6-----")
# import os
# list = os.listdir("practice")
# new_list = []
# for x in list:
#     if x.endswith(".csv"):
#         path = os.path.join("practice", x)
#         new_list.append(path)
# print(f'[CSV] 목록 {new_list}')