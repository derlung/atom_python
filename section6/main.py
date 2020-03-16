import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import re
import datetime
from lib.YouView_layout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
from PyQt5 import QtWebEngineWidgets
import re
import datetime

# form_class = uic.loadUiType('D:/atom_python/section6/lib/YouView.ui')[0]


class Main(QMainWindow,Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__()#부모의 생성자 함수 호출
        self.setupUi(self) #함수선언
        #인증버튼 이벤트 전
        self.initAuthLock()
        #인증버튼 이벤트 후
        self.initAuthLockActive()
        #시그널 초기화작업
        self.initSignal()
        #로그인 관련 변수 선언
        self.user_id=None
        self.user_pw=None

    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamComboBox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg("인증안됨")


    #기본 UI 활성화
    def initAuthLockActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamComboBox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg("인증완료")

    def showStatusMsg(self,msg):
         self.statusbar.showMessage(msg)

    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)

    @pyqtSlot()#명시적 표현
    def authCheck(self):
        pass

if __name__=="__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
