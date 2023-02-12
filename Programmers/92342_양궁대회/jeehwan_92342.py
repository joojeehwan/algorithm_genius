''''

ㄴㅐ가 이걸 풀 었따면 지금 카카오에 갔겠지 ㅋ 재밋네 ㅋ

점수 1점 주네 ㅋ 재밋네 ㅋ

풀이가 다양하니, 다른식으로 풀어보자

결국엔 완전탐색으로 풀어야 한다.


- 비트 마스크 풀이

예전에 비트 마스크 문제를 풀었었는데.. 복기 해보자

백준 1194 - 달이 차오른다 가자


비트형으로 이루어진 모든 경우의 수를 만들고, 이를 전부 다 확인.


ezsw의 유투브 강의 참고
- bit를 이용한 부분집합, 완전 탐색
https://www.youtube.com/watch?v=dzncNbPMiB4


이기기 위해선, 어피치 보다 한발만 더 많이 맞추면 된다.

문제에 주어진 n 보다 더 많이 발사하게 되면, 이를 무시하면 된다. 화살의 개수를 카운팅해야 겟구만


'''


def solution(n, info):
    answer = [0 for _ in range(11)]
    temp = [0 for _ in range(11)]  # 라이언이 쏜 배열을 저장하는 임시 배열 => 원래의 값과 이전 값을 비교해 가면서, 가장 큰 차이로 이기게 되는 값을 찾아간다.
    maxDiff = 0  # 가장 큰 차이로 라이언이 이기게 되는 점수

    for subset in range(1, 1 << 10):

        # subset : 1 - 1023 이를 이진수로 표현해서 , on/off를 표현 할 수 있음.
        # 지금의 subset의 경우는 라이언이 이긴다면 1로 표현아니면 0

        ryan = 0  # 라이언이 획득한 점수
        apeach = 0  # 어피치가 획득한 점수
        cnt = 0  # 라이언이 화살을 쏜 횟수

        # i번쨰 원소가, 이 부분집합에 존재 하는 지 확인
        for i in range(10):
            if subset & (1 << i):
                # 만약에 부분집합에 i번쨰에 값이 있으면 & 연산에 의해서 값이 1이 되니 True가 된다. 즉, 라이언이 이기게 되는 경우

                ryan += 10 - i
                temp[i] = info[i] + 1  # 라이언이 어피치를 이기기 위해서는 어피치 보다 1발만 더 쏘면 된다.
                cnt += temp[i]  # tmp[i] 에는 라이언이 쏘는 화살의 갯수가 담길테니!
            else:
                temp[i] = 0  # 라이언이 점수를 얻어서는 안돼
                if info[i]:  # 근데 어피치는 과녁에 맞춘 적이 있다면,
                    apeach += 10 - i

        if cnt > n:  # 라이언이 발사한 화살이 n보다는 많아지면 안된다.
            continue

        # 라이언의 "0점"에 기록할 화살의 갯수를 카운팅 로직
        temp[10] = n - cnt

        # 그전에 알고 있던 maxDiff 값과 비교

        if ryan - apeach == maxDiff:
            for i in reversed(range(11)):  # 뒤에서 부터 확인해야 하니!

                if temp[i] > answer[i]:  # 낮은 점수를 더 많이 맞춘 경우를 확인해야 하니!
                    maxDiff = ryan - apeach
                    answer = temp[:]
                    break

                elif temp[i] < answer[i]:
                    break

        elif ryan - apeach > maxDiff:

            maxDiff = ryan - apeach
            answer = temp[:]  # 정답에 temp 배열을 복사해서 넣어준다.

    # 라이언이 못이기는 경우도 있기에! 계속 maxDiff가 0 이라면,
    if maxDiff == 0:
        answer = [-1]

    return answer


'''

중복조합 풀이,


'''

from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_gap = -1  # 점수 차

    for combi in combinations_with_replacement(range(11), n):  # 중복 조합으로 0~10점까지 n개 뽑기
        info2 = [0] * 11  # 라이언의 과녁 점수

        for i in combi:  # combi에 해당하는 화살들을 라이언 과녁 점수에 넣기
            info2[10 - i] += 1

        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == info2[idx] == 0:  # 라이언과 어피치 모두 한번도 화살을 맞히지 못한 경우
                continue
            elif info[idx] >= info2[idx]:  # 어피치가 라이언이 쏜 화살의 수 이상을 맞힌 경우
                apeach += 10 - idx
            else:  # 라이언이 어피치보다 많은 수의 화살을 맞힌 경우
                lion += 10 - idx

        if lion > apeach:  # 라이언이 점수가 더 높은 경우
            gap = lion - apeach  # 점수 차
            if gap > max_gap:  # 기존보다 더 큰 점수 차인 경우
                max_gap = gap
                answer = info2
    return answer



'''
dfs 
풀이
https://unie2.tistory.com/1081?category=935213
'''


from copy import deepcopy

max_diff = 0
answer = []

def dfs(info, shoot, n, i) :
    global answer, max_diff
    if i == 11 :
        if n != 0 :
            shoot[10] = n
        score_diff = calcDiff(info, shoot)
        if score_diff <= 0 :
            return
        result = deepcopy(shoot)
        if score_diff > max_diff :
            max_diff = score_diff
            answer = [result]
            return

        if score_diff == max_diff :
            answer.append(result)
        return

    # 점수 먹는 경우
    if info[i] < n :
        shoot.append(info[i] + 1)
        dfs(info, shoot, n-info[i]-1, i + 1)
        shoot.pop()

    # 점수 안먹는 경우
    shoot.append(0)
    dfs(info, shoot, n, i + 1)
    shoot.pop()

def calcDiff(info, shoot) :
    enemyScore, myScore = 0, 0
    for i in range(11) :
        if (info[i], shoot[i]) == (0, 0) :
            continue
        if info[i] >= shoot[i] :
            enemyScore += (10 - i)
        else :
            myScore += (10 - i)

    return myScore - enemyScore


def solution(n, info) :
    global answer, max_diff
    dfs(info, [], n, 0)
    if answer == [] :
        return [-1]

    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]