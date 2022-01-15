時 = int(input())
分 = int(input())
總分鐘數 = 時 * 60 + 分
if 總分鐘數 >= 7*60+30 and 總分鐘數 < 17*60:
    print('At School')
else:
    print('Off School')