# x,y,w,h=map(int,input().split())
# print(min(x,y,w-x,h-y))

x, y, w, h = map(int,input().split())

if 1 <= w <= 1000 and 1 <= h <= 1000 and 1 <= x <= w-1 and 1 <= y <= h-1:
    if x < w-x:
        min_x = x
    else:
        min_x = w-x

    if y < h-y:
        min_y = y
    else:
        min_y = h-y

    if min_x < min_y:
        print(min_x)
    
    else:
        print(min_y)