import sys

input = sys.stdin.readline

target = int(input())

n = int(input())

broken = list(map(int, input().split()))

#현재 채널에서 + 혹은 -만 사용!하는 경우
min_count = abs(100 - target)

#이렇게 적는것이 포인트
for nums in range(1000001):
    nums = str(nums)
    #왜 str로 바꾸나?! nums 중에서 하나의 숫자만 뽑기 위해서! 그렇게 한 것!
    # str로 안바꾸면 하나의 숫자를 뽑을 수가 없으니깐!
    # 각 숫자 하나씪 확인!
    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        #고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            #아 abs(int(nums) - target) 부분이 ++ , -- 와 같은 역활을 한다.
            #거기다가 숫자의 길이를 더해주면,,
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)


'''

결국 2가지 케이스가 존재하는 것! 

 1. 현재채녈에서 희망채널까지 + , - 로 이동하는 경우
 2. 모든 채널을 순회하면서 해당 채널에서 희망채널까지 +- 버튼으로 이동했을떄의 횟수
'''