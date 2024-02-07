# 2번 문제

def exchange(english_name):
    planet_names = {'Mercury': '수성','Venus': '금성','Earth': '지구',
    'Mars': '화성','Jupiter': '목성','Saturn': '토성','Uranus': '천왕성','Neptune': '해왕성'
    }
    # 대소문자 구분 없이 검색
    korean_name = planet_names.get(english_name.capitalize())
    
    if korean_name:
        return korean_name
    else:
        return '영어로 입력해주세요.'

# 사용자로부터 영어 행성 이름 입력 받기
user_input = input('행성의 영어 이름을 입력하세요: ')
korean_name = exchange(user_input)

print(f'{user_input}의 영어 이름은 {korean_name}입니다.')





 # .get(english_name.capitalize())