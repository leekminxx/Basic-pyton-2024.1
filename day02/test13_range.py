# file : test13_range.py
# desc : 리스트 범위지정

list_a = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

print(list_a)

#범위 지정 range(n) , 0부터 n개의 범위 수를 생성
print(list(range(5)))
print(list(range(1,6))) # 1~5 
print(list(range(2, 21 , 2))) #마지막 2는 짝수 나오게 하는거  , 2부터 21까지 2씩증가 
print(list(range(1, 20 , 2))) #1부터 19까지 2씩 증가 
# print(range(10,5)) 이렇게 하면 안나옴  list 붙이기

list_a = list(range(1,10))
print(list_a)

list_a = [i for i in range(1,10)]  #리스트 컨프리헨션 
print(list_a)















