x=int(input())
v=0
for k in range(2,x):
 if(x%k==0):
  v=v+1
if(v<=0):
 print("yes")
else:
 print("no") 
