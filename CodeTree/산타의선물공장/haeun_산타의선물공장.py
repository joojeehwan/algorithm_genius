# import sys
# sys.stdin = open("input.txt", "r")


class Box:
    def __init__(self, id, weight, prev=None, next=None):
        self.id = id
        self.weight = weight
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"[{self.id}번 상자] => 무게 : {self.weight}, prev : {self.prev}, next: {self.next}"


class Belt:
    def __init__(self, id, boxes=None, head=None, tail=None):
        self.id = id
        self.boxes = boxes  # 머리, 꼬리 포함 상자들을 담은 dict
        self.head = head  # 머리 상자의 id
        self.tail = tail  # 꼬리 상자의 id

    def __repr__(self):
        return f"%%% [{self.id}번 벨트] => 머리 : {self.head}, 꼬리 : {self.tail}, 상자 개수 : {len(self.boxes)}"


def print_belts():
    for belt in belts:
        if not work[belt.id]:
            print(f"{belt.id}번 벨트는 고장!")
            continue
        print(belt)
        box = belt.boxes.get(belt.head)
        while box.next is not None:
            print(box)
            box = belt.boxes.get(box.next)
        print(belt.boxes.get(belt.tail))
        print("======================================")


def build_factory(N, M, ids, weights):
    global belts
    belts = [Belt(i) for i in range(M)]

    for b_idx in range(M):
        belt = belts[b_idx]  # 벨트 클래스
        boxes = dict()  # 벨트의 boxes에 할당할, Box 클래스를 담은 dict
        for i_idx in range(N // M):
            now = b_idx * (N // M) + i_idx  # ids, weights를 순회하는 인덱스
            box = Box(ids[now], weights[now])  # Box 클래스에 맞춰 생성
            if i_idx == 0:  # 맨 앞
                belt.head = box.id
            elif i_idx == N / M - 1:  # 맨 뒤
                box.prev = ids[now - 1]
                belt.tail = box.id
            else:  # 머리, 꼬리를 제외한 상자
                box.prev = ids[now - 1]
                box.next = ids[now + 1]
                boxes[ids[now - 1]].next = box.id  # 내 앞 상자의 next는 나다.
            boxes[box.id] = box  # 딕셔너리에 추가!
        belt.boxes = boxes  # 완성된 dict를 Belt 클래스에 할당한다.


def unload_box(w_max):
    unloads = 0  # 하차시킨 아이템의 무게 합
    for b_idx in range(M):
        # 벨트가 고장났으면 넘어간다.
        if not work[b_idx]:
            continue
        belt = belts[b_idx]
        head = belt.boxes.get(belt.head)

        # 뺄게 없는 경우
        if head is None:
            continue

        # 머리를 꺼내는 거니깐 당연히 머리의 앞은 없다.
        after = head.next
        if after is not None:  # 내 뒤가 머리가 된다.
            belt.boxes.get(after).prev = None
            belt.head = after

        # 무게가 w_max 이하인 경우 하차한다.
        if head.weight <= w_max:
            unloads += head.weight
            belt.boxes.pop(head.id)
        # 초과라면 맨 뒤로 보낸다.
        else:
            # 맨 뒤의 next를 나로 바꾼다.
            belt.boxes.get(belt.tail).next = head.id
            # 머리였던 상자의 앞, 뒤를 바꿔준다.
            head.prev = belt.tail
            head.next = None
            # 벨트의 꼬리도 바꿔준다.
            belt.tail = head.id

    print(unloads)


def drop_box(r_id):
    box = None
    belt_idx = -1

    for b_idx in range(M):
        if not work[b_idx]:
            continue
        if belts[b_idx].boxes.get(r_id):
            # r_id 박스가 있는 벨트를 찾았다.
            box = belts[b_idx].boxes.get(r_id)
            belt_idx = b_idx
            break

    if box is None:
        print(-1)
    else:
        print(r_id)
        belt = belts[belt_idx]
        before, after = box.prev, box.next
        if before is not None and after is not None:
            # (앞뒤가 있는 중간의 박스) => 중간의 나만 빼고 앞, 뒤 연결시켜준다.
            belt.boxes.get(before).next = after
            belt.boxes.get(after).prev = before
        elif before is not None and after is None:
            # (뒤가 없는 꼬리 박스) => 뒤가 없어서 r_id-1이 꼬리가 된다.
            belt.boxes.get(before).next = None
            belt.tail = before
        elif before is None and after is not None:
            # (앞이 없는 머리 박스) => 앞이 없어서 뒤가 머리가 된다.
            belt.boxes.get(after).prev = None
            belt.head = after
        belt.boxes.pop(box.id)


def check_box(f_id):
    # 박스를 찾으면 업데이트
    box = None
    belt_idx = -1

    for b_idx in range(M):
        if not work[b_idx]:
            continue
        if belts[b_idx].boxes.get(f_id):
            # f_id 박스를 찾았다.
            box = belts[b_idx].boxes.get(f_id)
            belt_idx = b_idx
            break

    if belt_idx == -1:
        print(-1)
    else:
        belt = belts[belt_idx]
        # 해당 상자 뒤에 있는 모든 상자를 전부 앞으로 가져온다.
        # 순서는 유지되어야 한다.
        # 가장 마지막 상자의 next는 맨 처음이며, 맨 처음 상자의 prev는 가장 마지막이다.
        first, last = belt.boxes.get(belt.head), belt.boxes.get(belt.tail)

        last.next = belt.head
        first.prev = belt.tail

        # 해당 상자 이전 상자의 next는 None이다. (가장 마지막이 된다.)
        before = box.prev
        if before is not None:
            belt.boxes.get(before).next = None
            belt.tail = before
        # 해당 상자(f_id)의 prev는 None이다. (가장 앞이 된다.)
        box.prev = None
        belt.head = f_id
        print(belt_idx + 1)


def break_belt(b_num):
    if not work[b_num]:
        print(-1)
        return

    # 고장 처리
    work[b_num] = False

    for look in range(M):
        next_b = (b_num + look) % M
        # 오른쪽 벨트도 고장났다면 넘어간다.
        if not work[next_b]:
            continue

        belt = belts[b_num]
        next_belt = belts[next_b]

        # 고장난 벨트에 있던 머리의 prev는 오른쪽 벨트의 꼬리다.
        # 오른쪽 벨트의 꼬리의 next는 고장난 벨트의 머리다.
        belt.boxes.get(belt.head).prev = next_belt.tail
        next_belt.boxes.get(next_belt.tail).next = belt.head

        # 오른쪽 벨트의 꼬리를 바꾼다.
        next_belt.tail = belt.tail

        # 옮겨주기
        next_belt.boxes.update(belt.boxes)

        # 고장난 벨트 초기화(사실 불필요)
        belt.head, belt.tail = None, None
        belt.boxes = {}

        print(b_num + 1)
        return


def solution():
    q = int(input())

    for _ in range(q):
        query = list(input().split())
        order = int(query[0])

        if order == 100:  # 공장 설립
            global N, M
            global work
            N, M = int(query[1]), int(query[2])
            work = [True] * M  # 벨트의 고장 여부를 나타낸다.
            build_factory(N, M, list(map(int, query[3:3 + N])), list(map(int, query[3 + N:])))
        elif order == 200:  # 물건 하차
            unload_box(int(query[1]))
        elif order == 300:  # 물건 제거
            drop_box(int(query[1]))
        elif order == 400:  # 물건 확인
            check_box(int(query[1]))
        elif order == 500:  # 벨트 고장
            break_belt(int(query[1]) - 1)
        # print_belts()


solution()
