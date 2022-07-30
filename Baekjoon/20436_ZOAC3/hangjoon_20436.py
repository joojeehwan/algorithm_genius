left_start, right_start = input().split()  # 왼손가락, 오른손가락 시작 위치
target = input()  # 만드려는 문자열

# 쿼터 키보드 좌표
LEFT = {
    'z': (0, 0), 'x': (0, 1), 'c': (0, 2), 'v': (0, 3),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4),
    'q': (2, 0), 'w': (2, 1), 'e': (2, 2), 'r': (2, 3), 't': (2, 4)
}
RIGHT = {
    'b': (0, 4), 'n': (0, 5), 'm': (0, 6),
    'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
    'y': (2, 5), 'u': (2, 6), 'i': (2, 7), 'o': (2, 8), 'p': (2, 9)
}

time = 0
for letter in target:
    if letter in LEFT:
        x1, y1 = LEFT[left_start]  # 손가락 좌표
        x2, y2 = LEFT[letter]  # 목표 키 좌표
        left_start = letter  # 손가락 이동
    else:
        x1, y1 = RIGHT[right_start]  # 손가락 좌표
        x2, y2 = RIGHT[letter]  # 목표 키 좌표
        right_start = letter  # 손가락 이동
    time += abs(x1 - x2) + abs(y1 - y2)  # 택시 거리
    time += 1  # 자 이게 클릭이야

print(time)