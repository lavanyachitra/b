from collections import Counter
z=int(input())
x=list(map(int,input().split()))
y=Counter(x)
list=[]
for a in y.items():
  if(a[1] != 1):
    print(a[0],end = " ")
for b in y.items():
  list.append(b[1])
if(max(list) == 1):
  print("unique")
