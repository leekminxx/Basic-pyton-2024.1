#desc : 구구단 프로그램 
#spec : for 문 잘 써야함 . 2중 for 문의 이해 

# 2 x 1 = 2 , 2 x 2 = 4 , 2 x 3 = 6 , 2 x 4 = 8 ... 2 x 9 = 18


print('구구단 시작 !')
x = 2 
for x in range(2, 10):
    print(f'{x} 단 ---- > ')
    for y in range(1 , 9):
        print(f'{x}x{y} = {x*y:2d}' , end= ' ')
    print() 






# # debugging
#     #F9(종단점 토글) , F5(디버깅시작), F10(한줄씩 실행) , F11(함수안으로 진입)
#     #Shift + F5(디버깅종료)
#     print('구구단 시작 !')
#     x = 2 
#     for x in range(2, 9+1): # 2부터 9까지 반복 
#         print(f'{x} 단 ---- > ') 
#         for y in range(1 , 9+1): # 1부터 9까지 반복
#             print(f'{x}x{y} = {x*y:2d}' , end= ' ') # end = 엔터대신 공백으로 변경
#         print() # 안쪽 for 문이 끝나면 마지막 엔터를 하나 추가