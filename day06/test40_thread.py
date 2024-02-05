# file : test40_thread.py
# desc : Qt에서 스테드 업싱 동작 테스트 

import sys
from PyQt5 import QtGui , QtWidgets , uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class backWorker(QThread): # PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) #시그널을 UI 스레드로 전달하기 위한 변수객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)
    
    def __init__(self, parent) -> None:
        super().__init__(parent) # 
        self.parent = parent #backWorker 에서 사용할 멤버변수 

    def run(self) -> None: #스레드 실행
        #스레드로 동작할 내용
        maxVal = 100000000
        self.initSignal.emit(maxVal)
        # self.parent.pgbTask.setValue(0) #프로그레스바 0부터 시작 !!QThread에선 UI관련된 처리를 할 수 없음 
        # self.parent.pgbTask.setValue(0 , maxVal-1) #프로그레스바 0부터 시작
        for i in range(maxVal):
            print_str = f'쓰레드 출력>> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            # self.parent.txbLog.append(print_str)
            # self.parent.pgbTask.setValue(i)

class qtwin_exam(QWidget):
    def __init__(self) -> None: # x버튼 종료확인
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui',self)  # QtDesigner에서 만든 ui를 로드
        # 버튼에 대한 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내에 있는 윗제접근은 VSCode상에서 색상으로 표시X
         
    def btnStartClicked(self):
        th = backWorker(self)
        th.start() #backWorker 내의 self.run() 실행
        th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리 
        th.setSignal.connect(self.setPgbTask)
        th.setLog.connect(self.setTxbLog) # TextBrowser 위젯에 진행사항 출력




    def closeEvent(self, QCloseEvent) -> None: #x버튼 종료확인
        re = QMessageBox.question(self , '종료확인' , '종료할래?' , 
        QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    # 스테드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 슬롯함수
    @pyqtSlot(int) #backWorker 스레드에서 #self.setLog.emit() 동작해서 실행
    def initPgbTask(self , maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0 , maxVal -1)

    @pyqtSlot(str) #backWorker 스레드에서 #self.setsignal.emit() 동작해서 실행
    def setTxbLog(self , msg):
        self.txbLog.append(msg)

    @pyqtSlot(int)
    def setPgbTask(self , val):    
        self.pgbTask.setValue(val)

if __name__ == '__main__':
    loap = QApplication(sys.argv)  # 내 소스의 위치로 앱을 생성할꺼야 loap 무한루프
    instance = qtwin_exam() #QWiidget을 상속한 qtwin_exam 객체를 생성
    instance.show()
    loap.exec_()







    