import os
import csv



# 파일 입출력
# open()
# 형식: open(파일명, 모드, encoding)
# -모드: r=읽기, w=새로쓰기, a=이어쓰기
# -encoding = 'utf-8'   한글이 깨지지 않도록 하는 것!!!!!!!

FILE = "practice/08_press_13_261029_3.csv"

# f = open(FILE, "r", encoding="utf-8")
# text = f.read()
# print(text)
# f.close()   # 파일을 열고 난 후 닫기까지


# f= open(FILE, "r", encoding = "utf-8")
# lines = f.readlines()
# print(type(lines), len(lines))
# f.close()

# # with open - 블록이 끝나면 자동 닫힘
# with open(FILE,"r",encoding = "utf-8") as f:
#     for line in f:
#         print(line)


# # write()
# with open("practice/test.txt", "w", encoding = "utf-8") as f:
#      f.write("쓰기 테스트")



# print("-----실습2-----")
# with open("practice/test.txt", "w", encoding = "utf-8") as f:
#      f.write("쓰기 테스트")

# o = open("practice/test.txt", "r", encoding = "utf-8")
# p = o.read()
# print(p)
# o.close()

# print("-----실습3-----")
# with open("practice/test.txt", "a", encoding = "utf-8") as f:
#      f.write("\n안녕하세요")

# o = open("practice/test.txt", "r", encoding = "utf-8")
# p = o.read()
# print(p)
# o.close()




# csv reader!
# with open(FILE,"r",encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)




print("-----실습5-----")
with open("practice/08_write.csv", "w", encoding = "utf-8", newline = "") as w:
    write = csv.writer(w)
    write.writerow(["이름", "순서"])
    write.writerow(["펌프", "01"])
with open("practice/08_write.csv", "r", encoding = "utf-8") as w:
    print(w.read())