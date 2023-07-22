# DFS 코드 형식 탐구





## 조합



### - for문을 활용한 방복

![스크린샷 2023-07-09 오전 3.37.02](/Users/joojeehwan/Desktop/스크린샷 2023-07-09 오전 3.37.02.png)



````python

lst = [1,2,3,4,5]

target = 2

n = len(lst)

answer = []

def dfs1(now_node, candi) :

    if len(candi) == target:
        answer.append(candi[:])
        return

    debug = 1
    # 반복문의 시작이 now_node이고, 나 혹은 나 이후의 것만 본다
    for next_node in range(now_node, n):
			
        candi.append(lst[next_node])
        dfs1(next_node + 1, candi)
        candi.pop()
````



````py
lst = [1,2,3,4,5]

target = 2

n = len(lst)

answer = []

def dfs2(now_node, candi) :

    if len(candi) == target:
        answer.append(candi[:])
        return

    debug = 1
    for next_node in range(now_node, n) :
        dfs2(next_node + 1, candi + [lst[next_node]])
````



### - dfs 자체를 활용한 반복

![스크린샷 2023-07-09 오전 3.39.05](/Users/joojeehwan/Desktop/스크린샷 2023-07-09 오전 3.39.05.png)



````python
lst = [1,2,3,4,5]

target = 2

n = len(lst)

answer = []

def dfs3(lev, cnt, candi) :

    #전체를 다 돌고,
    # 이 코드가 있는 이유?!
    # 해당 코드가 없으면, 인덱스의 끝을 넘는 곳까지 가게 됨. 계속 lev + 1을 증가 시키게 되는데,
    # 전체 범위 인덱스를 초과하면 return 해주거나, 막는 부분이 필요함.
    if lev == n :

        if cnt == target:
        #해당 경우의 수의 요소의 갯수가,내가 찾고자 하는 경우의 수 갯수와 똑같다면,
            answer.append(candi[:])
        return

    debug = 1
    candi.append(lst[lev])
    dfs3(lev + 1, cnt + 1, candi)
    candi.pop()
    dfs3(lev + 1, cnt, candi)
````





````python
lst = [1,2,3,4,5]

target = 2

n = len(lst)

answer = []

def dfs_2(lev, cnt, candi):
    if cnt == target:
         return answer.append(candi[:])

    if lev == n:
         return

    candi.append(lst[lev])
    dfs_2(lev + 1, cnt + 1, candi)
    candi.pop()
    dfs_2(lev + 1, cnt, candi)
````





### 문제 적용

프로그래머스 - 삼총사

````python
def solution(number):
    answer = 0
    n = len(number)
    used = [0] * n

    def nCr(r, start, n, total):
        nonlocal answer
        # 종료파트
        if r <= 0:
            if not total:
                answer += 1
            return

        # 유도파트
        for i in range(start, n):
            total = total + number[i]
            nCr(r-1, i + 1, n, total)
            total = total - number[i]


    nCr(3, 0, n, 0)
    return answer
````



```py
def solution4(number):
    answer = 0
    n = len(number)
    used = [0] * n

    def nCr(r, start, n, total):
        nonlocal answer
        # 종료파트
        if r <= 0:
            if not total:
                answer += 1
            return

        # 유도파트
        for i in range(start, n):
            if not used[i]:
                used[i] = 1
                nCr(r-1, i, n, total + number[i])
                used[i] = 0


    nCr(3, 0, n, 0)
    return answer

```



위의 2코드의 차이?! used 사용의 유무

조합을 구할 땐 굳이 used(기록 배열)을 생성하지 않아도 됨. 

순열을 구할 때, 보통 used배열을 사용함. 



## 순열



````python
# 순열 ver1

lst = [1,2,3,4,5]

target = 2

n = len(lst)

visited = [False] * n

answer = []

def dfs(lev, temp):

    if lev == target:

        answer.append(temp[:])

    #조합과의 가장 큰 차이점.. 모든 것을 다 본다. 그래서 visted 배열로 체킹이 필요 한 것
    # 그래서, 반복문의 시작이 0(시작 인덱스)에서 끝까지
    # dfs를 진입할 떄마다 처음부터 끝까지 다 보는 것
    for next_lev in range(n) :

        if not visited[next_lev] :

            visited[next_lev] = True
            temp.append(lst[next_lev])
            dfs(lev + 1, temp)
            visited[next_lev] = False
            temp.pop()
````





````python
# 순열 ver2 비트마스킹

lst = [1,2,3,4,5]

target = 2

n = len(lst)

answer = []


def dfs_v2(lev, used, temp):

    if lev == target:
        return answer.append(temp[:])

    for i in range(n):

        # i 값을 변화시키면서, used 숫자와의 & 연산을 통해 이용여부를 판단
        # 이용o 1 & 1 = 1 // 이용x 0 & 1 = 0 이렇게
        if used & (1 << i) :
            continue

        temp.append(lst[i])
        dfs_v2(lev + 1, used | (1 << i), temp)
        temp.pop()


dfs_v2(0, 0, [])

print(answer)
````

