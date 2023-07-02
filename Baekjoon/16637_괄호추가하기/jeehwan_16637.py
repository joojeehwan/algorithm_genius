N = int(input())

# 중간에 연사자가 있는 것 입력받기
# lambda x:int(x) if x.isdigit() else x
# 숫자인건 숫자로 받고, 아닌건 그냥 그대로 문자로 받겠다.
data = list(map(lambda x : int(x) if x.isdigit() else x, input()))

#최댓값을 구하기 위한 결과값 세팅
result = - int(1e9)


def calculate(num1, num2, op) :

    if op == '+' :
        return num1 + num2

    elif op == '-' :
        return num1 - num2

    elif op == '*':
        return num1 *  num2

def dfs(idx, value) :

    global result

    if idx >= N:
        #연산이 끝남과 동시에 최대값 갱신
        result = max(result, value)
        return

    if idx + 3 < N:  #괄호 사용 가능
        # idx + 4 ?!
        # 연산 이후의 다음 값을 value값으로 하기 위함. data[idx+4]가 그 다음의 value가 될 것이므로
        dfs(idx + 4, calculate(value, calculate(data[idx + 1], data[idx+3], data[idx + 2]), data[idx]))
    #괄호 사용 사용 불가
    dfs(idx+2, calculate(value, data[idx + 1], data[idx]))



if N == 1: # 주어진 수가 하나일 떄
    result = data[0]

else:
    dfs(1, data[0])

print(result)