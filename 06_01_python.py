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

print("----실습3----")
sensors = ("모터온도", 80,(4,8)), ("펌프압력", 90,(3,4)), ("현재 온도", 30, (6,9))
for x, y, z in sensors:
    if z[0] <= 5:
        print(x,z)