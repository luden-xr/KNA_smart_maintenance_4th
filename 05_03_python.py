# print("-----실습1-----")
# data = [28,27,32,35,31]
# for i in data:
#     if i >= 30:
#         print("고온: ", i)


# print("----실습2----")
# data = [1,8,9,7,8,3,1,6,10,3,4,5,6,7,8,9]
# for i in data:
#     if i >= 5 and i <= 10:
#         print(i)



# print("-----실습3-----")
# temp = [32,36,31,24,24,28,29]
# total = 0
# count =0
# for i in temp:
#     if i > 30:
#         total += i
#         count += 1
# print('고온평균', total / count)



# print("-----실습4-----")
# temp = [32,35,31,33,27,24,29,26]
# hollow = []
# for i in temp:
#     if i > 30:
#         hollow.append(i)

# print(temp, "/", hollow)
# print(len(hollow))


# print("-----실습5-----")
# temp = [20,26,27,23,28,31,33]
# h = []
# for i in temp:
#     F = (i*1.8)+32
#     h.append(round(F,2))
# print(f'{temp} / {h}')



# print("-----실습6-----")
# data = [25,26,27,28,29,30,31,32,33,34,35]
# h = []
# j=0
# count_1 = 0
# count_2 =0
# k=0
# for i in data:
#     j += i
#     count_1 += 1
#     if i > 30:
#         count_2 += 1
#         h.append(i)
#         k += i
# print("전체 평균:", j / count_1, "/", "고온 개수:", count_2 ,"/","고온 평균:",(k/count_2))

# print(h)