# for i in range(1,9+1) :
#     print(N,"*",i,"=",N*i)
# , 를 사용하면 자동으로 띄워쓰기가 한 칸 들어간다. 

n = int(input())

for i in range(1,10):
    print(str(n) + ' * ' + str(i) + " = " + str(n*i))
