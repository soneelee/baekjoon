import sys

def hanoi(N, start, end, other):
    global k
    if N == 1:
        print(start, end)
        return
    
    k += 1
    hanoi(N-1, start, other, end)
    print(start, end)
    hanoi(N-1, other, end, start)

    return


# main

N = int(sys.stdin.readline())

k = 0
print(2**N- 1)
start = 1
other = 2
end = 3

hanoi(N, start, end, other)



