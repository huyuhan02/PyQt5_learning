# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import FirstMainWindow  #主窗口的文件名为FirstMainWindow.py

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    myUi = FirstMainWindow.Ui_MainWindow()
    myUi.setupUi(myMainWindow)
    myMainWindow.show()
    sys.exit(app.exec_())