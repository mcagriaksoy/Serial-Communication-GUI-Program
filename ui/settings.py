# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFontComboBox, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(251, 386)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.SaveAll)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 221, 311))
        self.formLayout_config = QFormLayout(self.layoutWidget)
        self.formLayout_config.setObjectName(u"formLayout_config")
        self.formLayout_config.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_config.setFormAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.formLayout_config.setHorizontalSpacing(4)
        self.formLayout_config.setVerticalSpacing(2)
        self.formLayout_config.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.layoutWidget)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_config.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_46)

        self.refresh_button = QPushButton(self.layoutWidget)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(4, QFormLayout.ItemRole.FieldRole, self.refresh_button)

        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_config.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.port_comboBox = QComboBox(self.layoutWidget)
        self.port_comboBox.setObjectName(u"port_comboBox")
        self.port_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(5, QFormLayout.ItemRole.FieldRole, self.port_comboBox)

        self.label_25 = QLabel(self.layoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_config.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.baudrate_comboBox = QComboBox(self.layoutWidget)
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.setObjectName(u"baudrate_comboBox")
        self.baudrate_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(6, QFormLayout.ItemRole.FieldRole, self.baudrate_comboBox)

        self.label_26 = QLabel(self.layoutWidget)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_config.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.len_comboBox = QComboBox(self.layoutWidget)
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.setObjectName(u"len_comboBox")
        self.len_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(7, QFormLayout.ItemRole.FieldRole, self.len_comboBox)

        self.label_27 = QLabel(self.layoutWidget)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_config.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.timeout_comboBox = QComboBox(self.layoutWidget)
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.setObjectName(u"timeout_comboBox")
        self.timeout_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(8, QFormLayout.ItemRole.FieldRole, self.timeout_comboBox)

        self.label_28 = QLabel(self.layoutWidget)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_config.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.parity_comboBox = QComboBox(self.layoutWidget)
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.setObjectName(u"parity_comboBox")
        self.parity_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(9, QFormLayout.ItemRole.FieldRole, self.parity_comboBox)

        self.label_29 = QLabel(self.layoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_config.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_29)

        self.bit_comboBox = QComboBox(self.layoutWidget)
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.setObjectName(u"bit_comboBox")
        self.bit_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(10, QFormLayout.ItemRole.FieldRole, self.bit_comboBox)

        self.label_30 = QLabel(self.layoutWidget)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_config.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.flow_comboBox = QComboBox(self.layoutWidget)
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.setObjectName(u"flow_comboBox")
        self.flow_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(11, QFormLayout.ItemRole.FieldRole, self.flow_comboBox)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_config.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_2)

        self.fontComboBox = QFontComboBox(self.layoutWidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(1, QFormLayout.ItemRole.FieldRole, self.fontComboBox)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_config.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout_config.setItem(3, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_config.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"Refresh Port(s):", None))
        self.refresh_button.setText(QCoreApplication.translate("Dialog", u"\u21bb", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Selected Port:", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Baud Rate:", None))
        self.baudrate_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"9600", None))
        self.baudrate_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"57600", None))
        self.baudrate_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"115200", None))
        self.baudrate_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"110", None))
        self.baudrate_comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"300", None))
        self.baudrate_comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"1200", None))
        self.baudrate_comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"2400", None))
        self.baudrate_comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"4800", None))
        self.baudrate_comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"19200", None))
        self.baudrate_comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"38400", None))

        self.label_26.setText(QCoreApplication.translate("Dialog", u"Length (B):", None))
        self.len_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"8", None))
        self.len_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"7", None))
        self.len_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"6", None))
        self.len_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"5", None))

        self.label_27.setText(QCoreApplication.translate("Dialog", u"Timeout:", None))
        self.timeout_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"2", None))
        self.timeout_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"3", None))
        self.timeout_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"4", None))
        self.timeout_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"5", None))
        self.timeout_comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"10", None))
        self.timeout_comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"30", None))
        self.timeout_comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"50", None))
        self.timeout_comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"100", None))

        self.label_28.setText(QCoreApplication.translate("Dialog", u"Parity:", None))
        self.parity_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.parity_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Even", None))
        self.parity_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Odd", None))
        self.parity_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Mark", None))
        self.parity_comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Space", None))

        self.label_29.setText(QCoreApplication.translate("Dialog", u"StopBits:", None))
        self.bit_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.bit_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"1.5", None))
        self.bit_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"2", None))

        self.label_30.setText(QCoreApplication.translate("Dialog", u"Flow Control:", None))
        self.flow_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.flow_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Xon/Xoff", None))
        self.flow_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"RTS/CTS", None))
        self.flow_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"DSR/DTR", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"UI Language:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"English", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"T\u00fcrk\u00e7e", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Terminal Font:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Defult (System)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Dark", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Light", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"Theme:", None))
    # retranslateUi

