def check_prime(num):
    if num==0:
        return 0
    flag=0
    for i in range(2,num//2):
        if num%i==0:
            flag=1
    if flag==0:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
    
num=7
check_prime(num)