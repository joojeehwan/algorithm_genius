def solution(s):
    lnth = len(s)
    answer = lnth
    for subl in range(1, lnth//2 + 1):
        l = 0
        r = subl
        last = s[l:r]
        comlength = 0
        subcount = 1
        l = r
        r += subl
        while r <= lnth:
            if last == s[l:r]:
                subcount += 1
            else:
                comlength += subl
                if subcount > 1:
                    comlength += len(str(subcount))
                last = s[l:r]
                subcount = 1
            l = r
            r += subl
        comlength += subl
        if subcount > 1:
            comlength += len(str(subcount))
        if l < lnth:
            comlength += len(s[l:])
        answer = min(answer, comlength)
    return answer