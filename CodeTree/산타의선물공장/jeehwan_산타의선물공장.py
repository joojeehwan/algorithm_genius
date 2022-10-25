'''



예로 <Figure 5>에서 b_num이 3인 명령이 주어졌다면 3번째 벨트는 망가지며,
3번 벨트 위에 있던 모든 상자가 1번 벨트 위로 순서대로 올라가게 됩니다.
이 명령을 수행하기 전 만약 b_num 벨트가 이미 망가져 있었다면 -1을,
그렇지 않았다면 정상적으로 고장을 처리했다는 뜻으로 b_num 값을 출력합니다.

=> sss이게 무슨 뜻이지?! b_num이 중복되게 나올 수도?!

q개의 명령에 따라 일을 진행

m개의 벨트를 설치

n개의 물건을 준비하고,

각 벨트위에는 n/m 개의 물건들이 놓인다.
'''


from collections import defaultdict

# 일단 해설 이거 원래 기본적인 함수 세팅 있었던거 같은데, 여긴 없구먼


MAX_M = 10



#변수 선언

n, m, q = -1, -1, -1

# 각 id 별로 상자의 무게를 저장

weight = {}

# id에 해당하는 상자의 nxt값과 prv값을 관리 , 0이면 없다

prev, next = defaultdict(int), defaultdict(int)


#각 벨트별 head와 tail id를 관리.
head = [0] * MAX_M
tail = [0] * MAX_M


#벨트가 망가졌는지를 표시
broken = [False] * MAX_M


# 물건 별로 벨트 번호를 기입
# 벨트 번호가 -1 이면 사라진 것?!
# 망가지면, 앞으로 사용안하니 사라졋다고 표현

belt_num = defaultdict(lambda : -1)


# 1. 공장 설립
def build_factory(elems):

    #공장 정보 입력받기
    n, m = elems[1], elems[2]
    ids, ws = elements[3:3 + n], elems[3 + n : 3 + n + n]


    # id 마다 무게를 관리하기
    for i in range(n):
        #이건 dict에 단순히 담는 작업, key 여부를 굳이 판독할 필요 x
        weight[ids[i]] = ws[i]

    # 벨트 별로 상자 목록을 넣어주기

    size = n // m
    for i in range(m):
        #head와 tail설정하기
        # 아 이렇게 곱하는 형식으로 각각의 테이블 마다 나눌 수 있구나
        head[i] = ids[i * size]
        tail[i] = ids[(i + 1) * size - 1]

        # 아래 for 문 쉽게 생각하면, size 만큼 반복돈다고 생각
        # 상자 id마다 현재 지금 어느 벨트에 있는지 위치를 기록
        for j in range(i * size, (i + 1) * size):
            belt_num[ids[j]] = i

            # next, prev를 설정하기
            # 와 이렇게 각 배열의 인덱스마다 앞뒤가 뭔지 기록하기
            if j <(i + 1) * size - 1:
                next[ids[j]] = ids[j + 1]
                prev[ids[j + 1]] = ids[j]

# id에 해당하는 상자를 삭제
def remove_id(_id, remove_belt):
    b_num = belt_num[_id]

    #remove_belt는 boolean값이 들어와서 하차 여부를 결정하게 된다.
    #벨트 번호르 제거 해주기

    if remove_belt:
        belt_num[_id] = -1

    # 하나 남은 원소라면
    # head, tail이 사라지고 끝난다.
    # 머리와 꼬리가 같다?! 여기엔 서로 다른 id 값만 들어가는데?! 이건 원소가 하나 밖에 없다는 뜻 뿐
    if head[b_num] == tail[b_num]:
        head[b_num] = tail[b_num] =  0

    # 삭제 되는게 head 라면
    # head만 변경되고 끝난다.
    elif _id == head[b_num] :
        #원래 기존의 head 다음에 있던 것을
        nid = next[_id]
        # 이제 그것이 head가 되고
        head[b_num] = nid
        # head보다 앞서는 것은 없으니
        prev[nid] = 0

    # 삭제 되는게 tail이라면
    # tail만 변경되고 끝나기
    elif _id == tail[b_num]:
        #원래 기존의 tail보다 앞에 있는 것을
        pid = prev[_id]
        #이제 그것이 tail이 되고
        tail[b_num] = pid
        # tail보다 뒤에 있는 건 있을 수 없으니
        next[pid] = 0

    # 중간에 있는 것들, (head, tail 제외) => 이 부분 이해가 안되는 구먼
    # 중간이 사라지니, 그 중간을 제외한 앞 뒤로, 그 둘의 관계를 재 설정한것

    else :
        pid, nid = prev[_id], next[_id]
        next[pid] = nid
        prev[nid] = pid
    '''
    0
    0 이것과
    0 (이게 사라짐)
    0 이것의 관계를 다시 prev와 next로 재 설정 한것   
    '''
    #삭제가 되니깐, 지원지는 id에 대한 앞 뒤는 없을꺼자나?! 기록의 의미가 없자나
    next[_id] = prev[_id] = 0


