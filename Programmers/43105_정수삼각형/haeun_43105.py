"""
못품
https://programmers.co.kr/questions/26843
ㅠㅠㅠ
계산된 결과값들을 다 살려서 가져가야한다고 생각하다 시간초과 맞았다.
"""
def solution(triangle):
    triangle_height = len(triangle)

    dp = [[0]*triangle_height for _ in range(triangle_height)]
    dp[0][0] = triangle[0][0]

    for height in range(triangle_height-1):
        triangle_num_cnt = len(triangle[height])
        for triangle_idx in range(triangle_num_cnt):
            # 왼쪽 아래 (왼쪽부터 계산해와서 이미 있는 값과, 이번에 새로 구하는 값 비교)
            dp[height+1][triangle_idx] = max(dp[height+1][triangle_idx], dp[height][triangle_idx] + triangle[height+1][triangle_idx])
            # 오른쪽 아래 (똑같음)
            dp[height+1][triangle_idx+1] = max(dp[height+1][triangle_idx+1], dp[height][triangle_idx] + triangle[height+1][triangle_idx+1])

    return max(dp[triangle_height-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
