'''

최대힙

널리 잘 알려진 자료구조 중 최대 힙이 있다.
최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.


입력

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
입력되는 자연수는 231보다 작다.


츌력

입력에서 0이 주어진 회수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.


참고 : https://www.daleseo.com/python-heapq/


최대힙 구현

[응용] 최대 힙
heapq 모듈은 최소 힙(min heap)을 기능만을 동작하기 때문에 최대 힙(max heap)으로 활용하려면 약간의 요령이 필요합니다.
바로 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것입니다.
따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, (우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제하면 됩니다.
그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됩니다. (우선 순위에는 관심이 없으므로 )


'''

import sys
import heapq


n = int(sys.stdin.readline())
heap = []


for i in range(n):
    num = int(sys.stdin.readline())
    if num > 0 :
        heapq.heappush(heap, (-num, num))

    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)



