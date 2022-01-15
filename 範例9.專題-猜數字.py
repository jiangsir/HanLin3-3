import random
ans = random.sample(range(1, 10), 4) # 產生四個0~9不重複數字
count = 0
while count < 8:
    guess = list(map(int, input('請輸入4個1~9的不同數字並以空白隔開: ').split()))
    count += 1
    a = b = 0
    for i in range(4):
        if ans[i] == guess[i]:
            a = a + 1
        elif guess[i] in ans:
            b = b + 1
    if a == 4:
        print(f'共猜{count}次，正確答案為 {ans}')
        break
    else:
        print(f'{a}A{b}B')
else:
    print('超過 8 次，遊戲結束')
