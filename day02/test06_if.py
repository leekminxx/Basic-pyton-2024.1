# date : 20240130
# desc : 여러조건 if 문

date = input('skfWK dlqfur(예 : 12 - 31) > ')

month = date.split('-')[0] #'12'
day = date.split('-')[1] # '31'

if month == 12 and day == '25' : # 12월 25일 
    print('메리크리스마스!!')
elif month == '01' and day == '01':
    print('해피 뉴이어~!!')
elif month == '04' and day == '14':
    print('짜장면')
else:
    print('보통날입니다')





