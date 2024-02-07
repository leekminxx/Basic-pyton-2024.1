

def get_url(english):
    first = 'www.'
    last = '.com'
    add = first + english.lower() +last
    return add

input_1 = input('영문이름을 입력:')

url = get_url(input_1)
print(f'{input_1} 의 웹사이트 주소는{url}입니다')