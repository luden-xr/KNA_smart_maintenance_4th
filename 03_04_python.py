# # 메서드 - 점(.) 문법
# # 형식: 문자열.매서드이름()  괄호 무조건 붙이기1!!!!!
# word = 'Python'
# print(word.upper())





# print("------실습1------")

# data = 'ready'
# cap = data.upper()

# print(cap)

# print("-----실습2----")

# data = "WARNING"
# x = data.lower()

# print(x)


# print("-----실습3-----")

# name = 'kim chul soo'
# change_name = name.title()

# print(change_name)



# print("------실습4------")

# data_1 = 'Fault'
# data_2 = 'FAULT'

# print(data_1 == data_2)
# print(data_1.lower() == data_2.lower())



# print("-----실습5------")
# x = 'ABC'
# y = 'abc'
# z = 'Abc'

# print(x.isupper(), y.islower(), z.isupper())



# print("-----실습6-----")


# x = 'Sensor_LOG.scv'
# change_x = x.lower()
# print(change_x.startswith('sensor'), "/", change_x.endswith('.scv'))



# print("------실습7-----")

# data = ' 가동중 '
# print(data.strip())

# print("-----실습8-----")

# data = ' 대기 '
# print("["+ data.lstrip()+"]")
# print("["+data.rstrip()+"]")



# print("-----실습9-----")
# data = "***경고***"
# print(data.strip('*'))



# print("-----실습10-----")

# state = ' WARNING '
# print(state.strip().lower())



print("-----실습11-----")

data = ' 경보 '
data.strip()
print("["+data+"]")

data = data.strip()
print("["+data+"]")
