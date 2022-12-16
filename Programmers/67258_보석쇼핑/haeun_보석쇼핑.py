def solution(gems):
    answer = []
    min_len = 100001

    shelf = len(gems)
    gems_name = set(gems)
    gems_cnt = len(gems_name)

    now_gems = dict()
    start, end = 0, 0
    now_gems[gems[start]] = 1

    while start < shelf - gems_cnt + 1:
        if len(now_gems) != gems_cnt:
            end += 1

            if end > shelf - 1:
                break
            end_jewel = gems[end]
            if now_gems.get(end_jewel):
                now_gems[end_jewel] += 1
            else:
                now_gems[end_jewel] = 1
        else:
            if end - start < min_len:
                min_len = end - start
                answer = [start + 1, end + 1]
            start_jewel = gems[start]
            now_gems[start_jewel] -= 1
            if now_gems[start_jewel] == 0:
                now_gems.pop(start_jewel)
            start += 1

    return answer


"""
이거 슬라이딩 윈도우로 푼 사람 있나?
https://school.programmers.co.kr/questions/14715
"""