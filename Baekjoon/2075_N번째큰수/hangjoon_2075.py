import heapq


size = int(input())  # 표 크기
hq = []  # 최소 힙
for r in range(size):
    data = list(map(int, input().split()))
    for c in range(size):
        heapq.heappush(hq, data[c])
        if len(hq) > size:  # size를 초과하면 작은 것부터 pop
            heapq.heappop(hq)

# 결국 heap에는 size 개만 남음 = 가장 작은 원소가 size 번재
print(heapq.heappop(hq))
