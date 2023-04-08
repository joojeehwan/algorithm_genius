st = input()
search = input()

answer = 0
i = 0
while i < len(st):
    if st[i:i + len(search)] == search:             # 주어진 문자열을 잘라서 찾으려는 문자열과 같으면
        answer += 1
        i += len(search)
    else:
        i += 1

print(answer)