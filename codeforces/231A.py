count = int(input())
sum = 0 
for i in range(count) :
    p,v,t = input().split()
    check = int(p) + int(v) + int(t)
    if check >= 2 :
        sum += 1
print (sum)