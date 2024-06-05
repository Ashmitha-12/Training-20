#include<stdio.h>
int main()
{
	int a,count=0;
	scanf("%d",&a);
	while(a>0)
	{
		if(a&1)
		{
			count++;
			
		}
		a=a>>1;
	}
	printf("count set bits=%d",count);
}
