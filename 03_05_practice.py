# print("------실습1------")

# info = '설비 정상 가동'
# info = info.replace('정상','점검')
# # print(info)

# print("------실습2------")
# x = 'PUMP A 03'
# x = x.split()
# print(x)

# print("------실습3------")

# x = 'a,b,c,d'
# x = x.split(',')

# print(x)



# print("-----실습4-----")

# x = 'a,b,c,d'
# x = x.split(',',1)
# print(x)

# print("------실습5-----")

# date = '2025-01-15'
# date = date.split('-')
# date = '-'.join(date)

# print(date)



# print('-----실습6-----')

# print('2025', '1', '15',sep='-')
# print('2025', '1', '15',sep=',')


# print('-----실습7-----')

# date = '2025/01/15'
# date = date.split('/')
# print(date)
# date = '-'.join(date)
# print(date)



print('-----실습8-----')

data = '1,NORMAL,25.3'
data = data.split(',')
print(data[1].strip().lower())