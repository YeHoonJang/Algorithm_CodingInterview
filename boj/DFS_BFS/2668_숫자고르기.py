#다시

def dfs(i):
    x = under_row[i]
    if tmp_visited[i] is False:
        tmp_visited[i] = True
        x = under_row[x]
        dfs(x)
    elif tmp_visited[i] is True and visited[i] is False and i==under_row[x]:
        visited[i] = True
        dfs(x)
    else:
        pass


n = int(input())
under_row = [int(input()) for i in range(n)]
under_row.insert(0, 0)
up_row = [i for i in range(n+1)]

graph = list(zip(up_row, under_row))

visited = [False]*(n+1)
tmp_visited = visited.copy()


for i in range(1, n+1):
    dfs(i)

print(sum(visited))
for i in range(len(visited)):
    if visited[i] is True:
        print(i)