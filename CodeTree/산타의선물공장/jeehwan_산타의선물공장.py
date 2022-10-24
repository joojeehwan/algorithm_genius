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
    pass

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
    pass

# 5. 벨트 고장
def broken_belt(elems):
    pass


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