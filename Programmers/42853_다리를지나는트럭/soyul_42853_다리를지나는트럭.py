"""
트럭을 스택에 하나씩 넣어주고
시간이 지나면 빼주는 방식으로
"""

def solution(bridge_length, weight, truck_weights):

    answer = 0                  # 몇 시간 걸리는지 기록

    ing_truck = []              # 현재 다리 위에 있는 트럭 기록하는 스택
    time_truck = []             # 트럭이 다리 위에 얼마나 올라가있었는지 기록하는 리스트

    idx = 0
    while truck_weights:

        if time_truck:
            for i in range(idx, len(time_truck)):
                time_truck[i] -= 1
                if time_truck[i] == 0:          # 0초가 되면 다 건넌거니까 건너는 트럭 스택에서 빼주고 idx+1 (time 도 pop을 해주면 인덱스 에러가 난다)
                    ing_truck.pop(0)
                    idx += 1

        if sum(ing_truck) + truck_weights[0] <= weight:             # 감당할 수 있는 무게만큼 올라갈 수 있으면 트럭을 올려준다
            ing_truck.append(truck_weights[0])
            truck_weights.pop(0)
            time_truck.append(bridge_length)
        answer += 1

    return answer + bridge_length                # while truck_weights 로 기준을 줘서 마지막 트럭이 올라간 순간 끝난다 마지막 트럭은 bridge_length 시간만큼 건널것이니까 더해주고 return

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

# 트럭은 1초에 1칸씩 움직임