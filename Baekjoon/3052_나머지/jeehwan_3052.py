input_arr = [int(input()) for _ in range(10)]
answer_arr = [0] * 42

for num in input_arr:
    target = num % 42
    answer_arr[target] = 1

print(answer_arr.count(1))