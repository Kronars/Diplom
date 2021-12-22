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
        MainWindow.resize(1165, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(490, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setScaledContents(False)
        self.title.setObjectName("title")
        self.plot_pic = QtWidgets.QLabel(self.centralwidget)
        self.plot_pic.setGeometry(QtCore.QRect(340, 370, 800, 400))
        self.plot_pic.setText("")
        self.plot_pic.setPixmap(QtGui.QPixmap("C:\\Users\\Senya\\Prog_2\\Diplom\\../../../Лена/.designer/plot.png"))
        self.plot_pic.setObjectName("plot_pic")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 311, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.sliders_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.sliders_grid.setContentsMargins(0, 0, 0, 0)
        self.sliders_grid.setObjectName("sliders_grid")
        self.rpm_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.rpm_slider.setMinimum(700)
        self.rpm_slider.setMaximum(30000)
        self.rpm_slider.setSingleStep(1)
        self.rpm_slider.setProperty("value", 700)
        self.rpm_slider.setSliderPosition(700)
        self.rpm_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rpm_slider.setObjectName("rpm_slider")
        self.sliders_grid.addWidget(self.rpm_slider, 13, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sliders_grid.addItem(spacerItem, 8, 0, 1, 1)
        self.p_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.p_slider.setMinimum(1)
        self.p_slider.setMaximum(1230)
        self.p_slider.setOrientation(QtCore.Qt.Horizontal)
        self.p_slider.setObjectName("p_slider")
        self.sliders_grid.addWidget(self.p_slider, 5, 0, 1, 1)
        self.tk_pk_lay = QtWidgets.QHBoxLayout()
        self.tk_pk_lay.setObjectName("tk_pk_lay")
        self.pk_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pk_text.setFont(font)
        self.pk_text.setObjectName("pk_text")
        self.tk_pk_lay.addWidget(self.pk_text)
        self.pk_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pk_input.setText("")
        self.pk_input.setReadOnly(True)
        self.pk_input.setObjectName("pk_input")
        self.tk_pk_lay.addWidget(self.pk_input)
        self.tk_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tk_text.setFont(font)
        self.tk_text.setObjectName("tk_text")
        self.tk_pk_lay.addWidget(self.tk_text)
        self.tk_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tk_input.setText("")
        self.tk_input.setReadOnly(True)
        self.tk_input.setObjectName("tk_input")
        self.tk_pk_lay.addWidget(self.tk_input)
        self.sliders_grid.addLayout(self.tk_pk_lay, 9, 0, 1, 1)
        self.p_num = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.p_num.setMinimum(2.0)
        self.p_num.setMaximum(20.0)
        self.p_num.setSingleStep(0.5)
        self.p_num.setObjectName("p_num")
        self.sliders_grid.addWidget(self.p_num, 5, 1, 1, 1)
        self.rpm_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rpm_text.setFont(font)
        self.rpm_text.setObjectName("rpm_text")
        self.sliders_grid.addWidget(self.rpm_text, 12, 0, 1, 1)
        self.d_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.d_text.setFont(font)
        self.d_text.setObjectName("d_text")
        self.sliders_grid.addWidget(self.d_text, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sliders_grid.addItem(spacerItem1, 11, 0, 1, 1)
        self.p_text = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p_text.setFont(font)
        self.p_text.setObjectName("p_text")
        self.sliders_grid.addWidget(self.p_text, 4, 0, 1, 1)
        self.d_num = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.d_num.setSuffix("")
        self.d_num.setMinimum(2.0)
        self.d_num.setMaximum(20.0)
        self.d_num.setSingleStep(0.5)
        self.d_num.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.d_num.setObjectName("d_num")
        self.sliders_grid.addWidget(self.d_num, 1, 1, 1, 1)
        self.d_slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.d_slider.setMinimum(1)
        self.d_slider.setMaximum(180)
        self.d_slider.setSingleStep(1)
        self.d_slider.setOrientation(QtCore.Qt.Horizontal)
        self.d_slider.setObjectName("d_slider")
        self.sliders_grid.addWidget(self.d_slider, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sliders_grid.addItem(spacerItem2, 10, 0, 1, 1)
        self.rpm_num = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.rpm_num.setMinimum(700)
        self.rpm_num.setMaximum(30000)
        self.rpm_num.setSingleStep(100)
        self.rpm_num.setObjectName("rpm_num")
        self.sliders_grid.addWidget(self.rpm_num, 13, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 540, 311, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.thr_pwr_inp = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.thr_pwr_inp.setContentsMargins(0, 0, 0, 0)
        self.thr_pwr_inp.setObjectName("thr_pwr_inp")
        self.thr_inp_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thr_inp_text.setFont(font)
        self.thr_inp_text.setObjectName("thr_inp_text")
        self.thr_pwr_inp.addWidget(self.thr_inp_text)
        self.pwr_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.pwr_slider.setMinimum(1)
        self.pwr_slider.setMaximum(100)
        self.pwr_slider.setOrientation(QtCore.Qt.Horizontal)
        self.pwr_slider.setObjectName("pwr_slider")
        self.thr_pwr_inp.addWidget(self.pwr_slider)
        self.pow_inp_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pow_inp_text.setFont(font)
        self.pow_inp_text.setObjectName("pow_inp_text")
        self.thr_pwr_inp.addWidget(self.pow_inp_text)
        self.thr_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.thr_slider.setMinimum(1)
        self.thr_slider.setMaximum(100)
        self.thr_slider.setOrientation(QtCore.Qt.Horizontal)
        self.thr_slider.setObjectName("thr_slider")
        self.thr_pwr_inp.addWidget(self.thr_slider)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 390, 311, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.outStats_lay = QtWidgets.QFormLayout(self.layoutWidget)
        self.outStats_lay.setContentsMargins(0, 0, 0, 0)
        self.outStats_lay.setObjectName("outStats_lay")
        self.thr_text = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.thr_text.setFont(font)
        self.thr_text.setObjectName("thr_text")
        self.outStats_lay.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.thr_text)
        self.thr_vals = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.thr_vals.setFont(font)
        self.thr_vals.setObjectName("thr_vals")
        self.outStats_lay.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thr_vals)
        self.pwr_text = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pwr_text.setFont(font)
        self.pwr_text.setObjectName("pwr_text")
        self.outStats_lay.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pwr_text)
        self.pwr_vals = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.pwr_vals.setFont(font)
        self.pwr_vals.setObjectName("pwr_vals")
        self.outStats_lay.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pwr_vals)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(350, 60, 801, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.props_lay = QtWidgets.QVBoxLayout()
        self.props_lay.setObjectName("props_lay")
        self.front_prop = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.front_prop.setText("")
        self.front_prop.setPixmap(QtGui.QPixmap("C:\\Users\\Senya\\Prog_2\\Diplom\\../../../Лена/.designer/backup/resize.png"))
        self.front_prop.setObjectName("front_prop")
        self.props_lay.addWidget(self.front_prop)
        self.side_prop = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.side_prop.setText("")
        self.side_prop.setPixmap(QtGui.QPixmap("C:\\Users\\Senya\\Prog_2\\Diplom\\../../../Лена/.designer/backup/resize.png"))
        self.side_prop.setScaledContents(False)
        self.side_prop.setObjectName("side_prop")
        self.props_lay.addWidget(self.side_prop)
        self.gridLayout.addLayout(self.props_lay, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(350, 290, 801, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.comboBoxLay = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.comboBoxLay.setContentsMargins(0, 0, 0, 0)
        self.comboBoxLay.setObjectName("comboBoxLay")
        self.dp_assort_box = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.dp_assort_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dp_assort_box.setFont(font)
        self.dp_assort_box.setChecked(False)
        self.dp_assort_box.setObjectName("dp_assort_box")
        self.comboBoxLay.addWidget(self.dp_assort_box, 0, 0, 1, 1)
        self.selected_dp_props = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.selected_dp_props.setObjectName("selected_dp_props")
        self.comboBoxLay.addWidget(self.selected_dp_props, 1, 0, 1, 1)
        self.d_assort_box = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.d_assort_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d_assort_box.setFont(font)
        self.d_assort_box.setChecked(False)
        self.d_assort_box.setObjectName("d_assort_box")
        self.comboBoxLay.addWidget(self.d_assort_box, 0, 1, 1, 1)
        self.p_assort_box = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.p_assort_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_assort_box.setFont(font)
        self.p_assort_box.setChecked(False)
        self.p_assort_box.setObjectName("p_assort_box")
        self.comboBoxLay.addWidget(self.p_assort_box, 0, 2, 1, 1)
        self.selected_d_props = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.selected_d_props.setObjectName("selected_d_props")
        self.comboBoxLay.addWidget(self.selected_d_props, 1, 1, 1, 1)
        self.selected_p_props = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.selected_p_props.setObjectName("selected_p_props")
        self.comboBoxLay.addWidget(self.selected_p_props, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.rpm_num.valueChanged['int'].connect(self.rpm_slider.setValue)
        self.rpm_slider.valueChanged['int'].connect(self.rpm_num.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prop Selector"))
        self.title.setText(_translate("MainWindow", "Подбор пропеллера"))
        self.pk_text.setText(_translate("MainWindow", "pk"))
        self.tk_text.setText(_translate("MainWindow", "tk"))
        self.rpm_text.setText(_translate("MainWindow", "Обороты в минуту"))
        self.d_text.setText(_translate("MainWindow", "Диаметр"))
        self.p_text.setText(_translate("MainWindow", "Шаг"))
        self.thr_inp_text.setText(_translate("MainWindow", "Желаемая тяга (в %)"))
        self.pow_inp_text.setText(_translate("MainWindow", "Желаемая мощность (в %)"))
        self.thr_text.setText(_translate("MainWindow", "Создаваемая тяга:\n"
"\n"
""))
        self.thr_vals.setText(_translate("MainWindow", "0.5 Н\n"
"0.201 кгС\n"
"200 гС"))
        self.pwr_text.setText(_translate("MainWindow", "Требуемая мощность:\n"
"\n"
""))
        self.pwr_vals.setText(_translate("MainWindow", "0.5 Н\n"
"0.201 кгС\n"
"200 гС"))
        self.dp_assort_box.setText(_translate("MainWindow", "Подобрать наиболее похожий"))
        self.d_assort_box.setText(_translate("MainWindow", "Подобрать по диаметру"))
        self.p_assort_box.setText(_translate("MainWindow", "Подобрать по шагу"))
