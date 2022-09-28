num = int(input())
count = 0

if num <= 99:
    count = num

else:
    count = 99
    for n in range (100, num+1):
        a = n//100
        b = (n%100)//10
        c = (n%100)%10

        if 2*b == a+c:
            count += 1

print(count)