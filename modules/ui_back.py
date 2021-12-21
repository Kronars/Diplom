from main_win_code import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
from classes import Quad, Prop, Spares_stats

# pyuic5 C:\Users\Senya\Prog_2\Kyrsach\Proga\main_win.ui -o C:\Users\Senya\Prog_2\Kyrsach\Proga\main_win_code.py

class Ui_backend(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.D_MAX = 20
        self.P_MAX = 14
        self.D_MIN = 2
        self.P_MIN = 0.7

        self.data = Spares_stats(prop=True)
        self.prop = Prop(self.data, 5, 5)
        self.prop.get_real_props()
        self.stats = Quad(self.prop)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.mw = MainWindow

        self.slider_d_vals = np.linspace(self.D_MIN, self.D_MAX, self.d_slider.maximum() + 1)
        self.slider_p_vals = np.linspace(self.P_MIN, self.P_MAX, self.p_slider.maximum() + 1)

        self.d_slider.sliderMoved.connect(self.sliders_control)
        self.p_slider.sliderMoved.connect(self.sliders_control)
        self.rpm_slider.sliderMoved.connect(self.sliders_control)

        self.d_num.editingFinished.connect(self.sliders_control)
        self.p_num.editingFinished.connect(self.sliders_control)
        self.rpm_num.editingFinished.connect(self.sliders_control)

        self.own_box.clicked.connect(self.selection_control)
        self.selected_props.textActivated.connect(self.elect_prop)

    def elect_prop(self):
        selected = self.selected_props.currentText()
        for id, item in enumerate(self.data.data):
            try:
                self.data.data[id].index(selected+'.txt')
                self.set_prop_conf(item)
            except ValueError:
                continue
        
    def set_prop_conf(self, conf):
        self.prop.re_elect(conf)
        d, p, _, _ = conf
        self.correct_all(d, p)

    def correct_all(self, d, p):
        d, p = float(d), float(p)
        d_val = int((d - self.D_MIN) * 10) - 1
        p_val = int((p - self.P_MIN) * 100) - 1

        self.d_num.setValue(d)
        self.p_num.setValue(p)

        self.d_slider.setValue(d_val)
        self.p_slider.setValue(p_val)
        
    def selection_control(self):
        # who = self.mw.sender().objectName()
        if self.own_box.checkState():
            self.fill_combo_box()
        else:
            self.selected_props.clear()

    def fill_combo_box(self):
        self.calc_stats(from_ui=False)
        self.prop.get_real_props()
        for prop in self.prop.selection:
            self.selected_props.addItem(prop[3][:-4])
        self.sliders_control()
        
    def sliders_control(self):
        who = self.mw.sender().objectName()
        sliders_white_list = ['d_slider', 'p_slider', 'rpm_slider']
        spinBox_white_list = ['d_num', 'p_num', 'rpm_num']
        if who in sliders_white_list:
            self.selected_props.clear()
            self.own_box.setCheckState(False)
            self.do_sliders()
        elif who in spinBox_white_list:
            self.correct_sliders()
        self.prop.get_real_props()
        self.calc_stats()

    def correct_sliders(self):
        # print('correct sliders')
        d_val = int((self.d_num.value() - self.D_MIN) * 10)
        p_val = int((self.p_num.value() - self.P_MIN) * 100)

        self.d_slider.setValue(d_val)
        self.p_slider.setValue(p_val)

    def do_sliders(self):
        # print('do sliders')
        d_val = round(self.slider_d_vals[self.d_slider.sliderPosition()] + 1, 2)
        p_val = round(self.slider_p_vals[self.p_slider.sliderPosition()] + 1, 2)

        self.d_num.setValue(d_val)
        self.p_num.setValue(p_val)

    def calc_stats(self, from_ui=True):
        """Берёт значения из текущего положения спин боксов или объекта и высчитывает статы в лейбл
        from_ui == True: Значения интерфейса -> Статы
        from_ui == False: Значения объекта -> Статы"""
        # print('calc_stats')
        if from_ui:
            self.prop = Prop(self.data, self.d_num.value(), self.p_num.value(), self.rpm_num.value())
        else:
            self.prop = Prop(self.data, self.prop.d, self.prop.p, self.rpm_num.value())
        self.stats = Quad(self.prop)
        thrust = int(self.stats.calc_thrust(self.rpm_num.value()))
        power = int(self.stats.calc_power(self.rpm_num.value()))
        self.thr_vals.setText(f'{round(thrust, 5)} Н\n{round(thrust / 9.806, 5)} кгС\n{round(thrust / 9.806 * 1000, 5)} гС')
        self.pwr_vals.setText(f'{round(power, 5)} Ватт\n\n')
        self.display_plot()

    def display_plot(self):
        # if self.ready_to_plot:
        self.stats.draw_prop_stats(r'C:\Users\Senya\Prog_2\Kyrsach\Proga', self.rpm_num.value())
        pixmap = QtGui.QPixmap(r'C:\Users\Senya\Prog_2\Kyrsach\Proga\plot.png')
        self.plot_pic.setPixmap(pixmap)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_backend()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())