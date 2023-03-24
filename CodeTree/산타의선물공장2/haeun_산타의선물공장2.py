"""
Double Linked List 문제
- Node와 Node를 담는 벨트의 정보 저장
- 자꾸 13%에서 틀렸다. KeyError가 발생했다.
- 원인 ) move_all을 할때 m_dst가 아무것도 없었을 경우, 꼬리를 m_src 머리로 했다.
    - m_src가 1개라는 보장도 없는데 왜 이렇게 했는지는 모르겠다.
    - 그런데 이게 왜 key 에러를 유발하는지도 모르겠다. -1이 될 이유는 없는데?
- belt에 선물 index를 다 저장할 경우, remove와 append 때문인지 시간초과가 발생한다.
"""


# 선물 정보
class Present:
    def __init__(self, id, prv=None, nxt=None):
        self.id = id
        self.prv = prv
        self.nxt = nxt

    def __repr__(self):
        return f"{self.id}번 선물의 앞 = {self.prv} 과 뒤 = {self.nxt}"


presents = dict()  # key = id, value = (id, prev, next)

# 벨트 정보
# head와 tail은 벨트의 idx에 해당하는 선물 번호
# belt는 key = 벨트 idx, value = [선물 번호들]
head, tail, belt = [], [], []


def print_belt():
    print("------------ 벨트 출력 -----------------")
    for b in range(1,N+1):
        print(f"{b}번 벨트의 머리 : {head[b]} 와 꼬리 : {tail[b]}, 선물 : {belt[b]}")
        if head[b] != -1:
            node = presents[head[b]]
            while node.nxt is not None:
                print("  ", node)
                node = presents[node.nxt]
            print("  ", node)
        print()
    print()


def build_factory(N, M, belt_nums):
    global head, tail, belt
    head, tail, belt = [-1] * (N+1), [-1] * (N+1), [0] * (N+1)

    rail = [[] for _ in range(N+1)]

    for p in range(M):
        rail[belt_nums[p]].append(p+1)

    # 각 벨트별 선물을 보면서 선물을 만들고 head, tail 설정
    for i in range(1, N+1):
        boxes = rail[i]
        if boxes:  # 선물이 없다면 할 일도 없다.
            count = len(boxes)
            belt[i] = count

            head[i] = boxes[0]
            tail[i] = boxes[-1]
            presents[head[i]] = Present(head[i])
            presents[tail[i]] = Present(tail[i])

            for j in range(count-1):
                presents[boxes[j]] = presents.get(boxes[j], Present(boxes[j]))
                presents[boxes[j]].nxt = boxes[j+1]
                presents[boxes[j+1]] = presents.get(boxes[j+1], Present(boxes[j+1]))
                presents[boxes[j+1]].prv = boxes[j]


# m_src의 모든 물건을 m_dst의 앞으로 옮긴다.
# 출력 : m_dst의 선물 개수
def move_all(m_src, m_dst):
    if belt[m_src]:
        # m_src의 꼬리와 m_dst의 머리가 이어져야한다.
        # 머리가 없다면 이을 것도 없다.
        if head[m_dst] == -1:
            # @@@@@@@@ [디버깅] tail[m_dst] = head[m_src]를 했던게 문제.
            # m_src가 한개란 보장도 없는데 난 왜 이렇게 했을까..?
            tail[m_dst] = tail[m_src]
        else:
            # m_src의 꼬리와 m_dst의 머리가 이어져야한다.
            presents[head[m_dst]].prv = tail[m_src]
            presents[tail[m_src]].nxt = head[m_dst]

        # m_dst의 머리는 m_src의 머리가 된다.
        head[m_dst] = head[m_src]
        # m_dst에 m_src의 모든 선물 개수를 추가한다.
        belt[m_dst] += belt[m_src]
        head[m_src], tail[m_src], belt[m_src] = -1, -1, 0
    return belt[m_dst]


def remove_head(b_num):
    if head[b_num] == -1:
        return -1

    _head = head[b_num]

    if belt[b_num] == 1:
        head[b_num], tail[b_num] = -1, -1
        belt[b_num] = 0
    else:
        head[b_num] = presents[_head].nxt
        # 머리와 그 다음의 연결을 끊는다.
        presents[head[b_num]].prv = None
        presents[_head].nxt = None
        belt[b_num] -= 1

    return _head


def push_head(b_num, new_head):
    if new_head == -1:
        return

    if belt[b_num]:
        now_head = head[b_num]  # 원래 머리는 새 머리 뒤로 갈거임
        presents[new_head].nxt = now_head
        presents[now_head].prv = new_head
        head[b_num] = new_head
        belt[b_num] += 1
    else:
        # 비어있었다면
        head[b_num] = tail[b_num] = new_head
        belt[b_num] = 1


# m_src와 m_dst의 앞 선물만 교체한다.
# 선물이 하나도 없는 벨트가 있다면 그냥 있는 벨트에서 옮기기만 한다.
# 출력 : m_dst의 선물 개수
def change_head(m_src, m_dst):
    # m_src와 m_dst의 head를 받아본다.
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
    before = presents[p_num].prv if presents[p_num].prv is not None else -1
    after = presents[p_num].nxt if presents[p_num].nxt is not None else -1
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
            # print("########## 공장 설립 ##############")
            build_factory(query[1], query[2], query[3:])  # N, M, 벨트 번호
        elif order == 200:  # 물건 모두 옮기기
            # print(f"########## {query[1]}에서 {query[2]}로 물건 모두 앞으로 옮기기 ##############")
            print(move_all(query[1], query[2]))
        elif order == 300:  # 앞 물건만 교체하기
            # print(f"########## {query[1]}과 {query[2]}의 앞 물건만 교체하기 ##############")
            print(change_head(query[1], query[2]))
        elif order == 400:  # 물건 나누기
            # print(f"########## {query[1]}에서 {query[2]}로 물건 나눠서 앞에 옮기기 ##############")
            print(divide_present(query[1], query[2]))
        elif order == 500:  # 선물 정보 얻기
            # print(f"########## {query[1]}번 선물 정보 얻기 ##############")
            print(present_info(query[1]))
        elif order == 600:  # 벨트 정보 얻기
            # print(f"########## {query[1]}번 벨트 정보 얻기 ##############")
            print(belt_info(query[1]))
        # print_belt()

solution()