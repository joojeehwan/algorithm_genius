from collections import defaultdict


def solution(players, callings):
    dic = defaultdict(int)
    for value in callings:
        dic[value] += 1

    for player in players[:]:

        if player in dic.keys():
            index = players.index(player) - dic[player]
            del players[players.index(player)]
            players.insert(index, player)

    answer = players
    return answer