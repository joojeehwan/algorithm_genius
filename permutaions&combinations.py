#순열 순서가 있음! 그래서 (1,2) 랑 (2,1)은 다른것으로 본다.

from itertools import permutations

a = [1,2,3]
permute = permutations(a,2)

print(list(permute))


#조합은 순서가 없음!

from itertools import combinations

a = [1,2,3]
combi = combinations(a, 2)

print(list(combi))


