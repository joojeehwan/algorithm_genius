n = int(input()) #전체 문자열의 갯수
s = input() #문자열을 통한 덧셈 풀이
sum = 0
for i in range(n) :
    sum += ord(s[i]) - ord('0')

print(sum)
'''
아스키 코드를 활용한 풀이 
ord('9') - ord('0') = 9
ord('8') - ord('0') = 8
.
.
.
.
ord('0') - ord('0') = 0
> 이 풀이는 숫자가 0~9일 때만 유효
'''
