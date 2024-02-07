# file : test38_pyqt.py
# desc : Qt디자이너 만든 ui와 연동

import sys
from PyQt5 import QtGui , QtWidgets , uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget): ##상속
    def __init__(self) -> None: # x버튼 종료확인
        super().__init__()
        uic.loadUi('./day06/TestApp.ui',self)  # QtDesigner에서 만든 ui를 로드
        # 버튼에 대한 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내에 있는 윗제접근은 VSCode상에서 색상으로 표시X
        self.btnStop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self):
        print('시작버튼 클릭')
        self.lblStatus.setText('상태 : 동작시작')
        QMessageBox.about(self ,'동작' , '***시스템이 시작되었습니다')

    def btnStopClicked(self):
        print('종료버튼 클릭')
        self.lblStatus.setText('상태: 동작중지')
    # QWidget에 있는 closeEvent를 그대로 쓰면 그냥 닫힘 
    # 닫을지 말지를 한번더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)      
    def closeEvent(self, QCloseEvent) -> None:
       re = QMessageBox.question(self , '종료확인' , '종료할래?' , QMessageBox.Yes|QMessageBox.No)
       if re == QMessageBox.Yes: #닫기
           QCloseEvent.accept()
       else:
           QCloseEvent.ignore()

if __name__ == '__main__':
    loap = QApplication(sys.argv)  # 내 소스의 위치로 앱을 생성할꺼야 loap 무한루프
    instance = qtwin_exam() #QWiidget을 상속한 qtwin_exam 객체를 생성
    instance.show()
    loap.exec_()
    
































