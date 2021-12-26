from modules.ui_back import Ui_backend
from PyQt5 import QtWidgets
import sys

# pyuic5 C:\Users\Senya\Prog_2\Diplom\main_win.ui -o C:\Users\Senya\Prog_2\Diplom\modules\main_win_code.py

# Увеличить минимальные значения слайдеру рпм

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_backend()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main_':
    import os
    from modules.classes import Prop_stats
    prop = Prop_stats(3, 4)
    print(prop.path_to_pics)
    print('\n\n', prop.pics_names)