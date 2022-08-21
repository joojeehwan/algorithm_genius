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
