
import sys


N, B = map(int, sys.stdin.readline().split())

MATRIX = [list(map(int, input().split())) for _ in range(N)]

#print(MATRIX)


def MATRIX_MULTIPLE(n, matrix_a, martix_b):

    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] +=  ( matrix_a[i][k] * martix_b[k][j] )
            res[i][j] %= 1000
    return res



def solve(n, degree, matrix) :

    if degree == 1:
        return matrix


    elif degree == 2:
        return MATRIX_MULTIPLE(n, matrix, matrix)

    else:

        temp = solve(n, degree // 2, matrix)
        #짝수인 경우   제곱수를 계속 곱하면 됨. ex) AAAA = ((A ^ 2) ^ 2)
        if degree % 2 == 0 :
            return MATRIX_MULTIPLE(n, temp, temp)

        #홀수인 경우 마지막에 matrix를 하나 더 곱해줘야 한다.  ex) AAAAA = ((A ^ 2) ^ 2) * A
        else:
            return  MATRIX_MULTIPLE(n, MATRIX_MULTIPLE(n, temp, temp), matrix)

ans = solve(N, B, MATRIX)

for lst in ans:
    for value in lst:
        print(value % 1000, end = " ")
    print()