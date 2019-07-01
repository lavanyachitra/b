x=int(input())
u=list()
for i in range(x):
    o=input().split()
    o=[int(d) for d in o]
    for j in o:
        u.append(j)
u.sort()
for i in u:
    print(i,end=" ")
