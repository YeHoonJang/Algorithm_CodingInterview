n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = [[] for _ in range(n)]
result[0].append(arr[0][0])

for i in range(1, n):
    # 1, 2, 3, 4
    end = len(arr[i])-1
    # 0, 1, 2, 3, 4
    for j in range(len(arr[i])):
        # 0, 1 / 0, 1, 2 / 0, 1, 2, 3 / 0, 1, 2, 3, 4
        if j != 0 and j != end:
            result[i].append(max(result[i-1][j-1]+arr[i][j], result[i-1][j]+arr[i][j]))
        elif j == 0:
            result[i].append(result[i-1][0]+arr[i][0])
        elif j == end:
            result[i].append(result[i-1][j-1]+arr[i][j])

print(max(result[-1]))