# file : test36_pyqt.py
# desc : PyQt5 기본화면 만들기 

import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPaintEvent, QPainter , QColor , QFont

from PyQt5.QtWidgets import QApplication , QWidget
# print(sys.argv)

class qtwin_exam(QWidget): #QWidget을 상속받을거야 , QWidget이 가진 모든것을 사용할 수 있다
    # 생성자
    def __init__(self, ) -> None:
        super().__init__()
        self.initUI()  # 화면초기화 함수를 호출 

    def initUI(self):
        self.setGeometry((1920 - 400)//2 , (1080-300)//2 , 400, 300) # x , y , width , height
        self.setWindowTitle('Qt5 Hello World!')
        self.text = ''
        self.show()

    def drawText(self, event , paint):
        paint.setPen(QColor(10 , 10 , 10)) #0~255로 표현 
        paint.setFont(QFont('NanumGothic' , 15))
        paint.drawText(300//2 , 300//2 , 'HELL WORLD!')
        paint.drawText(event.rect() , Qt.AlignCenter , self.text) #AligrLeft , AlignCenter , AlignRight

    def paintEvent(self, event ) -> None: #재정의(Override) 부모함수를 재정의 
        paint = QPainter()
        paint.begin(self) #열면
        self.drawText(event , paint)
        paint.end() #닫아줘야 함 


loap = QApplication(sys.argv)  # 내 소스의 위치로 앱을 생성할꺼야 loap 무한루프
instance = qtwin_exam() #QWiidget을 상속한 qtwin_exam 객체를 생성
loap.exec_()
































