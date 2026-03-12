import sys
sys.stdin = open("jh_input.txt", "r")

def janghoon(cnt,start,current_sum):
    global dif_height

    if current_sum >= B:
        if current_sum - B < dif_height:
            dif_height = current_sum - B
        return
    # if cnt == N:
    #     return

    for i in range(start,len(arr)):
        janghoon(cnt+1,i+1,current_sum+arr[i])



T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    dif_height = float('inf')
    janghoon(0,0,0)
    print(f'#{tc} {dif_height}')













