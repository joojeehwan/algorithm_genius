import re

T = int(input())
pattern = re.compile('(100+1+|01)+')        # 정규표현식

for _ in range(T):
    wave = input()
    is_match = pattern.fullmatch(wave)          # 매치되는지 확인 아닐시 None 반환
    if is_match:
        print('YES')
    else:
        print('NO')