# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWinMenuToolbar

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    myUi = MainWinMenuToolbar.Ui_MainWindow()
    myUi.setupUi(myMainWindow)
    myMainWindow.show()
    sys.exit(app.exec_())