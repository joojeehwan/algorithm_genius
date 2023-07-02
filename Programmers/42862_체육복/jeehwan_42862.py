def solution(n, lost, reserve):
    #순수하게 여유분만 있는 학생(도난x)
    set_reserve = set(reserve) - set(lost)
    #순수하게 도난만 당한 학생(여유분x)
    set_lost = set(lost) - set(reserve)

    #여유분이 있는 학생 기준
    for i in set_reserve:
        #해당 학생의 index 기준 -1 / +1 햇을 떄, 도난당한 학생에게 체육복을 빌려줄 수 있는지 체크
        if i - 1 in set_lost:
            #remove 연산자를 활용해, 해당값 직접 삭제
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)

    return n - len(set_lost)