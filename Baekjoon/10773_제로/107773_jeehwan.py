K = int(input())

stack = []

for i in range(K) :
    n = int(input())

    if n == 0:
        stack.pop(-1)
    else:
        stack.append(n)

print(sum(stack))
