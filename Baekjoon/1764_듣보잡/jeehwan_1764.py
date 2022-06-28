
'''

지금 든 생각은 일단,,,

일단은 N, M 입력받아서, 리스트안에 듣 담고, 보 담고
집합으로 만들어서 교집합
갯수랑, 겹치는거 출력

"듣도 못한 사람의 명단에는 중복되는 이름이 없으며,
보도 못한 사람의 명단도 마찬가지이다."

너무 집합 쓰고 싶자나 ㅠ


좀더 문자열 스럽게 풀수가 있는건가,,
흠흠,,,



'''


N , M = map(int, input().split())

#입력받기 & 집합

#[list(input().rstrip()) for _ in range(N)]이렇게 하면 글자 하나씩!
noSee = set([input().rstrip() for _ in range(N)])
noHear = set([input().rstrip() for _ in range(M)])

#교집합 찾기

answer = list(noSee & noHear)

#정렬 후 갯수 / 이름 출력
answerSorted = sorted(answer)

print(len(answerSorted))

for ans in answerSorted:
    print(ans)

