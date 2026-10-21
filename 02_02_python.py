# 자료형

count = 3 # int = 정수
temp = 25.5 # float = 실수

ok = True # bool = 불린형
no = False

# type() -> 자료형을 알려줌
print(type(25)) 
print(type("센서 A"))  
print(type(ok))


# 자료형마다 다른 동작
print( 3 + 5 )
print("3" + "5") # 문자열 결합


# 연산자
# - 산술, 비교, 논리 연산자

# 산술 연산자
# 형식: +,-,*,/,//(몫),%(나머지),**(거듭제곱)

# 우선순위
# 괄호 > 거듭제곱 > 곱셈/나눗셈 > 덧셈/뺄셈

# 복합 할당
# 형식: score += 10 -> score = score + 10
score = 100
score += 10
print(score) # 110

# 비교 연산자
# 형식: ==(같다) !=(다르다)
print(5 == 5)
print("정상" == "정상")
print("A" == "a")


# 논리 연산자
#  and - 모두 참 , or - 둘 중 하나, not - 반대
print(True and False) #False
print(True or False)  #True
print(not True)    #False  (True의 반대가 출력)


# 입력 (input)
#  주의) 사용자 입력은 항상 "문자열"
# 형식: 변수 = input("안내문구: ")
name = input("이름: ")
age = input("나이: ")
print(name)