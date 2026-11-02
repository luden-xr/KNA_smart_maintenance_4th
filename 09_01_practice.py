# print("-----실습1-----")
# print("-----실습2-----")
# temp = input("온도값: ")
# try:
#     temp_v = int(temp)
#     print(f'{temp_v}도')
# except:
#     print("숫자만 입력하세요")
# print("프로그램이 계속 진행됩니다.")


print("-----실습3-----")
data = input("측정값: ")

try:
    data_input = int(data)
    result = 100 / data_input
    print(result)
except ValueError:
    print("숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")

