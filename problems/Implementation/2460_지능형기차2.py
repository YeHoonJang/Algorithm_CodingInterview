on, off = [], []
for _ in range(10):
    a, b = map(int, input().split())
    on.append(b)
    off.append(a)

passenger = []
for idx in range(10):
    if idx!=0:
        passenger.append(passenger[idx-1]-off[idx]+on[idx])
    elif idx==0:
        passenger.append(on[idx])
    else:
        passenger.append(passenger[idx-1]-off[idx])

print(max(passenger))
