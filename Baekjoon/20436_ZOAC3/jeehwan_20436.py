'''

여기서 포인트는,,!

성우는 한글 자음 쪽 자판은 왼손 검지손가락으로 입력하고,
한글 모음 쪽 자판은 오른손 검지손가락으로 입력한다.

거리 자체는 단순한 맨해튼 거리!
이차원 배열내에서 index구하는거다! 
'''

#와 이렇게 하면 되는군,,
#이 함수를 만들면 게임 끝
def findLoc(word):
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]
    #이차원 배열도 그냥 1차원 배열 enumerate 돌듯이 나온다.
    for idx , value in enumerate(keyboard):
        # print(idx, value)
        if word in value:
            #배열안에 내가 찾고 있는 단어가 있으면!
            y = idx #거기의 y좌표!는 idx값! enumerate로 이차원배열 1차원배열로 하나씪 꺼내니깐!
            x = value.index(word) #거기 꺼낸 배열에서 몇번쨰 인덱스에 위치 하는
            # print(x, y)
            return x, y

sl, sr = map(str, input().split())
sentence = input()

# print(sl, sr, sentence)
answer = 0

#자음 따로 저장
consonant  = "qwertasdfgzxcv"

for word in sentence:

    #반복문 돌면서 글자들을 검색!한다!
    #처음 부터 그 위치에 손이 가있다면! 한번 누르기만 하면 된다!
    if sl == word or sr == word:
        answer += 1


    # 아닌 경우 각각의 위치 별 x, y위치를 입력

    else:
        newSlx, newSly = findLoc(sl) #처음왼쪽 시작 위치
        newSrx, newSry = findLoc(sr) #처음 오른쪽 시작 위치 
        target_x, target_y = findLoc(word) #찾아가야하는 한 단어의 위치

        #자음이라면 왼쪽이 이동해야 함
        if word in consonant:
            # 마지막에 +1 까지해서 누르는 거 까지 처리
            answer += abs(newSlx - target_x) + abs(newSly - target_y) + 1
            # 누르러 갓으니 이동하자!
            sl, newSlx, newSly = word, target_x, target_y
        #모음이라면 오른쪽이 이동해야함.
        else:
            answer += abs(newSrx - target_x) + abs(newSry - target_y) + 1
            sr, newSrx, newSry = word, target_x, target_y

print(answer)