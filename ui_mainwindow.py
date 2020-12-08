# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camxVcocv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(14, 16, 375, 371))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_device_number = QLineEdit(self.layoutWidget)
        self.line_device_number.setObjectName(u"line_device_number")
        self.line_device_number.setEnabled(True)
        self.line_device_number.setMaximumSize(QSize(80, 16777215))
        self.line_device_number.setReadOnly(True)

        self.gridLayout_2.addWidget(self.line_device_number, 0, 2, 1, 1)

        self.combo_device_list = QComboBox(self.layoutWidget)
        self.combo_device_list.setObjectName(u"combo_device_list")
        self.combo_device_list.setMinimumSize(QSize(150, 0))

        self.gridLayout_2.addWidget(self.combo_device_list, 0, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.btn_enum_devices = QPushButton(self.layoutWidget)
        self.btn_enum_devices.setObjectName(u"btn_enum_devices")

        self.gridLayout_3.addWidget(self.btn_enum_devices, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_open_device = QPushButton(self.layoutWidget)
        self.btn_open_device.setObjectName(u"btn_open_device")

        self.horizontalLayout_5.addWidget(self.btn_open_device)

        self.btn_close_device = QPushButton(self.layoutWidget)
        self.btn_close_device.setObjectName(u"btn_close_device")

        self.horizontalLayout_5.addWidget(self.btn_close_device)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radio_continuous = QRadioButton(self.layoutWidget)
        self.radio_continuous.setObjectName(u"radio_continuous")
        self.radio_continuous.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radio_continuous)

        self.radio_trigger = QRadioButton(self.layoutWidget)
        self.radio_trigger.setObjectName(u"radio_trigger")

        self.horizontalLayout_4.addWidget(self.radio_trigger)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_start_grabbing = QPushButton(self.layoutWidget)
        self.btn_start_grabbing.setObjectName(u"btn_start_grabbing")

        self.horizontalLayout_3.addWidget(self.btn_start_grabbing)

        self.btn_stop_grabbing = QPushButton(self.layoutWidget)
        self.btn_stop_grabbing.setObjectName(u"btn_stop_grabbing")

        self.horizontalLayout_3.addWidget(self.btn_stop_grabbing)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkbtn_trigger_software = QCheckBox(self.layoutWidget)
        self.checkbtn_trigger_software.setObjectName(u"checkbtn_trigger_software")

        self.horizontalLayout_2.addWidget(self.checkbtn_trigger_software)

        self.btn_trigger_once = QPushButton(self.layoutWidget)
        self.btn_trigger_once.setObjectName(u"btn_trigger_once")

        self.horizontalLayout_2.addWidget(self.btn_trigger_once)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.btn_save_bmp = QPushButton(self.layoutWidget)
        self.btn_save_bmp.setObjectName(u"btn_save_bmp")

        self.gridLayout_3.addWidget(self.btn_save_bmp, 6, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.line_exposure_time = QLineEdit(self.layoutWidget)
        self.line_exposure_time.setObjectName(u"line_exposure_time")

        self.gridLayout.addWidget(self.line_exposure_time, 0, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.line_gain = QLineEdit(self.layoutWidget)
        self.line_gain.setObjectName(u"line_gain")

        self.gridLayout.addWidget(self.line_gain, 1, 2, 1, 1)

        self.line_frame_rate = QLineEdit(self.layoutWidget)
        self.line_frame_rate.setObjectName(u"line_frame_rate")

        self.gridLayout.addWidget(self.line_frame_rate, 2, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_get_parameter = QPushButton(self.layoutWidget)
        self.btn_get_parameter.setObjectName(u"btn_get_parameter")

        self.horizontalLayout.addWidget(self.btn_get_parameter)

        self.btn_set_parameter = QPushButton(self.layoutWidget)
        self.btn_set_parameter.setObjectName(u"btn_set_parameter")

        self.horizontalLayout.addWidget(self.btn_set_parameter)


        self.gridLayout_3.addLayout(self.horizontalLayout, 8, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_3)

        self.label_photo = QLabel(self.layoutWidget)
        self.label_photo.setObjectName(u"label_photo")

        self.horizontalLayout_6.addWidget(self.label_photo)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.line_exposure_time)
        self.label_2.setBuddy(self.line_gain)
        self.label_3.setBuddy(self.line_frame_rate)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.btn_enum_devices, self.btn_open_device)
        QWidget.setTabOrder(self.btn_open_device, self.btn_close_device)
        QWidget.setTabOrder(self.btn_close_device, self.btn_start_grabbing)
        QWidget.setTabOrder(self.btn_start_grabbing, self.btn_stop_grabbing)
        QWidget.setTabOrder(self.btn_stop_grabbing, self.btn_trigger_once)
        QWidget.setTabOrder(self.btn_trigger_once, self.btn_save_bmp)
        QWidget.setTabOrder(self.btn_save_bmp, self.btn_get_parameter)
        QWidget.setTabOrder(self.btn_get_parameter, self.btn_set_parameter)
        QWidget.setTabOrder(self.btn_set_parameter, self.checkbtn_trigger_software)
        QWidget.setTabOrder(self.checkbtn_trigger_software, self.line_exposure_time)
        QWidget.setTabOrder(self.line_exposure_time, self.line_gain)
        QWidget.setTabOrder(self.line_gain, self.line_frame_rate)
        QWidget.setTabOrder(self.line_frame_rate, self.radio_continuous)
        QWidget.setTabOrder(self.radio_continuous, self.radio_trigger)
        QWidget.setTabOrder(self.radio_trigger, self.line_device_number)
        QWidget.setTabOrder(self.line_device_number, self.combo_device_list)

        self.retranslateUi(Form)
        self.btn_enum_devices.clicked.connect(Form.enum_devices_clicked)
        self.combo_device_list.currentIndexChanged.connect(Form.device_list_changed)
        self.btn_open_device.clicked.connect(Form.open_device_clicked)
        self.btn_close_device.clicked.connect(Form.close_device_clicked)
        self.btn_start_grabbing.clicked.connect(Form.start_grabbing_clicked)
        self.btn_stop_grabbing.clicked.connect(Form.stop_grabbing_clicked)
        self.btn_trigger_once.clicked.connect(Form.trigger_once_clicked)
        self.btn_save_bmp.clicked.connect(Form.save_bmp_clicked)
        self.btn_get_parameter.clicked.connect(Form.get_paramater_clicked)
        self.btn_set_parameter.clicked.connect(Form.set_paramater_clicked)
        self.checkbtn_trigger_software.clicked.connect(Form.trigger_software_clicked)
        self.radio_continuous.clicked.connect(Form.radio_continuous_clicked)
        self.radio_trigger.clicked.connect(Form.radio_trigger_clicked)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u76f8\u673a\u603b\u6570:", None))
        self.btn_enum_devices.setText(QCoreApplication.translate("Form", u"\u679a\u4e3e\u8bbe\u5907", None))
        self.btn_open_device.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u8bbe\u5907", None))
        self.btn_close_device.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u8bbe\u5907", None))
        self.radio_continuous.setText(QCoreApplication.translate("Form", u"\u8fde\u7eed\u91c7\u96c6", None))
        self.radio_trigger.setText(QCoreApplication.translate("Form", u"\u89e6\u53d1\u6a21\u5f0f", None))
        self.btn_start_grabbing.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u91c7\u96c6", None))
        self.btn_stop_grabbing.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u91c7\u96c6", None))
        self.checkbtn_trigger_software.setText(QCoreApplication.translate("Form", u"\u8f6f\u89e6\u53d1", None))
        self.btn_trigger_once.setText(QCoreApplication.translate("Form", u"\u91c7\u96c6\u4e00\u6b21", None))
        self.btn_save_bmp.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u56fe\u50cf", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u66dd\u5149\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u589e\u76ca", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5e27\u7387", None))
        self.btn_get_parameter.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u53c2\u6570", None))
        self.btn_set_parameter.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u53c2\u6570", None))
        self.label_photo.setText(QCoreApplication.translate("Form", u"\u56fe\u50cf", None))
    # retranslateUi

