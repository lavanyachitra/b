def findRepeating(ar,low,high):
    iflow>high:
        return-1
mid=(low+hyigh)/2
if(ar[mid]!=mid+1):
   if(mid>0 and ar[mid]==ar[mid-1]):
       return mid
    return findRepeating(ar,mid+1,high)
ar=[1,2,3,4,5]
n=len(ar)
index=findReapting(ar,0,n-1)
if(index is not-1):
   print ar[index]
