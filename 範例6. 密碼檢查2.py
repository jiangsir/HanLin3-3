password = '137'
for i in range(3):
    if input('請輸入密碼: ') == password:
        print('歡迎使用本系統')
        break
else:
    print(f'密碼錯誤 {i+1} 次，帳號已被鎖定')
