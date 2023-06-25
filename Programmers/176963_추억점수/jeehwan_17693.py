from collections import defaultdict

def solution(name, yearning, photo):
    
    answer = []
    N_yearning = defaultdict(int)
    
    #이름별 점수 dict 담기 
    for index in range(len(name)):
        
        N_yearning[name[index]] = yearning[index]

    for i in range(len(photo)):
        
        temp_point = 0
        
        for j in range(len(photo[i])):
            
            temp_point += N_yearning[photo[i][j]]
    
        answer.append(temp_point)
    
    return answer


#풀이 2

def solution(name, yearning, photo):
    n = len(name)
    dct = {}
    for i in range(n):
        dct[name[i]] = yearning[i]

    answer = []
    for lst in photo:
        cnt = 0
        for a in lst:
            if a in dct:
                cnt += dct[a]
        answer.append(cnt)
    return answer

#풀이 3

def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores