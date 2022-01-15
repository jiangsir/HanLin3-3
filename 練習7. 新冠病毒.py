n = int(input())
x = int(input())
ans = 0
while n < x:
    ans += 1
    n *= 3
print(ans)