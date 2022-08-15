def dfs(r, c, sn, en, q_size):
    if q_size == 0:
        return sn
    else:
        if r < q_size ** 0.5: # 북쪽
            if c < q_size ** 0.5: # 북서쪽
                # print('up left')
                return dfs(r, c, sn, en - q_size * 3, q_size//4)
            else: # 북동쪽
                # print('up right')
                return dfs(r, c - q_size ** 0.5, sn + q_size, en - q_size * 2, q_size//4)
        else: # 남쪽
            if c < q_size ** 0.5: # 남서쪽
                # print('down left')
                return dfs(r - q_size ** 0.5, c, sn + q_size * 2, en - q_size * 1, q_size//4)
            else: # 남동쪽
                # print('down right')
                return dfs(r - q_size ** 0.5, c - q_size ** 0.5, sn + q_size * 3, en, q_size//4)


# 입력값
# 2**n = 정사각형의 가로, 세로
n, r, c = map(int, input().split())

# start_num
sn = 0
# end_num
en = (2**n)**2 - 1

# dfs
ans = dfs(r, c, sn, en, (2**(n-1))**2)
print(ans)