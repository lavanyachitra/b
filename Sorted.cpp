#include<io.stream.h>
#include<conio.h>
typedefpair<int,pair<int, int> >ppi;
vector<int> mergeArrays(vector<vector<int>>arr)
{
vector<int> output;
priority<ppi,vector<ppi>,greater<ppi> >pq;
for(int i=0;i<arr.size();i++)
pq.push({arr[i][0],{i.o}});
while(pq.empty()==false)
{
pq.pop();
int i=curr.second.first;
int j=curr.second.second;
output.push(curr.first);
if(j+1<arr[i].size())
pq.push({arr[i][j+1],{i,j+1}});
}
return output;
}
int main()
{
vector<vector<int>>arr{ {2,6,12},{1,9},{34,78,100,900}};
vector<int> output=mergeArrays(arr);
cout<<"merged array is"<<endl;
cout<<x<<" ";
return 0;
}

