def make_burger(level,cur_burger):
    global cnt

    if level == N:
        for i in cur_burger[:X]:
            if i == 'P':
                cnt+=1
        return

    if level < N:
        make_burger(level+1,['B']+cur_burger+['P']+cur_burger+['B'])


N, X = map(int, input().split())
burger = ['P']
cnt = 0
make_burger(0,burger)
print(cnt)














