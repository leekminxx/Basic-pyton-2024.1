
# en  = input("영단어를 입력하시오")
# print(len(en))
# for i in range(0 , en(len))







s = input('영단어를 입력하시오')
print(len(s))

def solution(s):
    answer = ""
    arr = s.split(' ')
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if(j%2==0):
                answer += arr[i][j].upper()
            else:
                answer += arr[i][j].lower()
        answer += ' '
    answer = answer[:-1]
    return answer

print(solution(s))




def get_url(english_name):
    base_domain = "www."
    top_level_domain = ".com"
    website_url = base_domain + english_name.lower() + top_level_domain
    return website_url

# 사용자로부터 영문 이름 입력 받기
user_input = input("영문 이름을 입력하세요: ")

# 입력된 영문 이름에 대한 웹사이트 주소 출력
url = get_url(user_input)
print(f"{user_input}의 웹사이트 주소: {url}")





def get_url(english):
    first = 'www'
    last = 'com'
    add = first + english.lower() +last
    return add

input_1 = input('영문이름을 입력:')

url = get_url(input_1)
print(f'{input_1} 의 웹사이트 주소는{url}입니다')