N, M = map(int, input().split())  # N 수빈 M 동생
tree = []


def plus(N):
    p = N + 1
    return p


def minus(N):
    n = N - 1
    return n


def multiple(N):
    m = N * 2
    return m


def triple(x):
    x_p = plus(x)
    x_n = minus(x)
    x_m = multiple(x)


cnt = 0


def anw(N, M):  # 5,17

    anw = []

    anw.append(M)  # anw = [17]
    cnt = 0
    while anw:
        if N == M:
            anw.pop()

        p = plus(N)
        n = minus(N)
        m = multiple(N)
        tree.append(p)
        tree.append(n)
        tree.append(m)

        if p or n == M:
            cnt += 1
            anw.pop()

        elif m == M:
            anw.pop()

        else:
            triple(p)
            triple(n)
            triple(m)

        for i in tree:

    return cnt


print(cnt)
