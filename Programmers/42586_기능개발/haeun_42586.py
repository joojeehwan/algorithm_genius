from collections import deque


def solution(progresses, speeds):
    answer = []
    count = len(progresses)

    queue = deque([i for i in range(count)])
    out = 0

    while queue:
        today = 0
        for work in range(out, count):
            if progresses[work] >= 100:
                queue.popleft()
                today += 1
            else:
                for job in range(work, count):
                    progresses[job] += speeds[job]
                break

        if today:
            answer.append(today)
            out += today

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))


"""
예전에 푼 버전. 예전에 비해 아주 쬐금 빨라짐

from collections import deque

def solution(progresses, speeds):
    answer = []
    prg_que = deque(progresses)
    spd_que = deque(speeds)
    count = 0
    while len(prg_que) != 0:
        for i in range(len(prg_que)):
            prg_que[i] += spd_que[i]
            
        while len(prg_que) != 0 and prg_que[0] >= 100:
            prg_que.popleft()
            spd_que.popleft()
            count +=1
        
        if count != 0:
            answer.append(count)
        count = 0
    
    return answer
"""