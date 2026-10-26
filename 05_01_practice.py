# print("-----실습1-----")

# N = 5
# for i in range(1, N+1):
#   print(i)
# for i in range(2, N+1,2):
#   print(i)
# for i in range(N, 0, -1):
#   print(i)

# print("-----실습2-----")
# N = 10
# total = 0
# for i in range(1,N+1):
#     total += i
# print(total) 


# print("-----실습3-----")
# for i in range(2,10):
#     for j in range(2,10):
#       print(i, "x", j ,"=", i*j)    
#     print("---------")



print("-----실습4-----")
N = 5 #측정횟수
total = 0
for i in range(N):
    data = int(input("측정값을 입력하세요: "))  #측정값 : 78 79 90 85 87
    if data > 80:
        total += 1
print(f'초과 개수:{total}')