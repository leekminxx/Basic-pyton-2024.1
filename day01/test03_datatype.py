# date : 20240129
# desc : 자료형

## 기본자료형 - 숫자형 , 문자형 , 불형 , None형 
## 추가자료형 - 리스트형 , 튜플형 ,  딕셔너리 , 집합.... 

## None형 == null(c , c++ , c# , Java , SQl)
## 값은 값인데 아무것도 지정할 수 없는 값 = > ( None은 없다라는 뜻 특수형 값이 없는것도 아니고 비어있는것도 아님 몇개담을지 모름 ) 담을수가없음 None 도 값

apple = None
print(apple)

## 숫자형 - 정수형 , 실수형 , 진수 형
### 정수
ten = 10
hundred = 100
temp = -8

### 실수 
pi = 3.141592
tax_rate = 10.0
emp_earn_rate = 3.3
test_val = 2e10   # 제곱 
print(test_val)

### 진수 (2 , 8 , 16진수)
bit8 = 0b10001110       

oct9 = 0o10
hex255 = 0xff 
print(bit8)
print(oct9)
print(hex255)

## 문자형 - 파이썬에는 문자 , 문자열 차이가 없음 
greeting = 'Hello!'
greeting = "Hello!"
print(greeting)
multi_str = '''hello
i am a porgrammer.
have a good afternoon'''
print(multi_str)
multi_str2 = ('Line1\n'
              'Line2\n'
              'Line3')
print(multi_str2)


## 불형 
isCheck = False
print(isCheck)

isCheck = True
print(isCheck)

answer = (3==6)
print(answer)
answer = (3.0 == 3)
print(answer)

print(type(apple))
print(type(hundred))
print(type(test_val))
print(type(hex255))
print(type(greeting))
print(type(isCheck))




























