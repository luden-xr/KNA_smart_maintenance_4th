# print("-----실습1-----")
# sensor = ('모터온도', 78)
# print(sensor[0])
# print(sensor[1])
# print(str(sensor[0]),"/",int(sensor[1]))



# print("----실습2----")
# sensors = ("회전속도", 95), ("펌프압력", 99), ("현재 온도", 85)
# for name, value in sensors:
#     if value > 90:
#         print(name, "경고")

# print("----실습3----")
# sensors = ("모터온도", 80,(4,8)), ("펌프압력", 90,(3,4)), ("현재 온도", 30, (6,9))
# for x, y, z in sensors:
#     if z[0] <= 5:
#         print(x,z)


# print("-----실습4-----")
# id = ("S01", "S02", "S03","S01")

# id_set = set(id)
# id_sorted = sorted(id_set)
# print("종류수:",len(id_sorted))
# print(id_set)


# print("-----실습5-----")
# id_1 = {'S01', 'S02','S03','S05'}
# id_2 = {'S03','S04','S05'}


# id_u = id_1.union(id_2)
# id_i = id_1.intersection(id_2)
# print("전체:",id_u)
# print("공통:",id_i)
# print(id_1.difference(id_2))
# print(id_2.difference(id_1))


# print("-----실습6-----")
# yesterday = {'S02','S03'}
# today = {'S02','S03','S05'}
# inter = today.intersection(yesterday)
# print("신규이상:",today.difference(yesterday))
# print("지속이상:",inter)


# 실습 4
logs = ["S01", "S02", "S01", "S03", "S02"]
unique_logs = set(logs)
print(sorted(unique_logs))
print("종류 수:", len(unique_logs))

# 실습 5
line_a = {"S01", "S02", "S03", "S05"}
line_b = {"S03", "S04", "S05"}
print(line_a.union(line_b))         # 전체
print(line_a.intersection(line_b))  # {'S03', 'S05'}
print(line_a.difference(line_b))    # {'S01', 'S02'}
print(line_b.difference(line_a))    # {'S04'}


# 실습 6
yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}
print(today.difference(yesterday))    # 신규: {'S05'}
print(today.intersection(yesterday))  # 지속: {'S02', 'S03'