# print("------실습1-----")

# name = '설비 PUMP_A'
# degree = '온도 87도'

# print(f'{name},{degree}')




# print("-----실습2-----")

# score_1 = 86
# score_2 = 87
# score_3 = 88

# print(f'{(score_1 + score_2 + score_3)/3}')


# print("-----실습3-----")

# data = 87.456

# print(f'{data:.1f}')
# print(f'{data:.2f}')


print("-----실습4-----")
data = ' 5, sensor_2, WARNING, 0.78912 '
data = [data.strip() for data in data.split(",")]

print(f'[센서 {data[1]}] 상태 {data[2].lower()}, 측정값 {float(data[3]):.2f}')

# <리더님 제출안!>
# data = ' 5, sensor_2, WARNING, 0.78912 '
# parts = data.strip().split(',')
# sid = parts[1].strip()
# atatus = parts[2].strip().lower()
# value = float(parts[3].strip())

# print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")