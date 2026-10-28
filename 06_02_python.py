# print("-----실습1-----")
# sensor = {"센서1":1, "센서2":2,"센서3":3}

# sensor["센서4"] = 4
# sensor["센서3"] = 78
# print(sensor.get("센서5",0))
# print("센서1" in sensor)

# print(sensor)

# print("-----실습2-----")
# sensor = {"압력":75, "온도":60}
# new_sensor = {"압력":80, "응력":20}

# sensor.update(new_sensor)
# print(sensor)
# del sensor["응력"]
# print(len(sensor))



# print("-----실습3-----")
# data = {"값1":95, "값2":70, "값3": 78, "값4":83, "값5":72, "값6":74}
# data_v = data.values()
# s = sum(data_v)/ len(data_v)
# print(s)
# value_max = 0
# name_max = None
# for name, value in data.items():
#     if value > value_max:
#         value_max = value
#         name_max = name
# print(f'최댓값 센서:{name_max} / {value_max}')

# for name, value in data.items():
#     if value == data[name]:
#         print(value)



# print("-----실습4-----")
# name = ['온도', '진동', '압력']
# data = [78, 0.5, 95]

# x = dict(zip(name, data))
# print(x)

# for y, z in x.items():
#     print(y,z)



# print("------실습5-----")
# data_1 = {"온도":80, "진동":60,"압력":50}
# data_lim = {"온도":80, "진동":70, "압력":60}

# for name_1, name_2 in data_1.items():
#     for name_3, name_4 in data_lim.items():
#         if name_1 == name_3 and name_2 >= name_4:
#             print("경고센서", name_1)

# print("-----실습6-----")
# data = {
#     "펌프1":{"온도":78, "상태": "정상"},
#     "펌프2":{"압력":95, "상태": "경고"}
# } 

# for name, info in data.items():
#     if info["상태"] == "경고":
#         print(name, "점검 필요")

# print("------실습7-----")
# list = ["온도,78", "압력,95", "진동,0.5"]
# sensor = {}
# for x in list:
#     y, z = x.split(",")
#     sensor[y] = z
# print(sensor)   


print("-----실습8-----")
data_1 = {"온도":90, "진동":60,"압력":70}
data_lim = {"온도":80, "진동":70, "압력":60}
avg = sum(data_1.values())/len(data_1.values())
print(round(avg,2))

set_blank = set()
for x, y in data_1.items():
    if y > data_lim[x]:
        set_blank.add(x)
            
print("위험 센서", sorted(set_blank))



