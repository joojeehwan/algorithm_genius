def solution(triangle):
    depth = len(triangle)
    for d in range(depth-1, 0, -1):
        below = triangle[d]
        above = triangle[d-1]
        for left in range(d):
            above[left] += max(below[left], below[left+1])
    answer = triangle[0][0]
    return answer