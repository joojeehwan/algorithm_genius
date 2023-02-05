''''

이진트리를 수로 표현

1. 이진수를 저장할 빈 문자열 생성

2. 주어진 이진트리에 더미 노드를 추가하여 포화이진 트리로 만들기  => 루트 노드는 그대로 유지 

3. 만들어진 포화 이진 트리의 노드들을 가장 왼쪽 노드에서부터 가장 오른쪽 노드까지, 왼쪽에 있는 순서대로 탐색 

    => 노드의 높이는 탐색의 순서에 영향을 끼치지 않는다.

4. 탐색한 노드가 더미 노드라면, 문자열 뒤에 0을 추가 // 더미 노드가 아니라면 문자열 뒤에 1을 추가 

5. 문자열에 저장된 이진수를 십진수로 변환


이진트리에서 리프 노드가 아닌 노드(루트 노드)는 자신이 왼쪽 자식이 루트인 서브트리의 노드보다 오른쪽에 있으며, 
자신의 오른쪽 자식이 루트인 서브트리의 노드들보다 왼쪽에 있다고 가정  => 생각해보면 당연해




[7, 4, 2]        [1, 1, 0]

[63, 111, 95]    [1, 1, 0]

'''


def is_tree(s, parent):
    if parent == '0':
        #부모가 0인데, 자식이 1을 가지고 있다?! 모순
        if not all(child == '0' for child in s):
            return False

    if len(s) == 1:
        return True

    center = len(s) // 2

    return is_tree(s[:center], s[center]) and is_tree(s[center + 1:], s[center])


def solution(numbers):
    answer = []

    for number in numbers:

        bs = bin(number)[2:]
        print()
        digit = 0  # 포화 이진 트리가 되기 위한 문자열의 길이

        for i in range(51):

            digit = 2 ** i - 1
            if digit >= len(bs):
                break

        bs = '0' * (digit - len(bs)) + bs
        answer.append(1 if is_tree(bs, bs[len(bs) // 2]) else 0)

    return answer



