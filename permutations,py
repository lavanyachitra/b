def toString(list):
   return ' '.join(list)
def permute(a,l,d):
   if l == d:
       print toString(a)
   else:
       for i in xrange(l,d+1):
           a[l],a[i] = a[i],a[l]
           permute(a,1+1,d)
           a[l],a[i]=a[i],a[l]
 string="ABC"
 n=len(string)
 a=list(string)
 permute(a,0,n-1)
    
   
   
