import java.*;
import java.util.Arrays;
class Largest
static int findMax(int ar[],int n)
{
Arrays.sort(ar);
int num =ar[0];
for(int i=n-1;i>=0;i--)
{
num = num*10+ar[i];
}
return num;
}
public static void main(String[] args)
int ar[]={1,2,3,4,5,0};
int n =ar.length;
System.out.println(findMax(ar,n));
}
