"""
처음엔 자신 기준 진 애들만 list에 추가해서 2개 이상인 애들만 구하려다,
그럼 이겼는데 순위를 못 정하는 경우 1, 2 > 3, 4 > 5 를 못 구해서 2개의 list를 쓰려했으나,
역시 2개 이상이라고 바로 걔네를 set에 집어넣는 순간 순위가 확정난 애도 들어가버려서
정말 고민을 많이 했다.
그리고 경기 순서대로 바로바로 결과가 나와야한다고 생각했다.

하지만 경기를 다 끝내고 나서 결과를 업데이트해서 경기 결과 순서에 따른 차이가 없도록 했고,
set로 중복을 없앴다. 사실 list로 하고 나중에 set처리 해도 되지만...이 아니다.
해보니까 시간초과 난다.ㅎㅎ;;

경기 결과를 다 업데이트 했으면 어차피 선수는 최대 100명이기 때문에 그냥 반복문 한번 더 돌면서
진 사람의 수와 이긴 사람의 수가 n-1(자신 제외)인 경우 순위가 확정이기 때문에 answer를 추가했다.

점수 : 1136 (+13)
"""


def solution(n, results):
    answer = 0
    # index를 이긴 사람
    win = [set() for _ in range(n+1)]
    # index에게 진 사람
    lose = [set() for _ in range(n+1)]

    for winner, loser in results:
        lose[winner].add(loser)
        win[loser].add(winner)

    for player in range(1, n+1):
        # player에게 진 사람에겐, player를 이긴 사람을 추가해준다.
        if lose[player]:
            for loser_me in lose[player]:
                win[loser_me] = win[loser_me].union(win[player])
        # player를 이긴 사람에겐, player에게 진 사람을 추가해준다.
        if win[player]:
            for winner_me in win[player]:
                lose[winner_me] = lose[winner_me].union(lose[player])

    for player in range(1, n+1):
        if len(win[player]) + len(lose[player]) == n-1:
            answer += 1

    return answer


print(solution(8, [[1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7], [6, 8], [7, 8]]))


"""
시간초과
def solution(n, results):
    answer = 0
    # index를 이긴 사람
    win = [[] for _ in range(n+1)]
    # index에게 진 사람
    lose = [[] for _ in range(n+1)]

    for winner, loser in results:
        lose[winner].append(loser)
        win[loser].append(winner)

    for player in range(1, n+1):
        # player에게 진 사람에겐, player를 이긴 사람을 추가해준다.
        if lose[player]:
            for loser_me in lose[player]:
                win[loser_me] += win[player]
        # player를 이긴 사람에겐, player에게 진 사람을 추가해준다.
        if win[player]:
            for winner_me in win[player]:
                lose[winner_me] += lose[player]

    for player in range(1, n+1):
        count = len(set(win[player])) + len(set(lose[player]))
        if count == n-1:
            answer += 1

    return answer
"""