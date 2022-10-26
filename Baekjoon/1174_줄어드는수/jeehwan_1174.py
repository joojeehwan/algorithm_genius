'''

백준 1174

결론 : 조합으로 전체 가짓수를 모두 구하고, sort, N번째 수를 구하면 된다.



#조합
nums = [1, 2, 3, 4]
num_cnt = len(nums)
combi_list = []
PICK_CNT = 2


def combination_recursive(now_idx, combi):
    if len(combi) == PICK_CNT:
        combi_list.append(combi[:])
        return
    for other_idx in range(now_idx, num_cnt):
        # 자기 다음부터 보기 때문에 사용했는지 확인 안함!!!
        combi.append(nums[other_idx])
        combination_recursive(other_idx+1, combi)
        combi.pop()


combination_recursive(0, [])
print(combi_list)


'''
# lst = [3,1,2,5,6]
# lst.sort()
# print(lst)

# 빠르게 combination 함수로
from itertools import combinations

N = int(input())


nums = [0,1,2,3,4,5,6,7,8,9]
res = []

#몇 자리 자리수를 정해주는 i
for i in range(1, 3):
    for j in combinations(nums, i):
        # reversed 를 통해서 "줄어드는 수"를 표현
        str_nums = list(map(str, reversed(list(j)))) #역으로 바꾸고, 리스트로 안에는 문자열
        res.append(int("".join(str_nums))) #문자로 바꿔서 뭉치고, 다시 숫자로 바꾸기

#오름차순으로
res.sort()
if N > len(res):
    print(-1)

else:
    print(res[N-1])


# dfs로 풀어보기
# dfs를 통해서, 백트래킹을 한다. 왼쪽수가 오른쪽 수보다 커야 하고, 수 number가 비어있다면,
# 값을 그대로, 주거나 출력할 수 있다.
n = int(input())


ans = set()

num = [] #연결하기 위해 숫자를 한자리씩 저장

def dfs():

    if num:
        ans.add(int("".join(map(str, num))))

    for i in range(10):
        if not num or num[-1] > i: #최대 정수 9876543210
            num.append(i)
            dfs()
            num.pop()

dfs() # 모든 경우의 수를 num에 저장

ans = list(ans)
ans.sort()
if n <= len(ans) :
  print(ans[n-1])
else : print(-1)



