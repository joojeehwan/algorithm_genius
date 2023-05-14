import sys
import heapq
from collections import defaultdict
from typing import List, Tuple, Dict, Set, Optional

# typing = 형 힌트 지원

si = sys.stdin.readline
Q = int(si())
N = 0

# 채점 대기
# 1. 도메인 별 채점 대기 우선순위 목록
# key = 도메인, value = pq(우선순위, 대기 시작 시간, url번호)
wait_q: Dict[str, List[Tuple[int, int, str]]] = defaultdict(list)
# 2. 대기 중인 Url 세트
wait_d: Set[str] = set()
# 3. 대기 큐의 길이
wait_cnt: int = 0

# 채점 진행
# 1. 쉬고있는 채점기 번호를 빠르게 찾기 위한 우선순위 큐
free: List[int] = list()
# 2. 채점기가 채점중인 task의 정보
# idx = 채점기 번호, value = [도메인, 시작시간]
# Optional => None 타입을 가질 수 있다는 뜻
mark: List[Optional[Tuple[str, int]]] = list()

# 채점 기록
# key = 도메인, value = 채점 가능 시간(start + gap*3)
history: Dict[str, int] = defaultdict(int)


def parse_url(u: str) -> List[str]:
    """
    url을 파싱하는 함수
    :param u: 입력받은 url
    :return: [도메인, 번호]
    """
    return u.split("/")


def push_q(t: int, p: int, u: str) -> None:
    global wait_cnt
    """
    wait_q에 입력받은 정보를 바탕으로 task 추가
    :param t: 대기열 입장 시간
    :param p: 우선순위 번호
    :param u: url
    :return: 
    """
    if u in wait_d:
        return
    # 대기중인 url 목록에 추가
    wait_d.add(u)
    # url 파싱
    domain, number = parse_url(u)
    # p -> t 순서에 맞춰 heapq에다 저장한다.
    heapq.heappush(wait_q[domain], (p, t, number))
    # 대기열 수를 추가한다.
    wait_cnt += 1


def init(n: int, u: str) -> None:
    global N, free, mark
    """
    초기화 함수입니다.
    :param n: 채점기의 개수
    :param u: 첫 task의 url
    :return:
    """
    N = n
    free = list(range(1, N + 1))
    mark = [None for _ in range(N + 1)]
    # 0초, 1 순위, url
    push_q(0, 1, u)


def grade(t: int) -> None:
    global wait_cnt
    """
    채점을 시도합니다.
    :param t: 채점 시작 시간
    :return:
    """

    # 1. 사용할 수 있는 채점기가 없다면 의미 없다.
    if not free: return

    # 2. 채점기가 있으면 채점할 task를 찾아본다.
    m_priority = sys.maxsize
    m_insert_time = sys.maxsize
    m_domain = ""

    for d, q in wait_q.items():
        # queue가 비었다면, 채점할 task가 없다는 뜻이다.
        if not q: continue

        # 도메인이 채점 중이거나, 가장 최근에 채점한 기록과 비교하여 불가능한지 판단
        if t < history[d]: continue

        # 채점할 task가 있다면 비교를 통해 고른다.
        priority, insert_time, _ = q[0]
        if (m_priority > priority) or (m_priority == priority and m_insert_time > insert_time):
            m_priority, m_insert_time, m_domain = priority, insert_time, d

    # 채점할 task를 골랐으면, 채점기도 고른다.
    if m_priority != sys.maxsize:
        mark[heapq.heappop(free)] = (m_domain, t)

        # 대기열에서 해당 task를 제거한다.
        _, _, number = heapq.heappop(wait_q[m_domain])
        wait_d.remove(m_domain+"/"+number)
        wait_cnt -= 1
        # 채점 진행중에는 max값을 넣어버린다.
        history[m_domain] = sys.maxsize


def finish(t: int, idx: int) -> None:
    """
    idx 채점기의 채점을 t에 끝냅니다.
    :param t: 끝내는 시간
    :param idx: 채점기 번호
    :return:
    """

    # 만약 비어있다면 띄용
    if mark[idx] is None: return

    # 다 쉬었다.
    heapq.heappush(free, idx)
    domain, start = mark[idx]
    mark[idx] = None

    history[domain] = start + (t - start)*3


def solution():
    for _ in range(Q):
        query = si().split()
        order = query[0]
        if order == "100":
            init(int(query[1]), query[2])
        elif order == "200":
            push_q(int(query[1]), int(query[2]), query[3])
        elif order == "300":
            grade(int(query[1]))
        elif order == "400":
            finish(int(query[1]), int(query[2]))
        else:
            print(wait_cnt)

solution()