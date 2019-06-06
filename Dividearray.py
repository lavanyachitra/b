def findSplit(ar,n):
    leftSum=0
    for i in range(0,n):
        leftSum +=ar[i]
        rightSum=0
    for j in range(i+1,n):
         rightSum +=ar[j]
    if(leftSum == rightSum):
         return i+1
    return-1
 def printTwo(ar,n):
      splitp=findSplit(ar,n)
      if(splitp ==-1 orsplitp == n):
            print("not possible)
            return
      for i  in range(0,n):
         if(splitp==i):
            print("")
         print(str(ar[i])+' ',end= ' ')
 ar=[1,2,3,4,5,6]
 n=len(ar)
 printTwo(ar,n)
         
         
      
    
