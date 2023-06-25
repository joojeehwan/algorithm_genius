'''

별거없다. 점프가 필요한 순간이면 + 1을 하고, 나머지가 존재하는 경우
점프가 필요하지 않은 경우라면, 계속 순간이동을 해서 건전지를 소모하지 않는다.


'''
def solution(n):
    ans = 0
    while n:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
    return ans
