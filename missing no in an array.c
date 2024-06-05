//find the 1 missing number in an 'n' array
#include<stdio.h>
int main()
{
	int a[]={1,2,3,4,5,7};
	int x=0,i=0;
	for(i=0;i<=6;i++)
	x=x^i;
	for(i=0;i<6-1;i++)
	x=x^a[i];
	printf("%d",x);
}
