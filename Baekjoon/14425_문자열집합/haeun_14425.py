"""
딕셔너리 -> 3000대 ms
세트 -> 140대 ms

"""
import sys

answer = 0
N, M = map(int, sys.stdin.readline().split())

# --------------------- 딕셔너리

# S = dict()
#
# for _ in range(N):
#     sentence = sys.stdin.readline().rstrip()
#     first_chr = sentence[0]
#     if S.get(first_chr):
#         # N개의 문자열중 첫번째 알파벳 기준으로 dictionary 형성
#         S[first_chr].append(sentence)
#     else:
#         S[first_chr] = [sentence]
#
#
# for _ in range(M):
#     M_sentence = sys.stdin.readline().rstrip()
#     first_chr = M_sentence[0]
#     # 첫번째 알파벳과 일치하는 문장이 S에 있었는지 확인하면서 불필요한 탐색 제거
#     if S.get(first_chr):
#         sentences = S[first_chr]
#
#         if M_sentence in sentences:
#             answer += 1
#
# print(answer)

# --------------------- 세트
S = set([sys.stdin.readline().rstrip() for _ in range(N)])

for _ in range(M):
    sentence = sys.stdin.readline().rstrip()
    if sentence in S:
        answer += 1

print(answer)