import math


def btf():
    for k1 in range(1, math.floor(math.sqrt(cards)) + 1):
        temp = cards_lst[:]
        cnt = 2 ** k1  # 옮기는 카드 수
        temp = shuffle(cnt, temp)  # 이번 섞기에 포함되는 모든 i 단계
        for k2 in range(1, math.floor(math.sqrt(cards)) + 1):
            temp2 = temp[:]
            cnt = 2 ** k2  # 옮기는 카드 수
            temp2 = shuffle(cnt, temp2)  # 이번 섞기에 포함되는 모든 i 단계
            if temp2 == result:
                return k1, k2
    return 0


def shuffle(cnt, lst):
    new = []
    while cnt > 0:
        back = lst[-cnt:]  # 카드더미의 뒷 부분
        front = lst[:-cnt]  # 카드더미의 앞 부분
        new = back + front + new[len(lst):] # 아래의 카드를 위로 올림
        cnt //= 2  # 나눌 카드 수 갱신
        lst = back  # 나눌 카드더미 갱신
    return new


cards = int(input())  # 전체 카드 수
cards_lst = list(range(1, cards+1))  # 카드 리스트
result = list(map(int, input().split()))  # 섞고난 후 카드 결과
ans = btf()
print(ans[0], ans[1])