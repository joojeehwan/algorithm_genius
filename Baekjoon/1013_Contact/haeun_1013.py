T = int(input())

for _ in range(T):
    wave = input()
    len_wave = len(wave)
    possible = True
    idx = 0

    while idx < len_wave:
        if wave[idx:idx+2] == "01":
            idx += 2
        else:
            if wave[idx:idx+3] == "100":
                idx += 3
                loop_one = False  # 1000 으로 끝나버리는 경우
                idx_loop = 0  # 0, 1의 반복만큼 한번에 이동

                while idx + idx_loop < len_wave:
                    if wave[idx+idx_loop] == "0":
                        if loop_one:  # 10010 인 경우, 01인지 보기 위해 나감
                            break
                    else:
                        loop_one = True
                    idx_loop += 1
                if not loop_one:  # 100+1+ 이면 1이 한번은 나와야하는데, 끝까지 안나온 경우(1000..0)
                    possible = False
                    break
                else:
                    idx += idx_loop  # idx 한번에 건너뛰기
            else:
                if idx > 4 and wave[idx-2:idx] == "11":  # 10011 이면 뒤에 01 또는 00이 붙을 수 있다.
                    # 이 경우는 01도, 100도 아닌 경우(00) 10011에서 마지막 1부터 다시 보기 위함이다.
                    idx -= 1
                else:
                    # 그것도 아니라면 나가시죠
                    possible = False
                    break

    if possible:
        print("YES")
    else:
        print("NO")
