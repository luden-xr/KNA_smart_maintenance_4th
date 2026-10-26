# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식: 문자열[번호]   (첫 글자 = 0번)

word = 'PYTHON'
print(word[0], word[2], word[5])

# 음수 인덱스: 뒤에서부터!
print(word[-1], word[-2])  #N, O

print(word[6])  #ERROR!!
