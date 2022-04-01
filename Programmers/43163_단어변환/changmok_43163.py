from collections import deque

def solution(begin, target, words):
    
    # 만약 target이 words에 없다면 애초에 불가능한 문제
    if target not in words:
        return 0
    
    conn = {} # 각 단어들의 연결관계를 그래프처럼 저장할 딕셔너리
    reach = {} # 각 단어에 닿는 최단 거리를 저장할 딕셔너리
    
    # begin 단어에 대하여 두 딕셔너리 초기값 설정
    conn[begin] = []
    reach[begin] = 0
    
    for word in words:
        conn[word] = []
        
    ll = len(words)
    wl = len(words[0])     
    
    # begin 단어와 연결된 words 단어들을 찾아 conn에 저장
    for word in words:
        diff = 0
        for c in range(wl):
            if begin[c] != word[c]:
                diff += 1
        if diff == 1:
            conn[begin].append(word)
    
    # 만약 begin과 연결된 단어가 없다면 이 역시 불가능한 문제
    if not conn[begin]:
        return 0
    
    # words 배열 내의 연결관계 파악
    for i in range(ll - 1):
        word = words[i]
        for j in range(i + 1, ll):
            nxword = words[j]
            diff = 0
            for c in range(wl):
                if word[c] != nxword[c]:
                    diff += 1
            if diff == 1:
                conn[word].append(nxword)
                conn[nxword].append(word)
    
    # BFS 시작
    q = deque([begin])
    
    while q:
        now = q.popleft()
        for nex in conn[now]:
            if reach.get(nex) and reach.get(nex) <= reach[now] + 1:
                continue
            reach[nex] = reach[now] + 1
            q.append(nex)
    
    # 만약 target에 닿아서 reach 값이 있다면 값을 리턴, 없다면 기본값 0을 리턴하도록 .get() 메서드 호출
    answer = reach.get(target, 0)
    return answer