# target id 바로 뒤에 id를 추가

def push_id(target_id, _id):
    next[target_id] = _id
    prev[_id] = target_id

    # 만약에 target_id가 tail이었다면
    # tail을 변경해주기
    # 그치! 뒤에 바로 추가 해버리는데! tail 뒤로 가게 되면 그게 바로 tail이 되는거지
    b_num = belt_num[target_id]
    if tail[b_num] == target_id:
        tail[b_num] = _id

# 2. 물건 하차
def drop_off(elems):
    w_max = elems[1]

    # 각 벨트마다 보며
    # 첫 번쨰 상자를 열어본다. 벨트의 맨 앞에 있는 상자를
    w_sum = 0

    for i in range(m):

        # 망가진 벨트라면, 넘어간다.
        if broken[i] :
            continue

        # 벨트의 head를 확인! 가장 맨 앞에 있는 상자를 열어봐야 하니깐!

        if head[i] != 0 : #head가 존재
            _id = head[i] # 맨앞에 있는 박스의 id 할당
            w = weight[_id] # 맨앞에 있는 박스의 무게 할당

            # 가장 앞에 있는 상자의 무게가 w_max 이하라면, 하차 시키고 답에 더해주기
            if w < w_max:
                w_sum += w

                # 하차를 진행하기
                remove_id(_id, True)

            # 만약에, 그 무게가 w_max를 넘게 된다며 하차를 시키지 않고, 그냥 벨트 맨뒤로만 보낸다.
            # next에 있는 상자가 있다. 나 보다 앞에 있는 상자가 있다.
            elif next[_id] != 0:

                # 상자를 지우기는 한되, 하차는 하지 않는...!
                # 왜 이렇게 되냐?! remove_id에서 인자인 False가 쓰이는 부분은
                # belt_num은 각 상자의 id 별로 어떤 벨트에 있는지를 기록하는 것
                # 근데 True가 되버리면, 벨트에서 완전히 사라지는 꼴이 되는거라..! 하지만 이건 그냥 이동만!
                remove_id(_id, False)
                #맨뒤에 해당 값을 바로 push 해주기
                push_id(tail[i], _id)

    print(w_sum)

# 3. 물건 제거
def remove(elems):
    r_id = elems[1]

    # 이미 삭제된 상자라면, -1을 출력하고 패스하기
    if belt_num[r_id] == -1 :
        print(-1)
        return

    #상자 삭제
    remove_id(r_id, True)
    print(r_id)

# 4. 물건 확인
def find(elems):

    f_id = elems[1]
    # 이미 삭제된 상자라면 -1을 출력하고 패스
    if belt_num[f_id] == -1:
        print(-1)
        return

    #해당 상자를 찾아 이를 맨앞으로만..! 가장 head로!, 이는 그렇다면, head가 아닌 경우에만 유효하겟지..!?

    b_num = belt_num[f_id]

    if head[b_num] != f_id : #지금 내가 보는 상자가, head가 아닌 경우에만!
        orig_tail = tail[b_num]
        orig_head = head[b_num]

        # 새롭게 다시 tail을 갱신 // 순서는 그대로 유지인것을 놓치면 안된다..!

        now_tail = prev[f_id]
        tail[b_num] = now_tail
        next[now_tail] = 0

        #기존의 tail next를 head로, head의 prev를 기존 tail로
        next[orig_tail] = orig_head
        next[orig_head] = orig_tail

        #새로 head를 지정
        head[b_num] = f_id


    print(b_num + 1)
# 5. 벨트 고장
def broken_belt(elems):
    b_num = elems[1]
    b_num -= 1

    # 이미 망가져 있다면
    # -1을 출력하고 패스합니다.
    if broken[b_num]:
        print(-1)
        return

    broken[b_num] = 1

    # 만약 빈 벨트라면 패스합니다.
    if head[b_num] == 0:
        print(b_num + 1)
        return

    # 오른쪽으로 돌면서
    # 아직 망가지지 않은 벨트 위로 상자를 전부 옮겨줍니다.
    nxt_num = b_num
    while True:
        nxt_num = (nxt_num + 1) % m
        # 최초로 망가지지 않은 곳이 보이면
        if not broken[nxt_num]:
            # 만약 해당 벨트가 비어있다면
            # 그대로 옮겨줍니다.
            if tail[nxt_num] == 0:
                head[nxt_num] = head[b_num]
                tail[nxt_num] = tail[b_num]
            else:
                # 해당 위치로 상자를 전부 옮겨줍니다.
                # head만 tail뒤에 붙여준 뒤
                push_id(tail[nxt_num], head[b_num])
                # tail만 갈아껴주면 됩니다.
                tail[nxt_num] = tail[b_num]

            # head부터 tail까지 보며
            # belt_num을 갱신해줍니다.
            _id = head[b_num]
            while _id != 0:
                belt_num[_id] = nxt_num
                _id = nxt[_id]

            head[b_num] = tail[b_num] = 0
            break

    print(b_num + 1)


# 입력 받기

q = int(input())

for _ in range(q):
    elements = list(map(int, input().split()))
    kind = elements[0]

    if kind == 100 :
        build_factory(elements)

    elif kind == 200:
        drop_off(elements)

    elif kind == 300:
        remove(elements)

    elif kind == 400:
        find(elements)

    else:
        broken_belt(elements)


'''



예로 <Figure 5>에서 b_num이 3인 명령이 주어졌다면 3번째 벨트는 망가지며,
3번 벨트 위에 있던 모든 상자가 1번 벨트 위로 순서대로 올라가게 됩니다.
이 명령을 수행하기 전 만약 b_num 벨트가 이미 망가져 있었다면 -1을,
그렇지 않았다면 정상적으로 고장을 처리했다는 뜻으로 b_num 값을 출력합니다.


이게 무슨 뜻이지?!

b_num이 중복되게 나올 수도?!


'''

