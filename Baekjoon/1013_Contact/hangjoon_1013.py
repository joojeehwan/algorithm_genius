import sys
import re


tc = int(sys.stdin.readline())  # 테스트케이스
target = re.compile("(100+1+|01)+")  # 원하는 패턴
for _ in range(tc):
    data = sys.stdin.readline().strip()
    if target.fullmatch(data):
        print("YES")
    else:
        print("NO")