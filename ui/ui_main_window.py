# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(929, 579)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(600, 579))
        main_window.setMaximumSize(QSize(929, 579))
        main_window.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        main_window.setWindowIcon(icon)
        main_window.setWindowOpacity(1.000000000000000)
        self.actionAna_Ekran = QAction(main_window)
        self.actionAna_Ekran.setObjectName(u"actionAna_Ekran")
        self.actionHelp = QAction(main_window)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 931, 581))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 721, 511))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)

        self.data_textEdit = QTextEdit(self.gridLayoutWidget_2)
        self.data_textEdit.setObjectName(u"data_textEdit")
        self.data_textEdit.setAutoFillBackground(False)
        self.data_textEdit.setFrameShape(QFrame.Shape.Box)
        self.data_textEdit.setFrameShadow(QFrame.Shadow.Raised)
        self.data_textEdit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.data_textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.data_textEdit, 2, 0, 1, 1)

        self.verticalLayoutWidget_5 = QWidget(self.tab)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(900, 390, 21, 132))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.command_edit_1 = QPushButton(self.verticalLayoutWidget_5)
        self.command_edit_1.setObjectName(u"command_edit_1")
        self.command_edit_1.setMinimumSize(QSize(19, 28))
        font = QFont()
        font.setPointSize(8)
        self.command_edit_1.setFont(font)

        self.verticalLayout_5.addWidget(self.command_edit_1)

        self.command_edit_2 = QPushButton(self.verticalLayoutWidget_5)
        self.command_edit_2.setObjectName(u"command_edit_2")
        self.command_edit_2.setMinimumSize(QSize(19, 28))
        self.command_edit_2.setFont(font)

        self.verticalLayout_5.addWidget(self.command_edit_2)

        self.command_edit_3 = QPushButton(self.verticalLayoutWidget_5)
        self.command_edit_3.setObjectName(u"command_edit_3")
        self.command_edit_3.setMinimumSize(QSize(19, 28))
        self.command_edit_3.setFont(font)

        self.verticalLayout_5.addWidget(self.command_edit_3)

        self.command_edit_4 = QPushButton(self.verticalLayoutWidget_5)
        self.command_edit_4.setObjectName(u"command_edit_4")
        self.command_edit_4.setMinimumSize(QSize(19, 28))
        self.command_edit_4.setFont(font)

        self.verticalLayout_5.addWidget(self.command_edit_4)

        self.verticalLayoutWidget_6 = QWidget(self.tab)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(730, 390, 171, 121))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.saved_command_1 = QPushButton(self.verticalLayoutWidget_6)
        self.saved_command_1.setObjectName(u"saved_command_1")

        self.verticalLayout_6.addWidget(self.saved_command_1)

        self.saved_command_2 = QPushButton(self.verticalLayoutWidget_6)
        self.saved_command_2.setObjectName(u"saved_command_2")

        self.verticalLayout_6.addWidget(self.saved_command_2)

        self.saved_command_3 = QPushButton(self.verticalLayoutWidget_6)
        self.saved_command_3.setObjectName(u"saved_command_3")

        self.verticalLayout_6.addWidget(self.saved_command_3)

        self.saved_command_4 = QPushButton(self.verticalLayoutWidget_6)
        self.saved_command_4.setObjectName(u"saved_command_4")

        self.verticalLayout_6.addWidget(self.saved_command_4)

        self.verticalLayoutWidget_4 = QWidget(self.tab)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(730, 260, 191, 131))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.verticalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)

        self.options_textEdit = QTextEdit(self.verticalLayoutWidget_4)
        self.options_textEdit.setObjectName(u"options_textEdit")
        self.options_textEdit.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_4.addWidget(self.options_textEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.end_button = QPushButton(self.verticalLayoutWidget_4)
        self.end_button.setObjectName(u"end_button")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.end_button.setFont(font1)
        self.end_button.setAutoFillBackground(False)
        self.end_button.setStyleSheet(u"")
        self.end_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_3.addWidget(self.end_button)

        self.start_button = QPushButton(self.verticalLayoutWidget_4)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setFont(font1)
        self.start_button.setAutoFillBackground(False)
        self.start_button.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.start_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.formLayoutWidget_3 = QWidget(self.tab)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(730, 230, 191, 21))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.label_8.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.status_label = QLabel(self.formLayoutWidget_3)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font2)
        self.status_label.setStyleSheet(u"")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.status_label)

        self.formLayoutWidget_4 = QWidget(self.tab)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(732, 28, 191, 231))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.formLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.port_comboBox = QComboBox(self.formLayoutWidget_4)
        self.port_comboBox.setObjectName(u"port_comboBox")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.port_comboBox)

        self.label_17 = QLabel(self.formLayoutWidget_4)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.baudrate_comboBox = QComboBox(self.formLayoutWidget_4)
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

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.baudrate_comboBox)

        self.label_18 = QLabel(self.formLayoutWidget_4)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_18)

        self.len_comboBox = QComboBox(self.formLayoutWidget_4)
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.setObjectName(u"len_comboBox")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.len_comboBox)

        self.label_19 = QLabel(self.formLayoutWidget_4)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.timeout_comboBox = QComboBox(self.formLayoutWidget_4)
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.setObjectName(u"timeout_comboBox")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.timeout_comboBox)

        self.label_20 = QLabel(self.formLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_20)

        self.parity_comboBox = QComboBox(self.formLayoutWidget_4)
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.setObjectName(u"parity_comboBox")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.parity_comboBox)

        self.label_21 = QLabel(self.formLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_21)

        self.bit_comboBox = QComboBox(self.formLayoutWidget_4)
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.setObjectName(u"bit_comboBox")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.bit_comboBox)

        self.label_24 = QLabel(self.formLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_24)

        self.flow_comboBox = QComboBox(self.formLayoutWidget_4)
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.setObjectName(u"flow_comboBox")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.flow_comboBox)

        self.label_46 = QLabel(self.tab)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(740, 10, 151, 16))
        self.refresh_button = QPushButton(self.tab)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(890, 0, 31, 28))
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 520, 901, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.send_data_text = QTextEdit(self.horizontalLayoutWidget)
        self.send_data_text.setObjectName(u"send_data_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.send_data_text.sizePolicy().hasHeightForWidth())
        self.send_data_text.setSizePolicy(sizePolicy1)
        self.send_data_text.setMaximumSize(QSize(465, 28))
        self.send_data_text.setFrameShape(QFrame.Shape.Box)
        self.send_data_text.setFrameShadow(QFrame.Shadow.Plain)
        self.send_data_text.setAcceptRichText(False)

        self.horizontalLayout.addWidget(self.send_data_text)

        self.send_button = QPushButton(self.horizontalLayoutWidget)
        self.send_button.setObjectName(u"send_button")

        self.horizontalLayout.addWidget(self.send_button)

        self.save_txt_button = QPushButton(self.horizontalLayoutWidget)
        self.save_txt_button.setObjectName(u"save_txt_button")

        self.horizontalLayout.addWidget(self.save_txt_button)

        self.view_change = QPushButton(self.horizontalLayoutWidget)
        self.view_change.setObjectName(u"view_change")
        self.view_change.setFont(font1)

        self.horizontalLayout.addWidget(self.view_change)

        self.night_mode = QPushButton(self.horizontalLayoutWidget)
        self.night_mode.setObjectName(u"night_mode")

        self.horizontalLayout.addWidget(self.night_mode)

        self.clear_buffer_button = QPushButton(self.horizontalLayoutWidget)
        self.clear_buffer_button.setObjectName(u"clear_buffer_button")

        self.horizontalLayout.addWidget(self.clear_buffer_button)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit_3 = QTextEdit(self.tab_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 10, 911, 491))
        self.textEdit_3.setUndoRedoEnabled(False)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setAcceptRichText(False)
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 530, 101, 16))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 530, 331, 16))
        self.label_2.setOpenExternalLinks(True)
        self.tabWidget.addTab(self.tab_2, "")
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"AFCOM Client (A free COM port data transfer client)", None))
#if QT_CONFIG(statustip)
        main_window.setStatusTip(QCoreApplication.translate("main_window", u"Mehmet Cagri Aksoy", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        main_window.setWhatsThis(QCoreApplication.translate("main_window", u"Serial Communication Program Mehmet Cagri Aksoy", None))
#endif // QT_CONFIG(whatsthis)
        self.actionAna_Ekran.setText(QCoreApplication.translate("main_window", u"Ana Ekran", None))
        self.actionHelp.setText(QCoreApplication.translate("main_window", u"Help", None))
        self.label_23.setText(QCoreApplication.translate("main_window", u"Gathering Data (Rx)", None))
        self.command_edit_1.setText(QCoreApplication.translate("main_window", u"...", None))
        self.command_edit_2.setText(QCoreApplication.translate("main_window", u"...", None))
        self.command_edit_3.setText(QCoreApplication.translate("main_window", u"...", None))
        self.command_edit_4.setText(QCoreApplication.translate("main_window", u"...", None))
        self.saved_command_1.setText(QCoreApplication.translate("main_window", u"Command 1", None))
        self.saved_command_2.setText(QCoreApplication.translate("main_window", u"Command 2", None))
        self.saved_command_3.setText(QCoreApplication.translate("main_window", u"Command 3", None))
        self.saved_command_4.setText(QCoreApplication.translate("main_window", u"Command 4", None))
        self.label_11.setText(QCoreApplication.translate("main_window", u"Connection Options:", None))
        self.end_button.setText(QCoreApplication.translate("main_window", u"STOP", None))
        self.start_button.setText(QCoreApplication.translate("main_window", u"START", None))
        self.label_8.setText(QCoreApplication.translate("main_window", u"Port Status :", None))
        self.status_label.setText(QCoreApplication.translate("main_window", u"Not Connected", None))
        self.label_16.setText(QCoreApplication.translate("main_window", u"Selected Port:", None))
        self.label_17.setText(QCoreApplication.translate("main_window", u"Baud Rate:", None))
        self.baudrate_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"9600", None))
        self.baudrate_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"57600", None))
        self.baudrate_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"115200", None))
        self.baudrate_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"110", None))
        self.baudrate_comboBox.setItemText(4, QCoreApplication.translate("main_window", u"300", None))
        self.baudrate_comboBox.setItemText(5, QCoreApplication.translate("main_window", u"1200", None))
        self.baudrate_comboBox.setItemText(6, QCoreApplication.translate("main_window", u"2400", None))
        self.baudrate_comboBox.setItemText(7, QCoreApplication.translate("main_window", u"4800", None))
        self.baudrate_comboBox.setItemText(8, QCoreApplication.translate("main_window", u"19200", None))
        self.baudrate_comboBox.setItemText(9, QCoreApplication.translate("main_window", u"38400", None))

        self.label_18.setText(QCoreApplication.translate("main_window", u"Length (B):", None))
        self.len_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"8", None))
        self.len_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"7", None))
        self.len_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"6", None))
        self.len_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"5", None))

        self.label_19.setText(QCoreApplication.translate("main_window", u"Timeout:", None))
        self.timeout_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"2", None))
        self.timeout_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"3", None))
        self.timeout_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"4", None))
        self.timeout_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"5", None))
        self.timeout_comboBox.setItemText(4, QCoreApplication.translate("main_window", u"10", None))
        self.timeout_comboBox.setItemText(5, QCoreApplication.translate("main_window", u"30", None))
        self.timeout_comboBox.setItemText(6, QCoreApplication.translate("main_window", u"50", None))
        self.timeout_comboBox.setItemText(7, QCoreApplication.translate("main_window", u"100", None))

        self.label_20.setText(QCoreApplication.translate("main_window", u"Parity:", None))
        self.parity_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"None", None))
        self.parity_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"Even", None))
        self.parity_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"Odd", None))
        self.parity_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"Mark", None))
        self.parity_comboBox.setItemText(4, QCoreApplication.translate("main_window", u"Space", None))

        self.label_21.setText(QCoreApplication.translate("main_window", u"StopBits:", None))
        self.bit_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"1", None))
        self.bit_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"1.5", None))
        self.bit_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"2", None))

        self.label_24.setText(QCoreApplication.translate("main_window", u"Flow Control:", None))
        self.flow_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"None", None))
        self.flow_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"Xon/Xoff", None))
        self.flow_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"RTS/CTS", None))
        self.flow_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"DSR/DTR", None))

        self.label_46.setText(QCoreApplication.translate("main_window", u"Settings:                   Refresh:", None))
        self.refresh_button.setText(QCoreApplication.translate("main_window", u"\u21bb", None))
        self.send_data_text.setPlaceholderText(QCoreApplication.translate("main_window", u"Please enter the data want to sent...", None))
        self.send_button.setText(QCoreApplication.translate("main_window", u"SEND", None))
