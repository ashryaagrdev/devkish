T = int(input())
for _ in range(T):
    n, m = input().split()
    n, m = int(n), int(m)
    if n%2==0 or m%2==0 :
        print("YES")
    else :
        print("NO")