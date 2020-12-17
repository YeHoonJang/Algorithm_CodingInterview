#순열
from itertools import combinations

data = ["A", "B", "C"]
result = list(combinations(data, 2))
print(result)

#중복 순열합
#2개를 뽑는 모든 순열 구하기 (중복 허용)
from itertools import product
result = list(product(data, repeat=2))
print(result)

#중복 조합
#2개를 뽑는 모든 조합 구하기 (중복 허용)
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)
