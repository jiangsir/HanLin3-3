n = int(input('請輸入數字n:'))

ans = 1
for i in range(1, n+1):
    ans = ans * i
print(f'1*2*3...*{n}={ans}')
