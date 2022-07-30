'''

이분 탐색,,!

포인트!

무엇을 이분탐색할지 정하는게 제일 중요하다!



이분 탐색 자체의 알고리즘이 어렵지는 않아!


가장 인접한 두 공유기 사이의 최대 거리!

=> 즉, 공유기 중에서 거리가 가장 가까운게 가장 최대하
되도록!


이분탐색의 대상 : 공유기를 설치할 거리

https://my-coding-notes.tistory.com/119 이 사람 설명잘햇네 이거


'''

import sys

N, C = map(int, sys.stdin.readline().split())
#글자 하나씩 입력받기! N개
house = [int(sys.stdin.readline()) for _ in range(N)]

house.sort()

#공유기 사이의 거리(이분탐색의 대상) 최솟, 최대값 설정!
start = 1

#정렬하고! 가장 끝집이랑 첫번쨰 집 거리 뺴면 나옴
end = house[N-1] - house[0]

#이분탐색 시작

answer = 0

while (start <= end):
    mid = (start + end) // 2 #이분탐색의 대상이 되는,,! 공유기 사이의 거리
    current = house[0] #마지막으로 설치된 공유기의 위치
    cnt = 1

    for i in range(N):
        #현재 집에서 다음집의 거리가 mid를 초과한다?! => 그럼 공유기 설치 가능
        if house[i] - current >= mid:
            #공유기 설치후에 갯수 증가 시키고, current에 최근 공유기 값 저장
            cnt += 1
            current = house[i]

    #공유기의 설치 완료 or 더 많이 되었다?! => 길이를 더 늘려야 한다!

    if cnt >= C:
        answer = mid
        start = mid + 1

    elif cnt < C:
        end = mid - 1

print(answer)
    #공유기 갯수가 더 적게 되었다?! => 길이를 더 적게 해야한다.



