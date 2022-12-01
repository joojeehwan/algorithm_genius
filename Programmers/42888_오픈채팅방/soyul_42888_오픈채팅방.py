def solution(record):
    answer = []

    inout = []                  # in out 을 기록하는 배열 [['in', 'uid1234'], ... ]
    nickname = {}               # 유정 아이디별로 닉네임을 기록하는 딕셔너리

    # in, out 기록과 아이디의 닉네임을 기록해줌
    for i in range(len(record)):
        r = list(record[i].split())
        if r[0] == "Enter":
            nickname[r[1]] = r[2]
            inout.append(['in', r[1]])
        elif r[0] == "Change":
            nickname[r[1]] = r[2]                   # 닉네임을 바꿔줌
        else:
            inout.append(['out', r[1]])

    # in인지 out인지 검사하면서 정답 출력
    for io in inout:
        if io[0] == "in":
            answer.append(nickname[io[1]] + "님이 들어왔습니다.")
        else:
            answer.append(nickname[io[1]] + "님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))