def solution(s):
    lnth = len(s)
    answer = lnth

    # 압축하는 문자열의 길이가 총 길이의 반을 넘어가면 압축의 의미가 없음
    for subl in range(1, lnth//2 + 1):
        l = 0           # 레프트
        r = subl        # 라이트
        last = s[l:r]   # 직전 문자열: 이와 일치하는 문자열을 연속으로 만나면 카운터만 증가
        subcount = 1    # 방금 말한 그 카운터
        comlength = 0   # subl 길이로 압축한 문자열의 길이
        
        # 첫번째 압축 문자열은 봤으니 한 스텝 전진
        l = r
        r += subl

        # 이후 반복문 시작
        while r <= lnth: # 라이트가 문자열을 벗어나지 않는 한
            if last == s[l:r]: # 지금 보는 문자열이 직전과 같다면
                subcount += 1  # 카운터 증가
            else:        # 다르다면
                comlength += subl # 직전 문자열 길이만큼 압축 문자열 길이 증가
                if subcount > 1:  # 카운터가 1이면 생략이지만 아니라면 그 길이만큼 또 추가
                    comlength += len(str(subcount))
                last = s[l:r]
                subcount = 1
            l = r
            r += subl
        comlength += subl # 라이트가 끝을 벗어나면 직전 문자열이 저장되지 않은 채로 탈출됨
        # 직전에 담긴 문자열에 대해 처리
        if subcount > 1:
            comlength += len(str(subcount))
        # 길이가 나누어떨어지지 않아 남은 만큼 또 처리
        if l < lnth:
            comlength += len(s[l:])
        
        # 최소값 판별
        answer = min(answer, comlength)
    return answer