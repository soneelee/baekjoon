a = input().split()

x = a[0]
y = x[2]+x[1]+x[0]

z = a[1]
w = z[2]+z[1]+z[0]

if int(y) > int(w):
    print(y)
else:
    print(w)

