//find the lonely integer in an array
#include <stdio.h>
int main()
{
	int n,i;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	int res=0;i=0;
	for(i=0;i<5;i++)
	{
		res=res^a[i];
	}
	printf("%d",res);
}
