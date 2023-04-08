string = input().strip()
key = input().strip()

length = len(key)
i = 0
ans = 0
while i < len(string):
    if string[i] == key[0] and string[i:i+length] == key:
        ans += 1
        i += length
    else:
        i += 1

print(ans)