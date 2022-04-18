from itertools import product

def solution(user_id, banned_id):
    lenbid = len(banned_id)
    possible = [[] for _ in range(lenbid)]
    for uid in user_id: # 각 유저 아이디에 대하여
        for bi in range(lenbid): # 불량 아이디를 대조
            if len(banned_id[bi]) == len(uid): # 길이 일치 여부부터 확인
                match = True # 길이가 일치하다면
                for i in range(len(uid)): # 문자별로 대조 시작
                    if banned_id[bi][i] == '*':
                        continue
                    if banned_id[bi][i] != uid[i]:
                        match = False
                        break
                if match: # 문자열이 일치한다면
                    possible[bi].append(uid) # 가능성 리스트에 저장
    answer = []
    products = list(product(*possible)) # itertools.product()는 입력 받은 iterable 인자들의 데카르트 곱을 구해주는 메서드
    for prod in products: # 해당 데카르트 곱들에 대하여
        prod = set(prod) # 집합으로 변환해서 prod 내의 중복 제거
        if len(prod) < lenbid: # 중복이 제거되어 길이가 짧아지는 경우
            continue
        if prod in answer: # answer에 해당 prod가 이미 들어간 경우
            continue
        answer.append(prod)
    return len(answer)