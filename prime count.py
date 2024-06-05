def prime_count(num):
    prime=[True]*(num+1)
    p=2
    count=0
    while(p*p<=num):
        if prime[p]:
            for i in range(p*p,num+1,p):
                prime[i]=False
        p+=1
    for p in range(2,num+1):
        if prime[p]:
            count+=1
    print(count)
            #print(p,end=" ")
num=int(input())
prime_count(num)