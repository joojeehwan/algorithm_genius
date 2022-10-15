import math

def solution(fees, records):

    # 누적 주차 시간을 계산하는 함수
    car = dict()
    total_minute = dict()
    for record in records:
        time = record[:5]
        number = record[6:10]
        type = record[-2:]
        if type == 'IN':                        # 입차면 기록해두고
            car[number] = int(time[:2]) * 60 + int(time[-2:])
        else:                                    # 출차면 바로 계산
            if number in total_minute:                      # 이미 차가 기록되어 있으면 더해주기
                total_minute[number] += int(time[:2]) * 60 + int(time[-2:]) - car[number]
            else:
                total_minute[number] = int(time[:2]) * 60 + int(time[-2:]) - car[number]
            car.pop(number)

    for number in car:
        if number in total_minute:
            total_minute[number] += 23 * 60 + 59 - car[number]
        else:
            total_minute[number] = 23 * 60 + 59 - car[number]

    # 누적 주차시간으로 주차비 계산
    # fees = [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
    pay = []
    for record in total_minute:
        if total_minute[record] < fees[0]:               # 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구
            pay.append((int(record), fees[1]))
        else:                                 # 기본 시간 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구
            pay.append((int(record), fees[1] + math.ceil((total_minute[record] - fees[0]) / fees[2]) * fees[3]))

    pay.sort()
    answer = []
    for p in pay:
        answer.append(p[1])

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))