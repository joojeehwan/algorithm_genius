'''


문제


LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.




참고 :  https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence


시간 복잡도 : O(height * width) => O(N ^ 2) 복잡도를 가짐
'''


import sys

input = sys.stdin.readline

words1, words2 = input().rstrip() , input().rstrip()
height , width = len(words1), len(words2)
#print(words1, words2)

LCS = [[0] * (width + 1) for _ in range(height + 1)]


for row in range(height + 1) :
    for col in range(width + 1) :

        if row == 0 or col == 0 :
            LCS[row][col] = 0

        elif words1[row - 1] == words2[col - 1] :
            LCS[row][col] = LCS[row - 1][col - 1] + 1

        else:
            LCS[row][col] = max(LCS[row - 1][col], LCS[row][col - 1])


print(LCS[-1][-1])