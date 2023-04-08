"""
Double Linked List 문제
- prv, nxt 배열을 활용해 앞, 뒤를 저장한다.
- class를 만들어서 정보를 저장한 코드와 메모리가 59MB VS 126MB이다.
- 쓸데없이 class를 만들지 말아야겠다고 생각했다. key 에러도 힘들다.
"""

# 선물 정보
prv, nxt = [], []

# 벨트 정보
# head와 tail은 벨트의 idx에 해당하는 선물 번호, belt는 선물 갯수
head, tail, belt = [], [], []


def build_factory(N, M, belt_nums):
    global head, tail, belt, prv, nxt
    head, tail, belt = [-1] * (N+1), [-1] * (N+1), [0] * (N+1)
    prv, nxt = [-1] * (M+1), [-1] * (M+1)

    rail = [[] for _ in range(N+1)]  # 각 벨트 별 선물 번호 저장

    for p in range(M):
        rail[belt_nums[p]].append(p+1)

    # 각 벨트별 선물을 보면서 선물을 만들고 head, tail 설정
    for i in range(1, N+1):
        items = rail[i]
        if items:  # 선물이 없다면 할 일도 없다.
            head[i] = items[0]
            tail[i] = items[-1]

            belt[i] = len(items)  # 선물 개수 저장

            # prv, next 설정
            for j in range(belt[i]-1):
                nxt[items[j]] = items[j+1]
                prv[items[j+1]] = items[j]


# m_src의 모든 물건을 m_dst의 앞으로 옮긴다.
# 출력 : m_dst의 선물 개수
def move_all(m_src, m_dst):
    # m_src에 아무것도 없다면 옮길게 없다.
    if belt[m_src] > 0:
        # m_dst에 아무것도 없다면 head, tail을 그대로 옮긴다.
        if belt[m_dst] == 0:
            head[m_dst], tail[m_dst] = head[m_src], tail[m_src]
        else:
            # m_src의 꼬리와 m_dst의 머리가 이어져야한다.
            prv[head[m_dst]] = tail[m_src]
            nxt[tail[m_src]] = head[m_dst]

            # m_dst의 머리는 m_src의 머리가 된다.
            head[m_dst] = head[m_src]

        belt[m_dst] += belt[m_src]
        head[m_src], tail[m_src], belt[m_src] = -1, -1, 0
    return belt[m_dst]


# 떼어낸 머리의 번호를 반환한다.
def remove_head(b_num):
    if head[b_num] == -1:
        return -1

    # m_src의 머리를 제거한다.
    origin_head = head[b_num]
    if belt[b_num] == 1:
        # 한 개밖에 없다면 머리와 꼬리는 사라진다.
        head[b_num] = tail[b_num] = -1
        belt[b_num] = 0
    else:
        # 아니라면 머리의 다음을 머리로 땡겨온다.
        head[b_num] = nxt[origin_head]
        # 원래 머리의 nxt를 끊고, 새 머리의 prv도 끊는다.
        nxt[origin_head] = prv[head[b_num]] = -1
        belt[b_num] -= 1

    return origin_head


# 반환 X. 머리를 집어 넣는다.
def push_head(b_num, new_head):
    if new_head == -1:
        return
    if belt[b_num] == 0:
        # 비어있었다면, 이제 얘가 유일하다.
        head[b_num] = tail[b_num] = new_head
        belt[b_num] = 1
    else:
        # 아니라면, 머리만 바뀐다.
        now_head = head[b_num]
        head[b_num] = new_head  # 떼어낸 머리 가져와서 쓰는 것
        nxt[new_head] = now_head  # 그 머리의 다음은 dst의 현재 머리
        prv[now_head] = new_head  # dst 현재 머리의 앞은 새로 가져온 머리
        belt[b_num] += 1


# m_src와 m_dst의 앞 선물만 교체한다.
# 선물이 하나도 없는 벨트가 있다면 그냥 있는 벨트에서 옮기기만 한다.
# 출력 : m_dst의 선물 개수
def change_head(m_src, m_dst):

    # m_src와 m_dst의 head를 떼낸다.
    src_head = remove_head(m_src)
    dst_head = remove_head(m_dst)

    push_head(m_src, dst_head)
    push_head(m_dst, src_head)

    return belt[m_dst]


# m_src의 앞에서 N // 2개 까지의 선물을 m_dst 앞으로 옮긴다.
# m_src에 한개밖에 없다면 옮기지 않는다.
# 출력 : m_dst의 선물 개수
def divide_present(m_src, m_dst):
    count = belt[m_src]

    to_dst = []
    for _ in range(count//2):
        to_dst.append(remove_head(m_src))

    for i in range(len(to_dst)-1, -1, -1):
        push_head(m_dst, to_dst[i])

    return belt[m_dst]


# p_num번호 선물의 앞, 뒤를 출력하는데 없는 건 -1로 치환한다.
# 출력 : 해당 선물의 앞 id + 뒤 id * 2
def present_info(p_num):
    before = prv[p_num] if prv[p_num] != -1 else -1
    after = nxt[p_num] if nxt[p_num] != -1 else -1
    return before + after * 2


# b_num번호 벨트의 머리, 꼬리, 선물의 개수를 출력하는데 없으면 머리, 꼬리는 -1로 치환한다.
# 출력 : 머리 + 꼬리 * 2 + 선물 * 3
def belt_info(b_num):
    return head[b_num] + tail[b_num] * 2 + belt[b_num] * 3


def solution():
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        order = query[0]
        if order == 100:  # 공장 설립
            global N
            N = query[1]
            build_factory(query[1], query[2], query[3:])  # N, M, 벨트 번호
        elif order == 200:  # 물건 모두 옮기기
            print(move_all(query[1], query[2]))
        elif order == 300:  # 앞 물건만 교체하기
            print(change_head(query[1], query[2]))
        elif order == 400:  # 물건 나누기
            print(divide_present(query[1], query[2]))
        elif order == 500:  # 선물 정보 얻기
            print(present_info(query[1]))
        elif order == 600:  # 벨트 정보 얻기
            print(belt_info(query[1]))

solution()