'''
# 일단 해설 이거 원래 기본적인 함수 세팅 있었던거 같은데, 여긴 없구먼

from collections import defaultdict

MAX_M = 10

# 변수 선언
n, m, q = -1, -1, -1

# 각 id별로 상자 무게를 저장합니다.
weight = {}

# id에 해당하는 상자의 nxt값과 prv값을 관리합니다.
# 0이면 없다는 뜻입니다.
prv, nxt = defaultdict(lambda: 0), defaultdict(lambda: 0)

# 각 벨트별로 head, tail id를 관리합니다.
# 0이면 없다는 뜻입니다.
head = [0] * MAX_M
tail = [0] * MAX_M

# 벨트가 망가졌는지를 표시합니다.
broken = [False] * MAX_M

# 물건 별로 벨트 번호를 기입합니다.
# 벨트 번호가 -1이면 사라진 것입니다.
belt_num = defaultdict(lambda: -1)


# 공장 설립
def build_factory(elems):
    global n, m

    # 공장 정보를 입력받습니다.
    n, m = elems[1], elems[2]
    ids, ws = elems[3:3 + n], elems[3 + n:3 + n + n]

    # id마다 무게를 관리합니다.
    for i in range(n):
        weight[ids[i]] = ws[i]

    # 벨트 별로 상자 목록을 넣어줍니다.
    size = n // m
    for i in range(m):
        # head, tail을 설정해줍니다.
        head[i] = ids[i * size]
        tail[i] = ids[(i + 1) * size - 1]
        for j in range(i * size, (i + 1) * size):
            # 상자 ID마다 벨트 번호를 기입합니다.
            belt_num[ids[j]] = i

            # nxt, prv를 설정해줍니다.
            if j < (i + 1) * size - 1:
                nxt[ids[j]] = ids[j + 1]
                prv[ids[j + 1]] = ids[j]


# Id에 해당하는 상자를 삭제합니다
def remove_id(_id, remove_belt):
    b_num = belt_num[_id]
    # 벨트 번호를 제거해줍니다.
    if remove_belt:
        belt_num[_id] = -1

    # 하나 남은 원소라면
    # head, tail이 사라지고 끝납니다.
    if head[b_num] == tail[b_num]:
        head[b_num] = tail[b_num] = 0

    # 삭제 되는게 head라면
    # head만 변경되고 끝납니다.
    elif _id == head[b_num]:
        nid = nxt[_id]
        head[b_num] = nid
        prv[nid] = 0
    # 삭제 되는게 tail이라면
    # tail만 변경되고 끝납니다.
    elif _id == tail[b_num]:
        pid = prv[_id]
        tail[b_num] = pid
        nxt[pid] = 0
    # 중간에 있는 id가 삭제되는 것이라면
    # nxt, prv만 수선해줍니다.
    else:
        pid, nid = prv[_id], nxt[_id]
        nxt[pid] = nid
        prv[nid] = pid

    # nxt, prv값을 지워줍니다.
    nxt[_id] = prv[_id] = 0


# target_id 바로 뒤에
# id를 추가합니다.
def push_id(target_id, _id):
    nxt[target_id] = _id
    prv[_id] = target_id

    # 만약 target_id가 tail이었다면
    # tail을 변경해줍니다.
    b_num = belt_num[target_id]
    if tail[b_num] == target_id:
        tail[b_num] = _id


# 물건 하차
def drop_off(elems):
    w_max = elems[1]

    # 각 벨트마다 보며
    # 첫 번째 상자를 열어봅니다.
    w_sum = 0
    for i in range(m):
        # 망가진 벨트라면 넘어갑니다.
        if broken[i]:
            continue

        # 벨트의 head를 확인합니다.
        if head[i] != 0:
            _id = head[i]
            w = weight[_id]

            # 가장 앞에 있는 상자의 무게가 w_max 이하라면
            # 하차시키고 답에 더해줍니다.
            if w <= w_max:
                w_sum += w

                # 하차를 진행합니다.
                remove_id(_id, True)
            # 그렇지 않다면
            # 상자를 맨 뒤로 올려줍니다.
            elif nxt[_id] != 0:
                # 제거해준 뒤
                remove_id(_id, False)

                # 맨 뒤에 push해줍니다.
                push_id(tail[i], _id)

    # 하차한 상자의 무게 합을 출력합니다.
    print(w_sum)


# 물건 제거
def remove(elems):
    r_id = elems[1]

    # 이미 삭제된 상자라면
    # -1을 출력하고 패스합니다.
    if belt_num[r_id] == -1:
        print(-1)
        return

    # 해당 상자를 제거합니다.

    remove_id(r_id, True)
    print(r_id)


# 물건 확인
def find(elems):
    f_id = elems[1]

    # 이미 삭제된 상자라면
    # -1을 출력하고 패스합니다.
    if belt_num[f_id] == -1:
        print(-1)
        return

    # 해당 상자를 찾아
    # 이를 맨 앞으로 당겨줍니다.
    # head가 아닌 경우에만 유효합니다.
    b_num = belt_num[f_id]
    if head[b_num] != f_id:
        orig_tail = tail[b_num]
        orig_head = head[b_num]

        # 새로 tail을 갱신해줍니다.
        now_tail = prv[f_id]
        tail[b_num] = now_tail
        nxt[now_tail] = 0

        # 기존 tail의 nxt를 head로,
        # heda의 prv를 기존 tail로 만들어줍니다.
        nxt[orig_tail] = orig_head
        prv[orig_head] = orig_tail

        # 새로 head를 지정합니다.
        head[b_num] = f_id

    # 해당 ID의 belt 번호를 출력합니다.
    print(b_num + 1)


# 벨트 고장
def broken_belt(elems):
    b_num = elems[1]
    b_num -= 1

    # 이미 망가져 있다면
    # -1을 출력하고 패스합니다.
    if broken[b_num]:
        print(-1)
        return

    broken[b_num] = 1

    # 만약 빈 벨트라면 패스합니다.
    if head[b_num] == 0:
        print(b_num + 1)
        return

    # 오른쪽으로 돌면서
    # 아직 망가지지 않은 벨트 위로 상자를 전부 옮겨줍니다.
    nxt_num = b_num
    while True:
        nxt_num = (nxt_num + 1) % m
        # 최초로 망가지지 않은 곳이 보이면
        if not broken[nxt_num]:
            # 만약 해당 벨트가 비어있다면
            # 그대로 옮겨줍니다.
            if tail[nxt_num] == 0:
                head[nxt_num] = head[b_num]
                tail[nxt_num] = tail[b_num]
            else:
                # 해당 위치로 상자를 전부 옮겨줍니다.
                # head만 tail뒤에 붙여준 뒤
                push_id(tail[nxt_num], head[b_num])
                # tail만 갈아껴주면 됩니다.
                tail[nxt_num] = tail[b_num]

            # head부터 tail까지 보며
            # belt_num을 갱신해줍니다.
            _id = head[b_num]
            while _id != 0:
                belt_num[_id] = nxt_num
                _id = nxt[_id]

            head[b_num] = tail[b_num] = 0
            break

    print(b_num + 1)


# 입력:
q = int(input())
for _ in range(q):
    elems = list(map(int, input().split()))
    q_type = elems[0]

    if q_type == 100:
        build_factory(elems)
    elif q_type == 200:
        drop_off(elems)
    elif q_type == 300:
        remove(elems)
    elif q_type == 400:
        find(elems)
    else:
        broken_belt(elems)

'''