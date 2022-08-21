import math


def solution(fees, records):
    answer = []
    basic_time, basic_fee, add_time, add_fee = fees
    history = dict()
    for record in records:
        time, number, move = record.split()
        hour, minute = map(int, time.split(":"))
        # 시간:분 을 분 단위로만 저장함
        if history.get(number):
            history[number].append(hour*60+minute)
        else:
            history[number] = [hour*60+minute]

    for car in history:
        full_time = 0
        cnt_record = len(history[car])

        # 기록이 짝수가 아니면 23:59 출차 기록 추가
        if cnt_record % 2:
            history[car].append(23*60+59)

        # 2개씩 보면서 주차시간 계산
        for i in range(0, cnt_record, 2):
            full_time += history[car][i+1] - history[car][i]

        if full_time <= basic_time:
            answer.append((car, basic_fee))
        else:
            # 올림은 math.ceil
            total_fee = basic_fee + math.ceil((full_time - basic_time) / add_time) * add_fee
            answer.append((car, total_fee))

    answer = sorted(answer)

    return [j[1] for j in answer]


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))