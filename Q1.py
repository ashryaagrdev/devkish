def computeXOR(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0
T = int(input())
for i in range(T):
    L, R = [int(i) for i in input().split()]
    if (computeXOR(R)^computeXOR(L-1))%2==0 :
        print("Even")
    else :
        print("Odd")