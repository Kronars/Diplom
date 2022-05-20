from modules.ui_interaction import Ui_backend
from PyQt5 import QtWidgets
import sys

# pyuic5 C:\Users\Senya\Prog_2\Diplom_rework\main_win.ui -o C:\Users\Senya\Prog_2\Diplom_rework\modules\main_window.py

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_backend()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())