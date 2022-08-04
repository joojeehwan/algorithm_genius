def solution(arr):
    answer = []

    # 틀림 바보
    #     for item in arr:

    #         if item in answer:
    #             continue
    #         answer.append(item)

    #     print(answer)

    # 풀이 1
    #     for i in range(len(arr)):

    #         #첫번 째는 무조건 넣자
    #         if i == 0:
    #             answer.append(arr[i])

    #         else:
    #             #연속 적이지 않다면!
    #             if arr[i] != arr[i-1]:
    #                 answer.append(arr[i])

    # 풀이 2
    #     for item in arr:

    #         if len(answer) > 0 and answer[-1] == item:
    #             continue

    #         answer.append(item)

    # 풀이 3
    for item in arr:

        if answer[-1:] == [item]:
            continue

        answer.append(item)
    return answer