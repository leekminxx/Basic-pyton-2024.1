# file : test14_while.py
# desc : while 문

## while 참인조건 : 
## 공통점 if 조건 : elif 조건 : else : , for in range(): , while 조건 :
count = 0

#while count <= 10:
#무한루프 : Windows Os , 모바일 Os , 자동차네비게이션 , 라즈베리파이 , 아두이노 ,게임 , winform 개발 
while True : 
    count = count + 1
    print('나무찍기' , count )
    if count == 10 :
        break # 반복문 탈출 

number = 1 

while True : 
    number = number + 1
    if str(number).count('3') >= 1 or \
        str(number).count('6') >= 1 or \
        str(number).count('9') >= 1:
        print('짝!') # continue로 변경 
        # continue는 단복에서 제외 
    else: 
        print(number)

    if number == 31: break  # 반복문을 완전히 빠져나감



    