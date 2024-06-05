//determine a number is power of 2 or not
//class work:determine a number is power of 4 or not
#include<stdio.h>
#include<math.h>
int main()
{
	int n,count=0;
	scanf("%d",&n);
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	if(count==1)
	{
		printf("yes");
	}
	else
	{
		printf("no");
	}
	
}
