'''

문제의 예시 이해

bridge_length가 2인것은 다리의 길이가 1인것!
다리를 1만큼 건널 때 1초가 소요되는 것!

즉 그래서
1) 7이 처음에 들어갈때 [0, 7] 1초
2) 그 다음에         [7, 0] 2초

다리라는 배열(스택)이 있다. 길이는 bridge_length만큼!

'''

def solution(bridge_length, weight, truck_weights):
    time = 0

    # 빈 공간을 0으로 표현
    daero = [0] * bridge_length

    while daero:

        daero.pop(0)
        time += 1
        if truck_weights: #대기하는 트럭들이 있다면
            #다리위에 있는 트럭들의 무게합 + 이제 들어오는 트럭의 무게 <= 다리가 버틸수 있는 무게
            # 다리가 버틸 수 있는 무게 인지 체크!
            if sum(daero) + truck_weights[0] <= weight:
                daero.append(truck_weights.pop(0))
            else:
                daero.append(0) #다리의 길이를 유지
    return time