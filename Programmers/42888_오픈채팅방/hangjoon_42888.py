def solution(records):
    user_dict = dict()  # 유저 아이디와 닉네임 목록
    room = []  # 방에 있는 사람들 목록
    messages = []  # 메시지 목록

    for record in records:
        data = record.split()
        if data[0] == 'Enter':  # 입장
            user_dict[data[1]] = data[2]
            room.append(data[1])
            messages.append((0, data[1]))
        elif data[0] == 'Leave':  # 퇴장
            room.remove(data[1])
            messages.append((1, data[1]))
        else:  # 닉네임 변경
            user_dict[data[1]] = data[2]
    answer = []
    for message in messages:
        if not message[0]:  # 입장
            answer.append(f"{user_dict[message[1]]}님이 들어왔습니다.")
        else:  # 퇴장
            answer.append(f"{user_dict[message[1]]}님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))