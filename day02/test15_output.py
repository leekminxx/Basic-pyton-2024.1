# file : test15_output.py
# desc : 콘솔 출력 포맷양식 String Format

string_1 = '{}'.format(10)  #위치에 함수 뒤에 들어있는 값을 치환 , 원하는 양식으로 표현 
print(type(string_1))

name = input('이름 입력 > ')
string_2 = '안녕하세요 , {} 입니다!'.format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000,'만' , ' 빌려주세요 ')
print(string_3)
#정수를 문자열포맷 
#= : 기호와 숫자를 분리 ,  !! 중요 02d : 두자리 만들때 빈자리 0으로 채우기 , d : 정수 
string_4 = '_____{:+010d}_____'.format(-100)
print(string_4)
#실수 문자열포맷 f = 기본소수점 6자리 
string_5 = '_________{:016f}_________'.format(78.3333333333333)
#string_5 = '_________{:.2f}_________'.format(78.3333333333333) 소숫점 둘째에서 자른다
#string_5 = '_________{:7.2f}_________'.format(78.3333333333333) 전체자리수를 7자리로 , 소숫점 뒤는 2자리로 픽스 정하겠다 


# print(string_5)
# value = 55.4
# string_6 = '{:g}'.format(55.4)
# print(string_6)




val = 78.33333333333
string_6 = f'_________{78.33333333333333}____________'
print(string_6)

#파이썬 3.6이후 도입 . format() 함수를 아예안함 
string_6 = f'__________{val:7.2f}________'
print(string_6)

string_7 = 'Hello World!'
print(string_7.upper()) #upper case 대문자변환 
print(string_7.lower()) #모두 소문자로 
print(string_7.lower().capitalize()) #앞머리만 대문자로 
print(string_7.split(',')) # 특정한 단어로 자르는 함수 

string_8 ='Hello i am lee kyeong . i am a lecturer. good luck for your day'
words = string_8.split(' ')
print(words)
print(len(words)) #단어의 개수는 
print(f'문장의 단어 갯수는 {len(words)} 개 입니다. ')

strint_9 ='A10'
print(strint_9.isalnum()) #True 
print(strint_9.isnumeric()) #False 알파벳
string_10 = '10.5' #소수점은 함수를 만들어서 처리해야....
print(string_10.isdigit()) #False 

print('안녕' in ' 안녕하세요') #문장안에 단어가 있는지 확인 







