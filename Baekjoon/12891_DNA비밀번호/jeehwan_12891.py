''''

EX) 

임의의 문자열 : "AAACCTGCCAA"
라고 주어졌을 때, 

뽑아야할 문자열의 길이를 4라고 하자. 

A는 1개 이상
C는 1개 이상
G는 1개 이상
T는 0개 이상

"ACCT"는 "G"가 1개 이상 등장해야 한다는 조건을 만족하자 못해 사용X
"GCCA"는 모든 조건을 만족.

=> 항상 순서가 붙어 있는채로 뽑게 된다. 


SO, 계속 1칸씩 이동하면서 조건에 맞는지만 확인하면 된다. 

'''


# 기본적인 슬라이딩 윈도우 개념 (반드시 투 포인터 개념과 같이 정리)

numbers = [1,2,4,-1,-8,29,1]

n = len(numbers)
k = 5

# 하나의 계산 범위 산정, 이 계산 범위가 길이의 변화 없이 끝까지
window = sum(numbers[:k])
answer = window

for i in range(5, n):
    #새롭게 추가되는 다음 인덱스 더하고, 맨 처음번쨰 인덱스 뺴고
    window += (numbers[i] - numbers[i-k])
    answer = max(answer, window)

print(answer)


import sys

input = sys.stdin.readline


s, p = map(int, input().split())

string = input().rstrip()

a, c, g, t = map(int, input().split())

result = 0

#초기 윈도우 값, 조건을 만족 하는 지 확인
start = string[:p]

temp = {"A":0, "C": 0, "G":0, "T":0}

for i in start:
    temp[i] += 1

cnt = 0

if temp["A"] >= a and temp["C"] >= c and temp["G"] >= g and temp["T"] >= t:
    cnt += 1



start_idx = 0
end_idx = start_idx + p


for i in range(len(string) - p):
    # 슬라이딩 윈도우 적용 부분
    temp[string[start_idx + i]] -= 1
    temp[string[end_idx + i]] += 1
    # dict애 string의 인덱스를 변화시켜, temp dict에 해당 알파벳의 value값을 변화시켜
    # 슬라이딩 윈도우 적용
    if temp["A"] >= a and temp["C"] >= c and temp["G"] >= g and temp["T"] >= t:
        cnt += 1

print(cnt)




