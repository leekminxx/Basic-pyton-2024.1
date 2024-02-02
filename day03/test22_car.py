# file : test22_car.py
# desc : Car 클래스 만들기 
class Car:
    whell_num = 4
    color = 'white'
    __plate_num = ' '  ##__써줌 
    company = ' '
    gear_type = ''

    # 전진 , 후진 , 좌회전 , 우회전 , 
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveback(self):
        print(f'{self.__plate_num}이 후진합니다.')

    def moveleft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')

    def movelight(self):
        print(f'{self.__plate_num}이 우회전합니다.')

    def __init__(self , number , company , color , gear) -> None:
     self.__plate_num = number
     self.company = company
     self.color = color
     self.gear_type = gear

    def __str__(self) -> str: #print(객체) 출력되는부분
        return f'제 차는{self.__plate_num}입니다. {self.color}입니다.'

    def getPlateNumber(self): #외부에서는 접근 할 수 없도록 막는조치 
        return self.__plate_num
    
    def setPlateNaumber(self , new_plateNumber):
        self.__plate_num = new_plateNumber

sarah = Car('04모 3053' , '현대자동차' , '흰색' , '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있습니다.
print(sarah)
print(f'차번호는{sarah.getPlateNumber()}')
print(f'차색상은{sarah.color}')
sarah.moveForward()

sarah.__plate_num = '98하 7789' #악의적인 의도를 가지고 변경
print(sarah)
sarah.setPlateNaumber ('04모3053')                                                      ##캡슐화 인캡슐레이션
print(sarah)
# csuv = Car('경남88 1922 ' ,'기아자동차' , '회색' , '자동')
# print(f'차번호는{csuv.plate_num}')


















