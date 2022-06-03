T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    pre_hex = input()
    edge = N // 4  # 한 변에 있는 숫자의 개수
    hex_set = set()  # 회전시킨 한 변의 16진수 담을 set(중복제거)

    # 회전할 횟수 => 한 변에 있는 숫자가 3개라면 2번까지 회전하는게 의미있다.
    for _ in range(edge):
        # 정사각형이므로 네 변을 한번씩 거쳐야함
        for i in range(4):
            hex_set.add(pre_hex[i*edge:(i+1)*edge])
        # 제일 마지막에 있는 문자를 앞으로 땡겨온다.
        pre_hex = pre_hex[-1] + pre_hex[:N-1]

    # 다 돌았다면 16진수를 10진수로 다 바꿔준다.
    hex_list = []
    for hex in hex_set:
        hex_to_int = 0

        for i in range(edge):
            try:
                # 숫자면
                num = int(hex[i])
            except:
                # A ~ F 사이면
                num = ord(hex[i]) - 55
            # 현재 숫자 * 16진수 몇 번째 자리인지
            hex_to_int += num * 16 ** (edge - 1 - i)
        hex_list.append(hex_to_int)
    # 정렬
    hex_list.sort()
    print(f"#{tc+1} {hex_list[-K]}")