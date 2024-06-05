a=input()
b=int(input())
M=(ord(a)+b)
if(M<122):
    print(chr(M))
else:
    N=(M-26)
    print(chr(N))