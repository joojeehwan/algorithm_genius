n = int(input()) #전체 문자열의 갯수
s = input() #문자열을 통한 덧셈 풀이
sum = 0
for i in range(n) :
    sum += ord(s[i]) - ord('0')

print(sum)