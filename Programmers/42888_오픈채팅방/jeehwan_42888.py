'''


2가지 case가 존재 

1. 채팅방 나간 후, 다시 새로운 닉네임으로 입장 (leave -> enter)

    > 입장  / 퇴장 로그 남음
    
2. 채팅방안에서 자체적으로 닉네임 변경(change)

    > 입장 / 퇴장 고려할 필요없이, 닉네임자체 찾아 변경


[유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
[유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
[유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
첫 단어는 Enter, Leave, Change 중 하나


해결 방법)



dict를 사용해, 유저id : 닉네임으로 key - value 설정

> uid와 닉네임을 묶으면, 중복되는 닉네임도 구분 가능
> uid - 닉네임 1대1로 저장해서, 굳이 변경되는 것을 기록x
> record 자체는 순서대로 들어오기에, 최신 값(value)을 바로 갱신하면 된다.

굳이 change를 고려하지 않아도 된다. why?! 우리는 어차피 최종적인 유저id - 닉네임만 알고 싶은 것





'''

# 방1
def solution(record):
    answer = []
    #정말 파이써닉하다...!
    id={info.split()[1]:info.split()[2] for info in record if info.split()[0]!="Leave"}
    for info in record:
        if info.split()[0]=="Enter":
            answer.append(id[info.split()[1]]+"님이 들어왔습니다.")
        elif info.split()[0]=="Leave":
            answer.append(id[info.split()[1]]+"님이 나갔습니다.")
    return answer



# 방2
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer


# 방3
# ids, answer로 분리해주고 각 커맨드마다 실행해준 뒤 마지막에 이전 닉네임 길이 저장할 필요 없이 뒤에 "들어왔습니다"를 확인해서
# 각 uid에 맞는 닉네임과 메세지로 변경해주면 됩니다.

def solution(record):
    ids = []
    answer = []
    users = {}
    for r in record:
        command = r.split()
        c = command[0]
        uid = command[1]
        if c == "Enter":
            users[uid] = command[2]
            ids.append(uid)
            answer.append(command[2]+"님이 들어왔습니다.")
        elif c == "Leave":
            ids.append(uid)
            answer.append(users[uid]+"님이 나갔습니다.")
        else:
            users[uid] = command[2]
    for i in range(len(ids)):
        username = users[ids[i]]
        if answer[i][len(answer[i]) - 7:] == "들어왔습니다.":
            answer[i] = username + "님이 들어왔습니다."
        else:
            answer[i] = username + "님이 나갔습니다."
    return answer


'''
입력

["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
'''

def solution(record):

    answer = []
    # id_dict = dict()
    # commands = [list(r.split()) for r in record]

    # 1. key - value dict에 저장
    dt = dict()
    for rec in record:
        # leave는 고려 x, 닉네임 변경에 관여x
        # 공백을 기준으로 list로 나누기
        temp = rec.split()
        if len(temp) == 3:
            # dict는 append, pop 이런거 없다!
            dt[temp[1]] = temp[2]
    # print(dt)

    # 2. command에 맞게 명령어 출력, 이 때 change는 고려x, 위의 dict저장하는 과정에서, 최신의 값 이미 저장
    # 변화 이력을 남길 필요 x
    for rec in record:

        temp = rec.split()
        if temp[0] == "Enter":
            answer.append(f"{dt[temp[1]]}님이 들어왔습니다.")

        elif temp[0] == "Leave":
            answer.append(f"{dt[temp[1]]}님이 나갔습니다.")


    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))