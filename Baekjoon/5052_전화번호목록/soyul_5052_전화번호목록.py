import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    phone_book = []
    for _ in range(n):
        phone_book.append(sys.stdin.readline())
    phone_book.sort()

    answer = "YES"
    for i in range(n-1):
        if len(phone_book[i+1]) > len(phone_book[i]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = "NO"
                break
    print(answer)