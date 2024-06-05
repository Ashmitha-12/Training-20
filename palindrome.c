#include<stdio.h>
int main()
{
	int str,r,sum=0,n,i,temp;
	scanf("%s",str);
	while(str!='\0')
	{
		r=n%10;
		sum=(sum*10)+r;
		n=n/10;
	}
	temp==n;
	if(temp==sum)
	{
		printf("palindrome");
	}
	else
	{
		printf("not palindrome");
	}
}
