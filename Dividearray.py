a=int(input())
l=[int(x) for x in input().split()]
av=int(a/2)
l1=l[:av]
l2=l[av::]
n1=sum(l1)//len(l1)
n2=sum(l2)//len(l2)
if n1==n2:
    print("yes")
else:
    print("no")
      
    
