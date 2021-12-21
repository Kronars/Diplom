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

from modules.classes import Props_data, Prop, Quad
import os

prop = Prop(3, 4)
print(prop.name)
valid = prop.get_real_props()[1]
prop.elect_this(valid)
print(prop.name)

# супер суета с ф-ями get tk get pk
# вероятно берут хуёвый рпм
