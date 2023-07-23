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

#dic를 활용한, swap 풀이
def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for who in callings:
        idx = result[who] # 호명된 선수의 현재 등수
        result[who] -= 1 # 하나 앞 등수로 바꿔줌 -1
        result[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx-1], players[idx] = players[idx], players[idx-1] # 위치 변경
    return players
