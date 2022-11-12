

#소거 방법
sentence = input()

target = input()

cnt = 0

while target in sentence:

    for i in range(len(sentence)):
        if sentence[i:i+len(target)] == target:
            # 여기서 sentence를 갱신해준다. 그래서 while문이 종료가 되는 것
            # 슬라이스 ':'를 통해서, 뒤에 끝까지 본다. 
            sentence = sentence[i + len(target):]
            break

    cnt += 1
print(cnt)

#위치별 값을 세는 방법

sentence = input()

target = input()

cnt = 0

n = 0

while n <= len(sentence) - len(target) :

    if sentence[n : n+len(target)] == target:
        cnt += 1
        n += len(target)
    else:
        n += 1

print(cnt)


#내장 함수 이용
print(input().count(input()))


# split 함수
word = input()
small = input()
sp_word = word.split(small)

print(len(sp_word) - 1)
