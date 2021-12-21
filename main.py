from modules.ui_back import Ui_backend
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
mainWin = QtWidgets.QMainWindow()
ui = Ui_backend()
ui.setupUi(mainWin)
mainWin.show()
sys.exit(app.exec_())