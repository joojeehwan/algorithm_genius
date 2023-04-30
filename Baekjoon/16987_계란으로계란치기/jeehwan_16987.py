'''



'''


#초기 입력

N = int(input())

eggs = []

for _ in range(N):
    temp = list(map(int, input().split()))
    eggs.append(temp)

#깰 수 있는 계란의 최대 갯수
ans = 0
def dfs(index, eggs):

    global ans

    #base 조건
    #오른쪽 끝에 도달한 경우
    if index == N:
        cnt = 0
        for egg in eggs:
            #내구도가 0보다 작다!? 꺠졋다
            if egg[0] <= 0 :
                cnt += 1
        #최대의 꺨 수 있는 계란을 갱신
        ans = max(ans, cnt)
        return #여기서 return을 안해주면 idnex out of range error 가 난다,,! 와,,, 이것때문에,,,

    #가지치기 1 지금 들고 있는 계란의 내구도가 0이하이면 다음 계란으로 넘어간다.
    if eggs[index][0] <= 0:
        dfs(index + 1, eggs)
        #여가선 굳이 return  을 안하더라도 , dfs로 넘어가는 부분이 있어, 괜찮지만,,!

    else: #else 가 필수다,,! why?! 아래의 로직을 굳이 타지 않아야 하는데 타게 되니깐 , 이거 안달아서 틀렷다.
        flag = True #자기 자신을 제외한 모든 계란이 꺠져있는 경우

        # 재귀반복 => 계란의 내구도가 남아 있는 경우 다른 계란들과 계란치기 진행
        # 무조건 순서대로 가지 않고, 무수히 많은 경우의 수가 있기에 완전탐색 (dfs로 검사를 하는 것)
        # dfs라고 인지를 하지 못했던 부분, 무조건 다음 순서의 계란으로 순서대로 가야 되는 줄,,,!
        for i in range(N):
            if index != i and eggs[i][0] > 0 : # 현재 들고 있는 계란 제외  // 내구도가 있는 계란만 진행
                flag = False
                #내구도는 부딪히는 계란의 무게만큼 줄어든다
                eggs[index][0] -= eggs[i][1]
                eggs[i][0] -= eggs[index][1]
                dfs(index + 1, eggs)
                eggs[index][0] += eggs[i][1]
                eggs[i][0] += eggs[index][1]


        #자기 자신을 제외한 모든 계란이 깨진 경우
        if flag:
            #바로 종료 조건
            dfs(N, eggs)

dfs(0, eggs)


print(ans)