'''

개미굴 - 트리


문제 풀기 전 트라이 공부

https://velog.io/@gojaegaebal/210126-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%8050%EC%9D%BC%EC%B0%A8-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0feat.-Class

예제 입력

3
2 B A
4 A B C D
2 A C


예제 출력

A

--B

----C

------D

--C

B

--A



'''

from collections import defaultdict

# dict 풀이 -> 결국엔 트라이의 구조

def makeTree(dic, arr):
    if len(arr) == 0:
        return

    # defaultdict를 사용하면 굳이 적어도 되지 않는 코드
    if arr[0] not in dic:
        dic[arr[0]] = {}

    debug = 1

    # 슬라이싱을 통해 [1:] 을 통해서, 하나씩 앞에서 걸러지는 효과 발생
    makeTree(dic[arr[0]], arr[1:])


n = int(input())

lsts = [list(map(str, input().split())) for _ in range(n)]

dic = {}

# 딕셔너리를 선언 후 , 맨 앞의 숫자만 빼놓고(갯수) 트리 형태 처럼 계층을 가지게끔 정의 함수를 사용해, 재귀적으로 반복


for lst in lsts:
    lst = lst[1:]  # 슬라이스를 활용해, 맨앞의 숫자는 제외

    makeTree(dic, lst)

print(dic)

