left, right = input().split()
word = input()

keyboard = [['qwert', 'asdfg', 'zxcv'],
            ['yuiop', 'hjkl', 'bnm']]

left_keyboard = 'qwertasdfgzxcv'

cnt = 0

def location(a):                         # 문자열의 위치를 반환
    if a in left_keyboard:                  # 왼쪽 손으로 치는 알파벳이면
        for i in range(3):
            if a in keyboard[0][i]:
                x = i
                break
        for j in range(len(keyboard[0][x])):
            if keyboard[0][x][j] == a:
                y = j
    else:
        for i in range(3):
            if a in keyboard[1][i]:
                x = i
                break
        for j in range(len(keyboard[1][x])):
            if keyboard[1][x][j] == a:
                y = j + len(keyboard[0][x])

    return (x, y)

# 현재 위치
now_left = location(left)
now_right = location(right)

# 위치를 구해가며 계산
answer = len(word)
for i in range(len(word)):
    if word[i] in left_keyboard:
        x, y = location(word[i])
        answer += (abs(now_left[0]-x) + abs(now_left[1]-y))
        now_left = (x, y)
    else:
        x, y = location(word[i])
        answer += (abs(now_right[0] - x) + abs(now_right[1] - y))
        now_right = (x, y)

print(answer)