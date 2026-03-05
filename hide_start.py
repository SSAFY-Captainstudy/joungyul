import math
N, M = map(int, input().split()) # N 수빈 M 동생

t = int(math.log2(100000)) #16
real_N = 0 #걷기 전 순간이동을 완료한 수빈의 위치
walk_d = abs(real_N - M)
 #tp와 tp_2사이에 M이 있음


if N < M: #수빈이가 동생보다 뒤에있으면
    for i in range(1,t):
        if N*(2**i) > M:
            tp_cnt = i
            break
# print(tp_cnt) 5 17 tp_cnt = 2
tp = N*(2**tp_cnt)
tp_2 = N*(2**(tp_cnt-1))
# print(tp)

if tp - M <= M - tp_2:
    time = tp - M
else:
    time = M - tp_2

print(time)