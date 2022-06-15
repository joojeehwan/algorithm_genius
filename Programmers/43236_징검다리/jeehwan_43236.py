''''

무엇을 이분탐색할지를 정하는게 제일 중요!


최소 거리를 이분 탐색의 대상으로 삼는다.


제거할 바위의 갯수 : n

바위들이 위치하고 있는 곳 : rocks

distance : 출발지점 부터 도착까지의 거리 

출발은 0이라고 봐야 함
'''


def solution(distance, rocks, n):

    answer = 0
    start, end = 0, distance
    rocks.sort() #일단 징검다리 정렬한다.
    rocks.append(distance) #마지막 도착지랑 거리 계산을 위해서!

    #이분 탐색 시작!

    while start <= end:
        mid = (start + end) // 2 #중간값 => 거리가 mid보다 작으면 x
        gone_stones = 0 #제거한 돌을 카운트
        start_stone = 0 #기준이 되는 돌(시작지점)
        min_distance = float("inf") # 각 mid에서 최솟값을 저장


        for rock in rocks:
            diff = rock - start_stone #바위와 현재 위치 사이의 거리
            if diff < mid: #mid보다 거리가 잛으면 바위 제거
                gone_stones += 1
            else: #mid보다 거리가 길거나 같으면 바위 그대로 둔다
                start_stone = rock #시작위치를 해당 바위로 옮기기
                min_distance = min(min_distance, diff) #최소값 저장! 해당mid단계에서


        #이렇게 반복이 끝나고, 모든 돌들을 확인한 다음에
        #제거한 돌들이 많아지면, 최대거리를 줄이고(왼쪽)! 돌들이 적으면 시작위치를 늘리고(오른쪽)

        if gone_stones > n:
            end = mid - 1

        else:
            answer = min_distance
            start = mid + 1

    return answer