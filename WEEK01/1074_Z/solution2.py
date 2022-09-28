import sys
import math

def recur(N, r, c, cnt):
    side_len = pow(2,N)

    if N == 1:
        if r < side_len/2 and c >= side_len/2:
            cnt += 1
        elif r >= side_len/2 and c < side_len/2:
            cnt += 2
        elif r >= side_len/2 and r >= side_len/2:
            cnt += 3
        print(int(cnt))
        return

    previous =  side_len/2 * side_len/2

    if r < side_len/2 and c >= side_len/2:    
        cnt += previous
        c -= side_len/2

    elif r >= side_len/2 and c < side_len/2:
        cnt += previous * 2
        r -= side_len/2

    elif r >= side_len/2 and c >= side_len/2:
        cnt += previous * 3
        c -= side_len/2
        r -= side_len/2

    return recur(N-1, r, c, cnt)

if __name__ == "__main__":
    N, r, c = map(int, sys.stdin.readline().split())
    recur(N, r, c, 0)
    