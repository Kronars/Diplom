from modules.main_win_code import Ui_MainWindow
from modules.classes import Prop_stats, Prop, Props_data
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, re
import numpy as np

# потеннциальная проблема:
# 1. некорректно работают боксы, при отжатии кнопки - краш

class Ui_backend(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.D_MAX = 20
        self.P_MAX = 14
        self.D_MIN = 2
        self.P_MIN = 0.7

        self.stats = Prop_stats(5, 5)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.mw = MainWindow

        self.slider_d_vals = np.linspace(self.D_MIN, self.D_MAX, self.d_slider.maximum() + 1)
        self.slider_p_vals = np.linspace(self.P_MIN, self.P_MAX, self.p_slider.maximum() + 1)

        # self.d_slider.valueChanged.connect(self.sliders_control)     # Если сделать так, то при изменении слайдера спин боксом
        # self.p_slider.valueChanged.connect(self.sliders_control)     # будет менятся и другой слайдер
        # self.rpm_slider.valueChanged.connect(self.sliders_control)

        self.d_slider.sliderMoved.connect(self.sliders_control)
        self.p_slider.sliderMoved.connect(self.sliders_control)
        self.rpm_slider.sliderMoved.connect(self.sliders_control)

        self.d_num.editingFinished.connect(self.sliders_control)
        self.p_num.editingFinished.connect(self.sliders_control)
        self.rpm_num.editingFinished.connect(self.sliders_control)

        self.d_assort_box.clicked.connect(self.selection_control)
        self.p_assort_box.clicked.connect(self.selection_control)
        self.dp_assort_box.clicked.connect(self.selection_control)

        self.selected_d_props.textActivated.connect(self.activate_prop)
        self.selected_p_props.textActivated.connect(self.activate_prop)
        self.selected_dp_props.textActivated.connect(self.activate_prop)
    
    def get_ui_params(self):
        '''Возвращает параметры пропа из интерфейса'''
        return [self.d_num.value(), self.p_num.value(), 'custom.txt', 'custom.txt']

    def set_params_to_obj(self, params):
        '''Устанавливает в объект пропа переданные параметры'''
        self.stats.elect_this(params)

    def set_params_to_ui(self):
        '''Устанавливает на слайдеры параметры из объекта пропа'''
        d, p = self.stats.d, self.stats.p
        d_val = int((d - self.D_MIN) * 10) - 1
        p_val = int((p - self.P_MIN) * 100) - 1

        self.d_num.setValue(d)
        self.p_num.setValue(p)

        self.d_slider.setValue(d_val)
        self.p_slider.setValue(p_val)

    def activate_prop(self):
        send_from = self.mw.sender().objectName()
        if send_from == 'selected_dp_props':
            obj = self.selected_dp_props
        elif send_from == 'selected_d_props':
            obj = self.selected_d_props
        elif send_from == 'selected_p_props':
            obj = self.selected_p_props
        selected = obj.currentText() + '.txt'
        match = re.search(r'(\w*)_(\d+.?\d*)x(\d+.?\d*)_', selected)
        name, d, p = match[1], float(match[2]), float(match[3])
        prop = [d, p, name, selected]
        self.set_params_to_obj(prop)
        self.set_params_to_ui()
        
    def selection_control(self):
        def fill_combo_box(self, props, box):
            box.clear()
            for prop in props:
                box.addItem(prop[3][:-4])
            self.set_params_to_obj(props[0])
            self.sliders_control()

        if self.dp_assort_box.isChecked():
            sorted_props = self.stats.get_real_props()
            box = self.selected_dp_props
        if self.d_assort_box.isChecked():
            d = self.get_ui_params()[0]
            sorted_props = self.stats.sorted_props(d, 'd')
            box = self.selected_d_props
        elif self.p_assort_box.isChecked():
            p = self.get_ui_params()[1]
            sorted_props = self.stats.sorted_props(p, 'p')
            box = self.selected_p_props
        fill_combo_box(self, sorted_props, box)

    def sliders_control(self):
        '''Устанавливает в объект пропа параметры со слайдеров
        Управляет слайдерами диаметра и шага, устанавливает соответсвующие спин боксы
        Точность спин бокса диаметра до десятых, спин бокса шага - до сотых'''
        def set_spin_box_val(self):
            d_val = round(self.slider_d_vals[self.d_slider.sliderPosition()] + 1, 2)
            p_val = round(self.slider_p_vals[self.p_slider.sliderPosition()] + 1, 2)

            self.d_num.setValue(d_val)
            self.p_num.setValue(p_val)

        def set_sliders_val(self):
            d_val = int((self.d_num.value() - self.D_MIN) * 10)
            p_val = int((self.p_num.value() - self.P_MIN) * 100)

            self.d_slider.setValue(d_val)
            self.p_slider.setValue(p_val)

        send_from = self.mw.sender().objectName()
        sliders = ['d_slider', 'p_slider', 'rpm_slider']
        spinBox = ['d_num', 'p_num', 'rpm_num']
        if send_from in sliders:
            set_spin_box_val(self)
        elif send_from in spinBox:
            set_sliders_val(self)
        else:
            return None
        # self.d_assort_box.setCheckState(False)
        # self.p_assort_box.setCheckState(False)
        # self.dp_assort_box.setCheckState(False)
        
        # self.selected_dp_props.clear()
        # self.selected_d_props.clear()
        # self.selected_p_props.clear()

        params = [self.d_num.value(), self.p_num.value(), 'custom.txt', 'custom.txt']
        self.set_params_to_obj(params)
        self.calc_stats()

    def calc_stats(self):
        """Берёт значения из текущего объекта пропа, рассчитывает на их основе лэйбл и график"""
        thrust = int(self.stats.calc_thrust(self.rpm_num.value()))
        power = int(self.stats.calc_power(self.rpm_num.value()))
        self.thr_vals.setText(f'{round(thrust, 5)} Н\n{round(thrust / 9.806, 5)} кгС\n{round(thrust / 9.806 * 1000, 5)} гС')
        self.pwr_vals.setText(f'{round(power, 5)} Ватт\n\n')
        self.display_plot()

    def display_plot(self):
        self.stats.draw_prop_stats(self.rpm_num.value())
        pixmap = QtGui.QPixmap(os.path.join(self.stats.path_to_plots, 'plot.png'))
        self.plot_pic.setPixmap(pixmap)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_backend()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())