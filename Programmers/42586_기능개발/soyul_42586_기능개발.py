def solution(progresses, speeds):

    days = []
    answer = []

    # 앞으로 남은 작업일수를 계산해서 days라는 배열에 넣어줌
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i]:
            days.append((100 - progresses[i])//speeds[i] + 1)
        else:
            days.append((100 - progresses[i])//speeds[i])

    # days가 다 비워질 때까지 스택에서 빼줌
    while days:
        day = days[0]                               # 가장 앞의 작업 일수를 기록
        cnt = 0
        while days and days[0] <= day:              # 스택에 자료가 있고, 앞의 작업 일수보다 적게 걸리는 일이 있으면 한 번에 같이빼줌
            days.pop(0)
            cnt += 1                                # 배포하는 작업의 기능 갯수를 기록했다가 저장
        answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))