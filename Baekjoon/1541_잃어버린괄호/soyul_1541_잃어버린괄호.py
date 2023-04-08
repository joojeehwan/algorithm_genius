lst = list(input().split('-'))      # - 로 구분해줌
ans = sum(list(map(int, lst[0].split('+'))))            # 첫번째 숫자는 더해주고  -로 구분되는 것마다 합을 구해서 빼줌
for k in range(1, len(lst)):
    ans -= sum(list(map(int, lst[k].split('+'))))

print(ans)