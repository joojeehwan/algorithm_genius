

'''


["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
[3, 7]

["AA", "AB", "AC", "AA", "AC"]
[1, 3]

["XYZ", "XYZ", "XYZ"]
[1, 1]

["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
[1, 5]


투 포인터 문제, 카카오 해설 참고


문제 해설

맵 자료구조에서, ‘map[보석 이름] = 빈도수’로 정의를 합니다. => 딕셔너리 사용하라는 뜻
왼쪽 포인터 l과 오른쪽 포인터 r을 모두 1번 진열대에 위치시킵니다.
양 포인터 중, 둘 중 하나라도 진열대의 범위를 벗어나면 알고리즘을 종료합니다.
양 포인터가 가리키는 범위 안에 포함된 보석 종류의 개수를 세어 봅니다.(map의 사이즈를 체크합니다)
5-1. 범위 안에 보석 종류가 전체 보석 종류와 일치하면 더 좋은 답인지 체크한 후 l를 증가시킵니다. 그리고 2로 갑니다.
5-2. 범위 안에 보석 종류가 전체 보석 종류보다 작다면 r를 증가시킵니다. 그리고 3으로 갑니다.


즉, 왼쪽을 가리키는 포인터 l과 오른쪽을 가리키는 포인터 r을 이용하여 보석의 종류가 모자라면 r을 증가시키고,
보석의 종류가 충분하면 l을 증가시키는 과정을 반복하면서, 정답을 갱신시켜나갑니다.
이때 l을 증가시키기 이전, map자료구조에서 l번 진열대에 있던 보석의 빈도수를 감소시켜주어야 하며 특히 빈도수가 1에서 0이 될 때에는 map에서 완전히 제거하여야 합니다.
r을 증가시킬 때는 map자료구조에서 증가된 r번 진열대에 있는 보석의 빈도수를 증가시켜줍니다.


https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL3-%EB%B3%B4%EC%84%9D-%EC%87%BC%ED%95%91-Python

참고
'''

# def solution(gems):
#     size = len(set(gems))
#     dic = {gems[0]:1}
#     temp = [0, len(gems) - 1]
#     start , end = 0, 0
#
#     while(start < len(gems) and end < len(gems)):
#         if len(dic) == size:
#             if end - start < temp[1] - temp[0]:
#                 temp = [start, end]
#             if dic[gems[start]] == 1:
#                 del dic[gems[start]]
#             else:
#                 dic[gems[start]] -= 1
#             start += 1
#
#         else:
#             end += 1
#             if end == len(gems):
#                 break
#             if gems[end] in dic.keys():
#                 dic[gems[end]] += 1
#             else:
#                 dic[gems[end]] = 1
#
#     return [temp[0]+1, temp[1]+1]


def solution(gems):

    # 처음 인덱스, 끝 인덱스
    answer = [0, len(gems)]
    # 보석의 종류 갯수(중복x)
    size = len(set(gems))
    left, right = 0, 0

    gem_dict = {gems[0] : 1} # 처음 시작하는 left, right가 같이 있는 그곳의 값은 넣어주고 시작

    while left < len(gems) and right < len(gems) : #범위를 벗어나지 않음

        #딕셔너리에 보석의 종류가 다 들어오는 경우
        if len(gem_dict) == size:
            #최소 크기 인지 확인해야 한다. 현재 answer에 들어있는 길이보다, 더 작다면 이를 갱신
            if right - left < answer[1] - answer[0] :
                answer = [left, right]
                
            else:
                #최소 크기가 아닌 경우에는, left를 오른쪽으로 이동 시켜, 포인터를 이동해야함. 이떄, 당연히 보석의 종류는 줄어야 한다.
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0: # 하나도 없으면, key가 없어져야 한다.
                    del gem_dict[gems[left]]
                left += 1
        else :
            #보석이 다 없으니깐, right 포인터를 오른쪽으로 이동시키면서 새로운 값을 확인해보기
            right += 1

            #끝까지 다 갔다.
            if right == len(gems):
                break

            # 이제 오른쪽으로 새롭게 이동하면서, 딕셔너리에 key가 존재하면, value를 증가시켜 준다.
            gem_dict[gems[right]] = gem_dict.get(gems[right], 0) + 1
            '''
             if gems[right] in gem_dict: # 딕셔너리 key에 있으면 count
                gem_dict[gems[right]] += 1
                
            else:   # 없으면 추가
                gem_dict[gems[right]] = 1
            '''
    return [answer[0] + 1, answer[1] + 1] #시작 인덱스가 1번 부터

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))