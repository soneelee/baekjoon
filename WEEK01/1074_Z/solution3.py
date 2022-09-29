import sys

def recur(N, r, c, count):

    side_len = 2**N

    previous = side_len/2 * side_len/2

    if N == 1:
        if r < side_len/2 and c >= side_len/2:
            count += 1
    
        elif r >= side_len/2 and c < side_len/2:
            count += 2
        
        elif r >= side_len/2 and c >= side_len/2:
            count =+ 3
    return


    if r < side_len/2 and c >= side_len/2:
        count = previous * 1
        c -= side_len/2

    elif r >= side_len/2 and c < side_len/2:
        count = previous * 2
        r -= side_len/2

    elif r >= side_len/2 and c >= side_len/2:
        count = previous * 3
        c -= side_len/2
        r -= side_len/2

    return recur(N-1, r, c, 0 )

N, r, c = map(int, sys.stdin.readline().split())

recur(N, r, c)