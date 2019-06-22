zx=int(input())-1
p=list(map(int,input().split()))
s=0
p.sort()
for i in range(zx,-1,-1):
	s=s*10+p[i]
print(s)
