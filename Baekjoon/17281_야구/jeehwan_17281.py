
'''


- 내가 아는 야구 룰

- 타순은 이닝이 바뀌어도 변하지 x

- 타자와 주자가 함께 이동, 타자 아웃시에 주자 이동 x

- 1번 선수를 4번 타자로 미리 결정  => 4번타자는 미리 결정되어 있다. 1번 선수로


한 야구팀의 감독 아인타는 타순을 정하려고 한다. 아인타 팀의 선수는 총 9명이 있고, 1번부터 9번까지 번호가 매겨져 있다.
아인타는 자신이 가장 좋아하는 선수인 1번 선수를 4번 타자로 미리 결정했다.
이제 다른 선수의 타순을 모두 결정해야 한다.
아인타는 각 선수가 각 이닝에서 어떤 결과를 얻는지 미리 알고 있다. 가장 많은 득점을 하는 타순을 찾고, 그 때의 득점을 구해보자.




풀이

1. permutations를 통해서, 타자들의 가능한 순서를 모두 미리 만듬.

2. 각 순서에 대해서 게임을 끝까지 진행해보고, 그 중 가장 큰 결과값을 정답으로 제출

3. point

    - base정보를 리스트나 다른 자료구조를 사용해 저장하는 것이 아니라, 변수를 사용해 체크

    - 1번 타자가 4번 타자로 고정되어 있다는 문제 조건 => 1번 인덱스 0 을 항상 3번자리에 넣기



0 : 아웃

1 : 안타

2 : 2루타

3 : 3루타

4 : 홈런

'''

#1. itertools 풀이


from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
player = [1, 2, 3, 4, 5, 6, 7, 8]
answer = 0

for permu in permutations(player, 8):

    permu = list(permu)

    #1번타자가 4번타자가 되어야 한다. 1번타자(0번인덱스) 9번타자(8번인덱스)

    permu = permu[:3] + [0] + permu[3:]

    score = 0

    game_idx = 0

    #게임 진행(이닝 시작)
    for ining in range(1, n + 1):

        out_cnt = 0

        #베이스 정보, 배열이 아닌 변수(정수) 값으로 저장
        base1, base2, base3 = 0, 0, 0

        while out_cnt < 3:

            #아웃
            if lst[ining - 1][permu[game_idx]] == 0:
                out_cnt += 1

            #안타
            elif lst[ining - 1][permu[game_idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            #2루타
            elif lst[ining - 1][permu[game_idx]] == 2:
                score += (base3 + base2)
                base1, base2, base3 = 0, 1, base1

            #3루타

            elif lst[ining - 1][permu[game_idx]] == 3:
                score += (base3 + base2 + base1)
                base1, base2, base3 = 0 , 0,  1

            #홈런
            elif lst[ining - 1][permu[game_idx]] == 4 :
                score += (base3 + base2 + base1 + 1)
                base1, base2, base3 = 0 , 0, 0

            game_idx += 1

            #주어진 이니동안은 인덱스가 계속해서 반복해야 함.
            if game_idx == 9:
                game_idx = 0
    answer = max(answer, score)

print(answer)


#2  base를 리스트로 푼 풀이


import sys
import itertools

input = sys.stdin.readline


def calScore(hit_res):
    # return add_score, add_out
    global base_state

    tmp_add_score = 0
    tmp_add_out = 0
    # 아웃
    if hit_res == 0:
        tmp_add_score = 0
        tmp_add_out = -1

        # 1루타
    elif hit_res == 1:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            base_state[1] = False
            base_state[2] = True
        if base_state[0]:
            base_state[0] = False
            base_state[1] = True
        base_state[0] = True

    # 2루타
    elif hit_res == 2:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            tmp_add_score += 1
            base_state[1] = False
        if base_state[0]:
            base_state[0] = False
            base_state[2] = True
        base_state[1] = True

    # 3루타
    elif hit_res == 3:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            tmp_add_score += 1
            base_state[1] = False
        if base_state[0]:
            tmp_add_score += 1
            base_state[0] = False
        base_state[2] = True

    # 홈런
    elif hit_res == 4:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            tmp_add_score += 1
            base_state[1] = False
        if base_state[0]:
            tmp_add_score += 1
            base_state[0] = False
        tmp_add_score += 1

    return tmp_add_score, tmp_add_out


INNING_NUM = int(input())

arr_inning = [list(map(int, input().split())) for _ in range(INNING_NUM)]

ans = 0
# [1,2,3,4,5,6,7,8] # 0 제외 1번놈(0)이 무조건 4번타자니까
for combi in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
    tmp_order = list(combi)
    batter_order = tmp_order[:3] + [0] + tmp_order[3:]
    score_tmp = 0
    batter_num = 0
    for inning in range(INNING_NUM):
        # state_init
        base_state = [False, False, False]
        out_cnt = 3
        # 경기 진행
        while out_cnt:
            this_res = arr_inning[inning][batter_order[batter_num]]
            add_score, add_out = calScore(this_res)
            score_tmp += add_score
            out_cnt += add_out
            batter_num = (batter_num + 1) % 9

    if score_tmp > ans:
        ans = score_tmp

print(ans)




#2. dfs 풀이

"""
17281 ⚾
"""

"""
17281 ⚾
"""
import sys
from itertools import permutations


def dfs1(l: int):
    if l == 3:
        temp.append(0)
        dfs2(4)
        temp.pop()
        return
    for i in range(1, 9):
        if visit[i] is False:
            temp.append(i)
            visit[i] = True
            dfs1(l+1)
            temp.pop()
            visit[i] = False


def dfs2(l: int):
    if l == 9:
        simulation()
        return
    for i in range(1, 9):
        if visit[i] is False:
            temp.append(i)
            visit[i] = True
            dfs2(l+1)
            temp.pop()
            visit[i] = False


def simulation():
    global ans
    score = 0
    turn = 0
    for i in result:
        base1, base2, base3 = 0, 0, 0
        out = 0
        while out != 3:
            if i[temp[turn]] == 0:
                out += 1
            elif i[temp[turn]] == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif i[temp[turn]] == 2:
                score += base2 + base3
                base3 = base1
                base2 = 1
                base1 = 0
            elif i[temp[turn]] == 3:
                score += base1 + base2 + base3
                base3 = 1
                base2 = 0
                base1 = 0
            else:
                score += base1 + base2 + base3 + 1
                base3 = 0
                base2 = 0
                base1 = 0
            turn += 1
            if turn == 9:
                turn = 0
    ans = max(ans, score)


if __name__ == '__main__':
    read = sys.stdin.readline

    ans = 0
    n = int(read())
    result = [list(map(int, read().split())) for _ in range(n)]

    for i in range(1, 9):
        visit = [False] * 9
        visit[i] = True
        temp = [i]
        dfs1(1)
    print(ans)
