import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('result.txt', 'w')

# Q개의 명령. 1 <= Q <= 100_000
Q = int(input())

# 전역 변수
N = 0  # 선물 갯수. 1 <= N <= 100_000
M = 0  # 벨트 갯수. 1 <= M <= 10

# 벨트 관련 변수
head, tail, broken = [], [], []

# 상자 관련 변수 key = id
prv, nxt, weight, belt = dict(), dict(), dict(), dict()


def print_belts():
    print("^^^^^^^^^^ 벨트 전체 출력 ^^^^^^^^^^")
    for b in range(M):
        print_belt(b+1)
    print("벨트 전체 출력 끝")


def print_belt(b):
    print(f"^^^^^^^^^^ {b}번 벨트 출력 ^^^^^^^^^^")
    print(f"{b}번 => 머리 : {head[b]} & 꼬리 : {tail[b]} & 상태 : {broken[b]}")
    node = head[b]
    while nxt[node] != 0:
        print_box(node)
        node = nxt[node]
    print_box(node)
    print("끝")


def print_box(b):
    print(f"=== {b}번 상자 => 앞 : {prv[b]} || 뒤 : {nxt[b]} || 벨트 : {belt[b]} || 무게 : {weight[b]}")


# 1. 공장 설립
# - M개의 벨트, 각 벨트에 N/M개의 물건 올라감 (물건은 총 N개)
# - 각 물건은(ID, W)로 이루어져있음. ID는 무조건 다름
# 0,1,2 | 3,4,5  | 6,7,8 | 9,10,11
# head[1] = 0, head[2] = 3
# tail[1] = 2, tail[2] = 5
def init_factory(ids, weights):
    # print("111111111111111111111111111")
    global head, tail, broken
    head, tail, broken = [0] * M, [0] * M, [0] * M
    cnt_belt = N // M

    for m in range(M):
        head[m] = ids[m*cnt_belt]
        tail[m] = ids[(m+1)*cnt_belt-1]
        for n in range(cnt_belt):
            now = ids[m*cnt_belt+n]
            belt[now] = m
            weight[now] = weights[m*cnt_belt+n]

            if n == 0:
                nxt[now] = ids[m*cnt_belt+n+1]
            else:
                prv[now] = ids[m*cnt_belt+n-1]
                nxt[prv[now]] = now  # nxt[now] = ids[m*M+n+1] 은 인덱스 에러 발생 가능
        prv[head[m]] = 0
        nxt[tail[m]] = 0


# 2. 물건 하차 (w_max)
# return 하차된 총 무게의 합
# - M개의 벨트를 순서대로 보며, 각 벨트의 "맨 앞에" 있는 물건이
# a) w_max 이하라면 하차. 한 칸씩 앞으로 땡김 => head의 다음이 head가 된다.
# b) 그렇지 않다면 맨 뒤로 보냄 => head의 다음이 head가 되고, head는 tail이 된다.
def unload_box(w_max):
    # print("22222222222222222222")
    total = 0
    for b_idx in range(M):
        if broken[b_idx]:
            continue
        if head[b_idx] == 0:
            continue
        b_head = head[b_idx]
        if weight[b_head] <= w_max:
            total += weight[b_head]
            belt[b_head] = None
            if b_head == tail[b_idx]:
                # 상자가 하나 있던 경우
                head[b_idx] = tail[b_idx] = 0
            else:
                # b_head의 다음이 머리가 된다.
                head[b_idx] = nxt[b_head]
                prv[head[b_idx]] = 0
        else:
            if b_head != tail[b_idx]:
                # 머리를 바꾸고(nxt[head]가 머리가 됨)
                head[b_idx] = nxt[b_head]
                prv[head[b_idx]] = 0

                # 꼬리를 바꾼다(b_head가 꼬리가 됨)
                prv[b_head] = tail[b_idx]
                nxt[tail[b_idx]] = b_head
                tail[b_idx] = b_head
                nxt[b_head] = 0
        # print_belt(b_idx)
    print(total)


