#include<stdio.h>
long long factorial(long long int n)
{
	if(n==0)
	{
		return 1;
	}
	else
	{
		return(n*factorial(n-1));
	}
}
int main()
{
	long long int n;
	long long fact;
	scanf("%lld",&n);
	fact=factorial(n);
	printf("factorial of %lld=%lld",n,fact);
	return 0;
}
