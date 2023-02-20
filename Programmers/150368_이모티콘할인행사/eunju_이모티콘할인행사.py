import itertools

def solution(users, emoticons):
    answer = []
    discounts = itertools.product([10,20,30,40],repeat=len(emoticons))
    
    maxjoiner = 0; maxamount = 0
    for discount in discounts:
        # 이모티콘 판매 유저, 총 이모티콘 판매액
        joiner=0; amount=0
        # 각 유저마다 이 할인 비율로 검사
        for user in users:
            buy = 0 # 유저가 산 이모티콘 가격
            for i in range(len(discount)):
                if user[0] <= discount[i]: # 유저의 퍼센트보다 이모티콘 할인율이 크면
                    buy+=(emoticons[i]*(1-discount[i]/100))
            if buy >= user[1]: # 유저의 제한 가격보다 이모티콘 구매비용이 크면, 이모티콘 플러스 가입
                joiner+=1
            else:   # 이모티콘 플러스에 가입할 필요 없는 유저는, 총 이모티콘 판매액에 유저가 구매한 비용 더하기
                amount+=buy

        # 이모티콘 플러스 가입할 user가 maxjoiner보다 많으면
        if maxjoiner < joiner:
            maxjoiner = joiner
            maxamount = amount
        # 이모티콘 플러스 가입할 user가 maxjoiner와 같으면, maxamount보다 판매액(amount)가 클때만 넣기
        elif maxjoiner == joiner:
            if maxamount < amount :
                maxamount = amount
        
    answer=[maxjoiner,int(maxamount)] 
    return answer