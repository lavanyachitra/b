#include<iostream.h>
#include<conio.h>
char *remove(char str[],int n)
int index=0;
for(i=o;i<n;i++)
{
int j;
for(j=0;j<i;j++)
if(str[i]==str[j])
break;
if(j==i)
str[index++] = str[i];
}
return str;
}
int main()
char str[]="aabbbabb";
int n=sizeof(str)/sizeofstr[0]);
cout<<remove(str,n);
return 0;
}


