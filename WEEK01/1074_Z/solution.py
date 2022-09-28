import sys
import math

def recur(side_len, cnt, r, c):
    if (side_len == 2):
        r_mod = r % 2
        c_mod = c % 2
        if r_mod == 0 and c_mod == 1:
            cnt += 1
        elif r_mod == 1 and c_mod == 0:
            cnt += 2
        elif r_mod == 1 and c_mod == 1:
            cnt += 3
        print(int(cnt))
        return 

    previous = (side_len / 2) * (side_len / 2)

    if r < side_len / 2 and c >= side_len / 2:
        cnt += previous
        c -= side_len / 2

    elif r >= side_len / 2 and c < side_len / 2:
        cnt += previous * 2
        r -= side_len / 2

    elif r >= side_len / 2 and c >= side_len / 2:
        cnt += previous * 3
        r -= side_len / 2
        c -= side_len / 2

    recur(side_len / 2, cnt, r, c)

if __name__ == "__main__":
    N, r, c = map(int, sys.stdin.readline().split())
    side_len = math.pow(2, N)
    cnt = 0
    recur(side_len, cnt, r, c)


