import math


def solution(fees, records):
    # 차량번호 순으로 오름차순 정렬하기
    data = []
    for record in records:
        data.append(record.split())
    data.sort(key=lambda x: x[1])
    records = data

    # 차량번호별 출차정보 dict로 정리하기
    records_dict = {}
    for record in records:
        time, num, parking = record
        if num in records_dict.keys():
            records_dict[num] += [(time, parking)]
        else:
            records_dict[num] = [(time, parking)]

    ans = []
    for key, values in records_dict.items():
        # 주차시간 계산하기
        parking_lot = []
        time = 0  # 총 주차시간
        for value in values:
            if value[1] == "IN":  # 입차
                in_h, in_m = map(int, value[0].split(":"))  # 입차 시, 분
                parking_lot.append(in_h * 60 + in_m)
            else:  # 출차
                out_h, out_m = map(int, value[0].split(":"))  # 출차 시, 분
                time += (out_h * 60 + out_m) - parking_lot.pop()
        if parking_lot:  # 출차가 기록되지 않음
            time += (23 * 60 + 59) - parking_lot.pop()

        # 요금 계산하기
        base_time, base_rate, unit_time, unit_rate = fees  # 기본 시간, 기본 요금, 단위 시간, 단위 요금
        if time <= base_time:
            ans.append(base_rate)
        else:
            ans.append(base_rate + math.ceil((time - base_time) / unit_time) * unit_rate)
    return ans


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                                      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN",
                                      "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))