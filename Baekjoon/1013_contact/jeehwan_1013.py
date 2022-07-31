'''


정규 표현식 문제



이건 알고에 안나오겟다.

'''


import re
t = int(input())
for i in range(t):
    a = input()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(a):
        print("YES")
    else:
        print("NO")