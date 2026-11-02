# try - except - else - finally
# else - 예외가 하나도 안 났을 때만 실행
# finally - 성공/실패 상관없이 무조건 마지막 실행


# text = "62.5"
# try:
#     temp = flaot(text)
# except ValueError:
#     print("변환 실패")
# else:
#     print("변환 성공:", temp)
# finally:
#     print("종료")
import csv
import os


# print("-----실습1-----")
# f = None
# try:
#     f = open("practice/tessssst.txt", "r", encoding = "utf-8")
#     text = f.read()
#     print(text)
# except FileNotFoundError:
#     print("파일 없음")
# finally:
#     if f is not None:
#       f.close()
#     print("파일 닫힘")



# 실습2
try:
    with open("practice/09_ict_inspection_dirty_15_261102_2.csv",encoding = "utf-8") as f:
        rows = f.readlines()[1:]    # 슬라이싱(해더 빼려고)
except FileNotFoundError:
    rows = []


total = 0
skipped = 0
valid = 0
for line in rows:
    try:
        total += float(line.split(",")[2])  #측정값(2열부터)
        valid += 1
    except (ValueError, IndexError):
        skipped += 1
        continue

print("합계:", total,"유효:", valid,"건너뜀:", skipped)