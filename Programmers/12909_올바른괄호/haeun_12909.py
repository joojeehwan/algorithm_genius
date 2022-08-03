def solution(s):
    if s[0] == ")":
        return False

    answer = True

    open_bracket = 0
    close_bracket = 0

    for bracket in s:
        if bracket == "(":
            open_bracket += 1
            # if open_bracket > close_bracket > 0:
            #     answer = False
            #     break
        else:
            close_bracket += 1
            if open_bracket == close_bracket:
                open_bracket, close_bracket = 0, 0
            elif open_bracket < close_bracket:
                answer = False
                break

    if open_bracket != close_bracket:
        answer = False

    return answer

print(solution("(((()())))"))

