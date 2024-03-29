# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Senya\Prog_2\Diplom\main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 818)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.general_lay = QtWidgets.QWidget(MainWindow)
        self.general_lay.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.general_lay.setFont(font)
        self.general_lay.setObjectName("general_lay")
        self.gridLayoutWidget = QtWidgets.QWidget(self.general_lay)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 321, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.sliders_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.sliders_grid.setContentsMargins(0, 0, 0, 0)
        self.sliders_grid.setObjectName("sliders_grid")
        self.p_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.p_slider.setMinimum(1)
        self.p_slider.setMaximum(1230)
        self.p_slider.setOrientation(QtCore.Qt.Horizontal)
        self.p_slider.setObjectName("p_slider")
        self.sliders_grid.addWidget(self.p_slider, 5, 0, 1, 1)
        self.d_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d_text.setFont(font)
        self.d_text.setObjectName("d_text")
        self.sliders_grid.addWidget(self.d_text, 0, 0, 1, 1)
        self.p_num = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.p_num.setMinimum(2.0)
        self.p_num.setMaximum(20.0)
        self.p_num.setSingleStep(0.5)
        self.p_num.setObjectName("p_num")
        self.sliders_grid.addWidget(self.p_num, 5, 1, 1, 1)
        self.p_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p_text.setFont(font)
        self.p_text.setObjectName("p_text")
        self.sliders_grid.addWidget(self.p_text, 4, 0, 1, 1)
        self.rpm_num = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.rpm_num.setMinimum(0)
        self.rpm_num.setMaximum(30000)
        self.rpm_num.setSingleStep(50)
        self.rpm_num.setObjectName("rpm_num")
        self.sliders_grid.addWidget(self.rpm_num, 16, 1, 1, 1)
        self.d_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.d_slider.setMinimum(1)
        self.d_slider.setMaximum(180)
        self.d_slider.setSingleStep(1)
        self.d_slider.setOrientation(QtCore.Qt.Horizontal)
        self.d_slider.setObjectName("d_slider")
        self.sliders_grid.addWidget(self.d_slider, 1, 0, 1, 1)
        self.rpm_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.rpm_slider.setMinimum(0)
        self.rpm_slider.setMaximum(30000)
        self.rpm_slider.setSingleStep(1)
        self.rpm_slider.setProperty("value", 500)
        self.rpm_slider.setSliderPosition(500)
        self.rpm_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rpm_slider.setObjectName("rpm_slider")
        self.sliders_grid.addWidget(self.rpm_slider, 16, 0, 1, 1)
        self.d_num = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.d_num.setSuffix("")
        self.d_num.setMinimum(2.0)
        self.d_num.setMaximum(20.0)
        self.d_num.setSingleStep(0.5)
        self.d_num.setObjectName("d_num")
        self.sliders_grid.addWidget(self.d_num, 1, 1, 1, 1)
        self.rpm_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rpm_text.setFont(font)
        self.rpm_text.setObjectName("rpm_text")
        self.sliders_grid.addWidget(self.rpm_text, 13, 0, 1, 1)
        self.tk_pk_lay = QtWidgets.QHBoxLayout()
        self.tk_pk_lay.setObjectName("tk_pk_lay")
        self.pk_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pk_text.setFont(font)
        self.pk_text.setObjectName("pk_text")
        self.tk_pk_lay.addWidget(self.pk_text)
        self.pk_input = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.pk_input.setDecimals(3)
        self.pk_input.setMaximum(10.0)
        self.pk_input.setSingleStep(0.001)
        self.pk_input.setObjectName("pk_input")
        self.tk_pk_lay.addWidget(self.pk_input)
        self.tk_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tk_text.setFont(font)
        self.tk_text.setObjectName("tk_text")
        self.tk_pk_lay.addWidget(self.tk_text)
        self.tk_input = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.tk_input.setDecimals(3)
        self.tk_input.setMaximum(10.0)
        self.tk_input.setSingleStep(0.001)
        self.tk_input.setObjectName("tk_input")
        self.tk_pk_lay.addWidget(self.tk_input)
        self.sliders_grid.addLayout(self.tk_pk_lay, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sliders_grid.addItem(spacerItem, 12, 0, 1, 1)
        self.air_box = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.air_box.setDecimals(4)
        self.air_box.setMaximum(10.0)
        self.air_box.setSingleStep(0.001)
        self.air_box.setProperty("value", 1.2754)
        self.air_box.setObjectName("air_box")
        self.sliders_grid.addWidget(self.air_box, 11, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sliders_grid.addItem(spacerItem1, 6, 0, 1, 1)
        self.air_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.air_label.setObjectName("air_label")
        self.sliders_grid.addWidget(self.air_label, 11, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.general_lay)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 470, 311, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.stats_lay = QtWidgets.QGridLayout(self.layoutWidget)
        self.stats_lay.setContentsMargins(0, 0, 0, 0)
        self.stats_lay.setObjectName("stats_lay")
        self.curr_prop_text = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.curr_prop_text.setFont(font)
        self.curr_prop_text.setObjectName("curr_prop_text")
        self.stats_lay.addWidget(self.curr_prop_text, 0, 0, 1, 1)
        self.pwr_text = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pwr_text.setFont(font)
        self.pwr_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pwr_text.setObjectName("pwr_text")
        self.stats_lay.addWidget(self.pwr_text, 2, 0, 1, 1)
        self.curr_prop_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.curr_prop_name.setFont(font)
        self.curr_prop_name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.curr_prop_name.setObjectName("curr_prop_name")
        self.stats_lay.addWidget(self.curr_prop_name, 0, 1, 1, 1)
        self.thr_vals = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.thr_vals.setFont(font)
        self.thr_vals.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.thr_vals.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.thr_vals.setObjectName("thr_vals")
        self.stats_lay.addWidget(self.thr_vals, 1, 1, 1, 1)
        self.pwr_vals = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.pwr_vals.setFont(font)
        self.pwr_vals.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pwr_vals.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.pwr_vals.setObjectName("pwr_vals")
        self.stats_lay.addWidget(self.pwr_vals, 2, 1, 1, 1)
        self.thr_text = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.thr_text.setFont(font)
        self.thr_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.thr_text.setObjectName("thr_text")
        self.stats_lay.addWidget(self.thr_text, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.general_lay)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(21, 310, 1241, 63))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.comboBoxLay = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.comboBoxLay.setContentsMargins(0, 0, 0, 0)
        self.comboBoxLay.setObjectName("comboBoxLay")
        self.dp_assort_box = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.dp_assort_box.setObjectName("dp_assort_box")
        self.comboBoxLay.addWidget(self.dp_assort_box, 0, 1, 1, 1)
        self.selected_dp_props = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.selected_dp_props.setObjectName("selected_dp_props")
        self.comboBoxLay.addWidget(self.selected_dp_props, 1, 1, 1, 1)
        self.p_assort_box = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.p_assort_box.setObjectName("p_assort_box")
        self.comboBoxLay.addWidget(self.p_assort_box, 0, 3, 1, 1)
        self.d_assort_box = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.d_assort_box.setObjectName("d_assort_box")
        self.comboBoxLay.addWidget(self.d_assort_box, 0, 2, 1, 1)
        self.selected_p_props = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.selected_p_props.setObjectName("selected_p_props")
        self.comboBoxLay.addWidget(self.selected_p_props, 1, 3, 1, 1)
        self.selected_d_props = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.selected_d_props.setObjectName("selected_d_props")
        self.comboBoxLay.addWidget(self.selected_d_props, 1, 2, 1, 1)
        self.all_sort_box = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_sort_box.sizePolicy().hasHeightForWidth())
        self.all_sort_box.setSizePolicy(sizePolicy)
        self.all_sort_box.setBaseSize(QtCore.QSize(0, 0))
        self.all_sort_box.setAcceptDrops(False)
        self.all_sort_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.all_sort_box.setObjectName("all_sort_box")
        self.comboBoxLay.addWidget(self.all_sort_box, 1, 0, 1, 1)
        self.all_sort_title = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.all_sort_title.setObjectName("all_sort_title")
        self.comboBoxLay.addWidget(self.all_sort_title, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.general_lay)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 20, 921, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.props_lay = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.props_lay.setContentsMargins(0, 0, 0, 0)
        self.props_lay.setObjectName("props_lay")
        self.front_prop = QtWidgets.QLabel(self.layoutWidget1)
        self.front_prop.setText("")
        self.front_prop.setPixmap(QtGui.QPixmap("C:\\Users\\Senya\\Prog_2\\Diplom\\../../../Лена/.designer/backup/resize.png"))
        self.front_prop.setObjectName("front_prop")
        self.props_lay.addWidget(self.front_prop)
        self.side_prop = QtWidgets.QLabel(self.layoutWidget1)
        self.side_prop.setText("")
        self.side_prop.setPixmap(QtGui.QPixmap("C:\\Users\\Senya\\Prog_2\\Diplom\\../../../Лена/.designer/backup/resize.png"))
        self.side_prop.setScaledContents(False)
        self.side_prop.setObjectName("side_prop")
        self.props_lay.addWidget(self.side_prop)
        self.graphWidget = GraphicsLayoutWidget(self.general_lay)
        self.graphWidget.setGeometry(QtCore.QRect(340, 430, 921, 381))
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.general_lay)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 380, 311, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pow_formula = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pow_formula.sizePolicy().hasHeightForWidth())
        self.pow_formula.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pow_formula.setFont(font)
        self.pow_formula.setFrameShape(QtWidgets.QFrame.Box)
        self.pow_formula.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pow_formula.setTextFormat(QtCore.Qt.PlainText)
        self.pow_formula.setScaledContents(False)
        self.pow_formula.setAlignment(QtCore.Qt.AlignCenter)
        self.pow_formula.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.pow_formula.setObjectName("pow_formula")
        self.verticalLayout.addWidget(self.pow_formula)
        self.thr_formula = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thr_formula.sizePolicy().hasHeightForWidth())
        self.thr_formula.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thr_formula.setFont(font)
        self.thr_formula.setFrameShape(QtWidgets.QFrame.Box)
        self.thr_formula.setFrameShadow(QtWidgets.QFrame.Plain)
        self.thr_formula.setTextFormat(QtCore.Qt.PlainText)
        self.thr_formula.setScaledContents(False)
        self.thr_formula.setAlignment(QtCore.Qt.AlignCenter)
        self.thr_formula.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.thr_formula.setObjectName("thr_formula")
        self.verticalLayout.addWidget(self.thr_formula)
        self.full_calc = QtWidgets.QLabel(self.general_lay)
        self.full_calc.setGeometry(QtCore.QRect(340, 380, 921, 51))
        self.full_calc.setTextFormat(QtCore.Qt.AutoText)
        self.full_calc.setScaledContents(False)
        self.full_calc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.full_calc.setWordWrap(True)
        self.full_calc.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.full_calc.setObjectName("full_calc")
        self.speed_label = QtWidgets.QLabel(self.general_lay)
        self.speed_label.setGeometry(QtCore.QRect(20, 710, 311, 60))
        self.speed_label.setMinimumSize(QtCore.QSize(311, 30))
        self.speed_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.speed_label.setWordWrap(True)
        self.speed_label.setObjectName("speed_label")
        self.boost_formula = QtWidgets.QLabel(self.general_lay)
        self.boost_formula.setGeometry(QtCore.QRect(20, 580, 309, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boost_formula.sizePolicy().hasHeightForWidth())
        self.boost_formula.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.boost_formula.setFont(font)
        self.boost_formula.setFrameShape(QtWidgets.QFrame.Box)
        self.boost_formula.setFrameShadow(QtWidgets.QFrame.Plain)
        self.boost_formula.setTextFormat(QtCore.Qt.PlainText)
        self.boost_formula.setScaledContents(False)
        self.boost_formula.setAlignment(QtCore.Qt.AlignCenter)
        self.boost_formula.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.boost_formula.setObjectName("boost_formula")
        self.formLayoutWidget = QtWidgets.QWidget(self.general_lay)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 630, 311, 70))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.mass_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.mass_label.setObjectName("mass_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mass_label)
        self.mass_spin_box = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.mass_spin_box.setObjectName("mass_spin_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mass_spin_box)
        self.amount_props_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.amount_props_label.setObjectName("amount_props_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.amount_props_label)
        self.amount_spin_box = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.amount_spin_box.setObjectName("amount_spin_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.amount_spin_box)
        MainWindow.setCentralWidget(self.general_lay)

        self.retranslateUi(MainWindow)
        self.rpm_num.valueChanged['int'].connect(self.rpm_slider.setValue)
        self.rpm_slider.valueChanged['int'].connect(self.rpm_num.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prop Selector"))
        self.d_text.setText(_translate("MainWindow", "Диаметр"))
        self.p_text.setText(_translate("MainWindow", "Шаг"))
        self.rpm_text.setText(_translate("MainWindow", "Обороты в минуту"))
        self.pk_text.setText(_translate("MainWindow", "CP"))
        self.tk_text.setText(_translate("MainWindow", "CT"))
        self.air_label.setText(_translate("MainWindow", "Плотность воздуха"))
        self.curr_prop_text.setText(_translate("MainWindow", "Текущий винт:"))
        self.pwr_text.setText(_translate("MainWindow", "Требуемая мощность:"))
        self.curr_prop_name.setText(_translate("MainWindow", "custom"))
        self.thr_vals.setText(_translate("MainWindow", "0.5 Н"))
        self.pwr_vals.setText(_translate("MainWindow", "0.5 Ватт"))
        self.thr_text.setText(_translate("MainWindow", "Создаваемая тяга:"))
        self.dp_assort_box.setText(_translate("MainWindow", "Подобрать наиболее похожий"))
        self.p_assort_box.setText(_translate("MainWindow", "Подобрать по шагу"))
        self.d_assort_box.setText(_translate("MainWindow", "Подобрать по диаметру"))
        self.all_sort_title.setText(_translate("MainWindow", "Все доступные винты:"))
        self.pow_formula.setText(_translate("MainWindow", "Мощность = CP p n^3 D^5"))
        self.thr_formula.setText(_translate("MainWindow", "Тяга = CT p n^2 D^4"))
        self.full_calc.setText(_translate("MainWindow", "Расчёт тяги: \n"
"Расчёт мощности:"))
        self.speed_label.setText(_translate("MainWindow", "m / P * 3.6 * n = 30 км/ч"))
        self.boost_formula.setText(_translate("MainWindow", "Ускорение: Сила тяги / Масса"))
        self.mass_label.setText(_translate("MainWindow", "Масса (в кг)"))
        self.amount_props_label.setText(_translate("MainWindow", "Количество винтов"))
from pyqtgraph import GraphicsLayoutWidget
