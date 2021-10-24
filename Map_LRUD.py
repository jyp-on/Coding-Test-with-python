n = int(input())
plans = input().split()
x, y = 1, 1

#    L   R   U  D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(types)):
        if plan == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x, y = nx, ny

print(x, y)
