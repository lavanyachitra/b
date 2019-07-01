num=int(input())-1
x=list(map(int,input().split()))
x=x[::-1]
for i in range(n):
    print(x[i],end='->')
print(x[n])  
  