#if QT_CONFIG(tooltip)
        self.save_txt_button.setToolTip(QCoreApplication.translate("main_window", u"Save the output", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.save_txt_button.setStatusTip(QCoreApplication.translate("main_window", u"Save the output", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.save_txt_button.setWhatsThis(QCoreApplication.translate("main_window", u"Save the output", None))
#endif // QT_CONFIG(whatsthis)
        self.save_txt_button.setText(QCoreApplication.translate("main_window", u"Save as .txt", None))
#if QT_CONFIG(tooltip)
        self.view_change.setToolTip(QCoreApplication.translate("main_window", u"Click Here to go to the Simple View", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.view_change.setStatusTip(QCoreApplication.translate("main_window", u"Click Here to go to the Simple View", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.view_change.setWhatsThis(QCoreApplication.translate("main_window", u"Click Here to go to the Simple View", None))
#endif // QT_CONFIG(whatsthis)
        self.view_change.setText(QCoreApplication.translate("main_window", u"<<", None))
        self.night_mode.setText(QCoreApplication.translate("main_window", u"\ud83c\udf18 Dark Mode", None))
        self.clear_buffer_button.setText(QCoreApplication.translate("main_window", u"Clear Buffer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main_window", u"Main Page", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("main_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Information</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:12pt;\">The AFCOM (aka Serial communication GUI program) tool is a software application that allows users to send and receive data via the serial port (COM port) of their computer. The tool can be used for various purposes, such as testing, debugging, or communicating with other devices that use the serial protocol. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Features</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"just"
                        "ify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The COM port tool has the following features: It supports multiple COM ports and can detect the available ports automatically. It allows users to configure the parameters of the serial communication, such as baud rate. It provides a user-friendly interface that shows the transmitted and received data in hexadecimal, decimal, ASCII, or binary formats. It allows users to save and load the data to and from files.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Legal Information</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This application incorporates Qt for Python (PySide), which is licensed under the GNU Lesser General Public License version 3 (LGPLv3). By using this software, you agree to comply with the terms of the LGPLv3 license. For more information about Qt for Python, visit https://www.qt.io/qt-for-python. A copy of the LGPLv3 license is included with this application.</span></p>\n"
"<p align=\"justify\" style=\"-qt"
                        "-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Version 2024.12", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p><a href=\"https://github.com/mcagriaksoy/Serial-Communication-GUI-Program\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p>Feel free to ask any questions or bug report on <a href=\"https://github.com/mcagriaksoy/Serial-Communication-GUI-Program\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main_window", u"About", None))
    # retranslateUi

