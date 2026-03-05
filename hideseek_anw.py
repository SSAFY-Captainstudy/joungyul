from collections import deque
N, M = map(int, input().split()) # N 수빈 M 동생M
queue = deque()
queue.append(N)
time = [-1]*(100000 + 1)
time[N] = 0

while queue:
    x = queue.popleft()

    if x == M:
        print(time[x])
        break

    direct = [(x*2),(x-1),(x+1)]
    for nx in direct:
        if 0 <= nx <= 100000 and time[nx] == -1:
            if nx == (x*2):
                time[nx] = time[x]
                queue.appendleft(nx)
            else:
                time[nx] = time[x] + 1
                queue.append(nx)
