'''
n=input()
i=0
j=len(n)-1
while(i<j):
    if(n[i]!=n[j]):
        print("not palindrome")
        break;
    else:
        print("palindrome")
        break;
'''
s=input()
i=0
j=len(s)-1
while(i<j):
    if s[i]!=s[j]:
        print("false")
        break
    i+=1
    j-=1
else:
        print("true")