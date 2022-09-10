from collections import defaultdict


def binary_search(lst, key):
    start, end = 0, len(lst) - 1
    center = (start + end) // 2
    while start <= end:
        center = (start + end) // 2
        if int(lst[center]) < key:
            start = center + 1
            center = start
        else:
            end = center - 1
    return len(lst) - center


def solution(info, query):

    # key(문자열)-value(정수 리스트) 형태의 해시테이블로 만들기
    info_dict = defaultdict(list)
    for inf in info:
        key = ''
        inf = inf.split()
        for i in range(4):
            key += inf[i]
        info_dict[key].append(int(inf[-1]))
    # 이분탐색을 위한 정렬
    for k in info_dict.keys():
        info_dict[k].sort()
    # 무관한 항목('-')의 경우 모든 경우의 수로 key를 만들기 위한 목록
    key_lst = [['java', 'python', 'cpp'], ['frontend', 'backend'], ['junior', 'senior'], ['chicken', 'pizza']]

    answer = []
    # 각 요구사항 별 충족하는 지원자가 있는지 판별
    for qs in query:
        qs = qs.split()
        cnt = 0  # 해당 요구사항(qs)에 충족하는 지원자의 수
        keys = []  # 해당 요구사항을 key 형태(문자열)로 만들기
        for i, q in enumerate(qs):  # 해당 요구사항(qs)의 세부 항목(q)
            # 시작하기(첫 항목 = 언어)
            if i == 0:
                if q == '-':  # 무관하면 key_lst 에서 모든 경우의 수 추가
                    for k in key_lst[0]:
                        keys.append(k)
                else:
                    keys.append(q)
            # 코테 비교하기(마지막 항목 = 점수)
            elif i == len(qs) - 1:
                q = int(q)
                for key in keys:
                    if info_dict[key]:  # 해당 key를 가진 지원자가 있을 경우만
                        cnt += binary_search(info_dict[key], q)  # 이분 탐색
            # 항목들 추가하기
            else:
                new_keys = []
                if q == 'and':
                    continue
                if q == '-':  # 무관하면 key_lst 에서 모든 경우의 수 추가
                    for k in key_lst[i // 2]:
                        for key in keys:
                            new_keys.append(key + k)
                else:
                    for key in keys:
                        new_keys.append(key + q)
                keys = new_keys[:]
        answer.append(cnt)
    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))