# 31분 54초

def adjacent(a, b):
    if magnets[a][(tops[a]+2) % 8] != magnets[b][(tops[b]+6) % 8]:
        return True
    else:
        return False


def see_left(l, r, c):
    if adjacent(l, r):
        if l >= 1:
            see_left(l-1, l, -c)
        tops[l] = (tops[l] + c) % 8


def see_right(l, r, c):
    if adjacent(l, r):
        if r <= 2:
            see_right(r, r+1, -c)
        tops[r] = (tops[r] + c) % 8


for t in range(1, int(input()) + 1):
    k = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    tops = [0] * 4
    scores = [1, 2, 4, 8]

    # top
    # magnets[n][tops[n]]
    # adjacent(now and right)
    # magnets[n][(tops[n]+2)%8] <-> magnets[n+1][(tops[n+1]+6)%8]
    # adjacent(now and left)
    # magnets[n-1][(tops[n-1]+2)%8] <-> magnets[n][(tops[n]+6)%8]
    rotations = [tuple(map(int, input().split())) for _ in range(k)]
    score = 0
    for which, clock in rotations:
        which -= 1
        if which >= 1:
            see_left(which-1, which, clock)
        if which <= 2:
            see_right(which, which+1, clock)
        tops[which] = (tops[which] - clock) % 8
    for i in range(4):
        score += scores[i] * magnets[i][tops[i]]

    print(f'#{t} {score}')