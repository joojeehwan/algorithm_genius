from copy import deepcopy
import time

# 이게 맞는건지 모르겠다...
def find_possible_numbers(row, col):
    # set를 만들어서 교집합을 찾아냄
    row_possibles = set()
    col_possibles = set()
    tres_possibles = set()
    for idx in range(9):
        if rows[row][idx] == 0:
            row_possibles.add(idx + 1)
    for idx in range(9):
        if cols[col][idx] == 0:
            col_possibles.add(idx + 1)
    for idx in range(9):
        if tres[(row // 3) * 3 + col // 3][idx] == 0:
            tres_possibles.add(idx + 1)
    return row_possibles.intersection(col_possibles).intersection(tres_possibles)


def dfs(making_sudoku, count):
    global answer
    # 빈 칸을 모두 봤다면 끝냄
    if count == empty_cnt:
        answer = making_sudoku
        return

    now_row, now_col = empty_list[count]
    now_possible_numbers = find_possible_numbers(now_row, now_col)
    if not possible_numbers:
        return
    else:
        for now_number in now_possible_numbers:
            now_index = now_number - 1
            rows[now_row][now_index], cols[now_col][now_index], \
            tres[(now_row // 3) * 3 + now_col // 3][now_index] = 1, 1, 1
            making_sudoku[now_row][now_col] = now_number
            dfs(making_sudoku, count+1)
            if answer:
                # 답을 찾았다면 0으로 되돌릴 이유가 없으므로 끝내야함
                return
            rows[now_row][now_index], cols[now_col][now_index], \
            tres[(now_row // 3) * 3 + now_col // 3][now_index] = 0, 0, 0
            making_sudoku[now_row][now_col] = 0


sudoku = list(list(map(int, input().split())) for _ in range(9))

# 각 행, 열, 3*3 칸 안에 1부터 9까지 무슨 숫자가 있는지
rows = list([0] * 9 for _ in range(9))
cols = list([0] * 9 for _ in range(9))
tres = list([0] * 9 for _ in range(9))

# 0의 위치를 담을 배열
empty_list = []

answer = False

for row in range(9):
    for col in range(9):
        # 0일 경우 위치를 저장하고
        if sudoku[row][col] == 0:
            empty_list.append((row, col))
        else:
            # 아닐 경우 해당 숫자의 index에 갖고 있다고 행, 열, 3*3 마다 저장함
            number = sudoku[row][col] - 1
            rows[row][number] = 1
            cols[col][number] = 1
            tres[(row // 3) * 3 + col // 3][number] = 1

empty_cnt = len(empty_list)
# 첫 번째 빈칸부터 시작한다.
first_row, first_col = empty_list[0][0], empty_list[0][1]
possible_numbers = find_possible_numbers(first_row, first_col)
for number in possible_numbers:
    index = number - 1
    rows[first_row][index], cols[first_col][index], tres[(first_row // 3) * 3 + first_col // 3][index] = 1, 1, 1
    new_sudoku = deepcopy(sudoku)
    new_sudoku[first_row][first_col] = number
    dfs(new_sudoku, 1)
    if answer:
        # 이건 혹시 첫번째에서 고른 숫자가 맞지 않을까봐 for문을 돌림
        break
    rows[first_row][index], cols[first_col][index], tres[(first_row // 3) * 3 + first_col // 3][index] = 0, 0, 0
    new_sudoku[first_row][first_col] = 0

for i in range(9):
    print(*answer[i])
# print(time.process_time())