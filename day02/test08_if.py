# desc : 홀수 / 짝수 구분 

number = int(input('정수입력 > ')) #입력받은 후 정수로 변경

if number % 3 == 0: #배수를 입력받을 때 사용 
    print('3의배수')
else: 
    print('나머지 수')
