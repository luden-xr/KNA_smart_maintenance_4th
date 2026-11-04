import numpy as np

# temp = np.array([70,71,72])
# print(temp)

# print(temp + 2 )

# # 튜븦로 배열 만들기
# print(np.array((1,2,3)))   #[1,2,3]

# print("-----실습1-----")
# temp = np.array([32,18,35,84,98])
# print(temp)
# temp_v = 1.8*temp+32
# print(np.round(temp_v, 2))

# print([f'섭씨{x}도' for x in temp])
# print([f'화씨{round(x,1)}도' for x in temp_v])

# print("-----실습2-----")
# electro_flow = np.linspace(0,70,8)
# print(electro_flow)

# print("-----실습3-----")
# data = np.arange(0,40,5)
# print(data)

# print("-----실습4-----")
# data =np.array([[42,2], [38,6], [40,3], [31,8]])
# demension_n = data.ndim
# shape = data.shape
# sz = data.size
# type = data.dtype
# print(f'차원:{demension_n} / 형태:{shape} / 개수:{sz} / 형식:{type}')

# print("-----실습5-----")
# data = np.array([2.5, 5.6, 5.4, 18.69])
# dt = data.dtype
# type_shift = data.astype(int)
# print(data)
# print(type_shift)

print("-----실습6-----")
data = np.array([30, 15.44, 4603,30,18.69,4603, 30, 62.48, 4967,
                 30,18.37, 4603])
table = data.reshape(3,4)
print(table)
print(data.flatten())

