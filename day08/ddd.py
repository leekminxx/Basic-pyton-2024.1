





# # # def print_multiplication_table(number):
# # #     print(f"{number}단을 출력합니다:")
# # #     for i in range(1, 10):
# # #         result = number * i
# # #         print(f"{result}", end ='   ')

# # # # 사용자로부터 단번호 입력 받기
# # # while True:
# # #     try:
# # #         user_input = int(input("구구단을 출력할 단번호를 입력하세요 (1부터 9까지): "))
# # #         if 1 <= user_input <= 9:
# # #             break
# # #         else:
# # #             print("1부터 9까지의 숫자를 입력하세요.")
# # #     except ValueError:
# # #         print("숫자만을 입력하세요.")

# # # # 입력받은 단번호로 구구단 출력
# # # print_multiplication_table(user_input)





# # def process_string(input_string):
# #     # 단어 수 세기
# #     word_count = len(input_string.split())

# #     # 짝수 번째 단어 대문자로 변경
# #     words = input_string.split()
# #     modified_words = [word.upper() if i % 2 == 1 else word for i, word in enumerate(words)]
# #     modified_string = ' '.join(modified_words)

# #     return word_count, modified_string

# # # 사용자로부터 문자열 입력 받기
# # user_input = input("영어 문자열을 입력하세요: ")

# # # 입력된 문자열의 단어 수 및 짝수 번째 단어 대문자로 변경하여 출력
# # word_count, modified_string = process_string(user_input)

# # print(f"입력된 문자열의 단어 수: {word_count}")
# # print(f"짝수 번째 단어 대문자로 변경된 문자열: {modified_string}")





# # def counting(input_str):
# #     english_count = len(input_str.split())

# #     english_count = input_str.split()
# #     two_words = [word.upper() if i % 2 == 1 ]


    





# # 4번 문제 - 함수 구현?
# from urllib.request import Request, urlopen

# def get_url(url):
#     web_sites = {'google' : 'https://www.google.com/',
#                  'naver' : 'https://m.naver.com/',
#                  'python' : 'https://www.python.org/',
#                  'github' : 'https://github.com/'}
    
#     if url in web_sites:
#         return web_sites[url]
#     else:
#         print('현재의 딕셔너리에서는 찾을 수 없습니다.')

# url = input('영문 이름 입력 (ex -> google)')
# get_url(url)

a





# # def get_url(english_name):
# #     # 기본 도메인
# #     base_domain = "www."

# #     # 입력된 영문 이름을 소문자로 변환하여 도메인에 추가
# #     website_url = base_domain + english_name.lower() + ".com"

# #     return website_url

# # # 사용자로부터 영문 이름 입력 받기
# # user_input = input("영문 이름을 입력하세요: ")

# # # 입력된 영문 이름에 대한 웹사이트 주소 출력
# # url = get_url(user_input)
# # print(f"{user_input}의 웹사이트 주소: {url}")




# # # 2번 문제

# def dic(english):
#     planet = {'Mercury': '수성','Venus': '금성','Earth': '지구',
#     'Mars': '화성','Jupiter': '목성','Saturn': '토성','Uranus': '천왕성','Neptune': '해왕성'
#     }
#     # 대소문자 구분 없이 검색
#     korean = planet.get(english.capitalize())
    
#     if korean:
#         return korean
#     else:
#         return '영어로 입력해주세요.'

# # 사용자로부터 이름 입력 받기
# english_name = input('행성의 영어 이름을 입력하세요: ')
# korean = dic(english_name)

# print(f'{english_name}의 영어 이름은 {korean}입니다.')


def short(url1):
    url = {'goole':'www.goole.com' ,
            'naver':'www.naver.com',
            'youtube':'www.youtube.com'}
    url_f = url.get(url1.capitalize())

    if url_f:
        return url_f
    else:
        return '제대로 입력해주세요'

    result_url = input('영문이름을 입려하시오 > ')
    url_f =short(result_url)
    print(f'{url_f}')




















