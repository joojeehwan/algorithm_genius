if __name__=="__main__":
    N= int(input())

    arr = [[0 for _ in range(0,3)] for i in range(0,N)]
    
    #r g b
    for i in range(0,N):
        arr[i][0],arr[i][1],arr[i][2] = list(map(int,input().split()))

    ans = 0xFFFFFF

    #첫번째 집을 R로 칠했을 때 dp
    #첫번째 집을 G로 칠했을 때 dp
    #첫번째 집을 B로 칠했을 때 dp
    for rgb in range(0, 3):
        # d[a][b] = a번 집을 색 b로 칠했을 때 최소비용
        # 첫 번째 집과 마지막 집이 서로 이웃인 조건이 추가
        dp = [[0xFFFFFF for _ in range(0,3)] for i in range(0,N)]
        
        # 추가
        dp[0][rgb] = arr[0][rgb] #첫번째 구역의 RGB는 첫번째 RGB 값으로 고정

        for i in range(1, N):   
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]  #R -> 이전구역의 min(G,B)
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]  #G -> 이전구역의 min(R,B)
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]  #B -> 이전구역의 min(R,G)
        
        #첫번째 집, 마지막 집에 칠한 색이 다른 경우만
        #ans랑 비교해서 최소비용 값 구하기
        for color in range(0,3):
            if color != rgb:
                ans = min(ans, dp[N-1][color])

    print(ans)