# 3. 물건 제거 (r_id)
# return r_id 또는 -1
# - r_id에 해당하는 상자가 놓여있는 벨트가 있다면
# a) 해당 벨트에서 상자 제거, 뒤의 상자들 한칸씩 땡김
# b) 없으면 -1
def remove_box(r_id):
    # print("333333333333333333333")
    b_num = belt.get(r_id)
    if b_num is None:
        print(-1)
    else:
        print(r_id)
        # 해당 벨트에서 상자 제거
        before, after = prv[r_id], nxt[r_id]
        if before == 0 and after != 0:
            # 머리였다면
            head[b_num] = after
            prv[after] = 0
        elif after == 0 and before != 0:
            # 꼬리였다면
            tail[b_num] = before
            nxt[before] = 0
        elif after != 0 and before != 0:
            # 중간에 끼인 애였다면
            nxt[before] = after
            prv[after] = before
        # 관계성 다 끊기
        prv[r_id], nxt[r_id], belt[r_id] = 0, 0, None
        # print_belt(b_num)


# 4. 물건 확인 (f_id)
# return 상자가 있는 벨트 번호 or -1
# - 상자가 있는 경우, 해당 상자의 뒤에 있는 모든 상자를 전부 앞으로 가져옴 (순서 유지)
# => f_id 는 head가 되고, tail의 다음은 원래 head였던 애가 된다. 그리고 tail은 f_id 앞이 된다.
def check_box(f_id):
    # print("444444444444444444")
    if belt.get(f_id) is None:
        print(-1)
    else:
        b_num = belt[f_id]
        print(b_num+1)
        if head[b_num] != f_id:
            # 해당 번호를 포함해 뒤의 모든 것을 앞으로 땡긴다.
            before = prv[f_id]
            original_head = head[b_num]

            # 머리로 설정
            head[b_num] = f_id
            prv[f_id] = 0
            prv[original_head] = tail[b_num]

            # 기존 꼬리 다음은 기존 머리이다.
            nxt[tail[b_num]] = original_head

            # 해당 번호 이전의 값은 꼬리가 된다.
            tail[b_num] = before
            nxt[before] = 0


# 5. 벨트 고장 (b_num)
# return b_num 또는 -1
# b_num의 벨트가 고장나면 다신 쓸 수 없으며, 이미 고장났다면 -1을 반환
# 1. b_num부터 다음 벨트를 순서대로 보며
# 2. 고장나지 않은 최초의 벨트(work)에
# 3. b_num 벨트의 모든 상자를 뒤에 붙인다. => work의 tail에 b_num의 head를 붙이고,
# => work의 tail은 b_num의 tail이 된다.
def broke_belt(b_num):
    b_num -= 1
    if broken[b_num]:
        print(-1)
    else:
        # print("5555555555555555")
        for i in range(1, M):
            next_b = (b_num + i) % M
            # b_num의 모든 상자를 next_b 뒤로 옮긴다.
            if not broken[next_b]:
                print(b_num+1)

                # b_num이 비어있었다면 의미 X
                if head[b_num] == 0 and tail[b_num] == 0:
                    break

                # b_num의 상자 belt번호 변경
                node = head[b_num]
                while nxt[node] != 0:
                    belt[node] = next_b
                    node = nxt[node]
                belt[tail[b_num]] = next_b

                # next_b가 비어있다면 b_num 그대로 옮겨주면 됨
                if head[next_b] == 0 and tail[next_b] == 0:
                    head[next_b], tail[next_b] = head[b_num], tail[b_num]
                else:
                    now_head, now_tail = head[b_num], tail[b_num]
                    next_tail = tail[next_b]  # next_b의 head는 건들일이 없음

                    # next_b의 꼬리와 b_num의 머리를 연결
                    nxt[next_tail] = now_head
                    prv[now_head] = next_tail

                    # next_b의 꼬리 업데이트
                    tail[next_b] = now_tail

                # b_num 처리
                broken[b_num] = 1
                head[b_num], tail[b_num] = 0, 0
                break

def solution():
    for _ in range(Q):
        query = list(map(int, input().split()))
        order = query[0]
        if order == 100:
            # 공장 설립
            global N, M
            N, M = query[1], query[2]
            init_factory(query[3:3+N], query[3+N:])
        elif order == 200:
            # 물건 하차
            unload_box(query[1])
        elif order == 300:
            # 물건 제거
            remove_box(query[1])
        elif order == 400:
            # 물건 확인
            check_box(query[1])
        else:
            # 벨트 고장
            broke_belt(query[1])
        # print(f"{order, query[1]}")
        # print(f"{1}번 => 머리 : {head[1]} & 꼬리 : {tail[1]} & 상태 : {broken[1]}")
        # print_box(123545443)
solution()