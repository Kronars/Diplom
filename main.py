from modules.ui_back import Ui_backend
from PyQt5 import QtWidgets
import sys

if __name__ == '__main_':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_backend()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())

from modules.classes import Prop_stats
import os

prop = Prop_stats(3, 5)
valid = prop.get_real_props()[1]
print(valid)
prop.elect_this(valid)
print(prop.inf())

# супер суета с ф-ями get tk get pk
# вероятно берут хуёвый рпм
