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
# try:
#     with open("practice/09_ict_inspection_dirty_15_261102_2.csv",encoding = "utf-8") as f:
#         rows = f.readlines()[1:]    # 슬라이싱(해더 빼려고)
# except FileNotFoundError:
#     rows = []


# total = 0
# skipped = 0
# valid = 0
# for line in rows:
#     try:
#         total += float(line.split(",")[2])  #측정값(2열부터)
#         valid += 1
#     except (ValueError, IndexError):
#         skipped += 1
#         continue

# print("합계:", total,"유효:", valid,"건너뜀:", skipped)

# print("-----실습4-=----")
# list_1 = ["practice/09_ict_inspection_15_261102_1.csv",
#           "practice/09_ict_spection_clean.csv",
#           "practice/09_ict_inspection_dirty_15_261102_2.csv"]
# count = 0
# valid = 0
# for x in list_1:
#     try :
#        with open(x, "r", encoding = "utf-8") as f:
#           header_except = f.readlines()[1:]
#           valid += len(header_except)
#           print("읽기 성공: ", x, len(header_except), "개")

#     except FileNotFoundError:
#      print(x,"파일 찾을 수 없음")
#      count +=1
#      continue
# print("총파일 수 :", len(list_1), "처리된 파일 수:", len(list_1)-count, "찾을 수 없는 파일 수:", count)

print("-----실습5-----")
def check_value(text, lo=0.0, hi=5000.0):
    v = float(text)
    return v
for t in ["128.0", "결측", "-999"]:
    try:
        if check_value(t) < 0.0 or check_value(t) > 5000.0:
            raise ValueError("범위 벗어남")
        else:
            print(check_value(t),"- 통과")
    except ValueError as e:
        print(t, "- 제외: :", e)