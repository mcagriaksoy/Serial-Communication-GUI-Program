# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(926, 574)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        main_window.setWindowIcon(icon)
        main_window.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(parent=main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 581))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 731, 521))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_23 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)
        self.data_textEdit = QtWidgets.QTextEdit(parent=self.gridLayoutWidget_2)
        self.data_textEdit.setAutoFillBackground(False)
        self.data_textEdit.setObjectName("data_textEdit")
        self.gridLayout_2.addWidget(self.data_textEdit, 2, 0, 1, 1)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(900, 390, 21, 135))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.command_edit_1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_5)
        self.command_edit_1.setMinimumSize(QtCore.QSize(19, 28))
        self.command_edit_1.setObjectName("command_edit_1")
        self.verticalLayout_5.addWidget(self.command_edit_1)
        self.command_edit_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_5)
        self.command_edit_2.setMinimumSize(QtCore.QSize(19, 28))
        self.command_edit_2.setObjectName("command_edit_2")
        self.verticalLayout_5.addWidget(self.command_edit_2)
        self.command_edit_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_5)
        self.command_edit_3.setMinimumSize(QtCore.QSize(19, 28))
        self.command_edit_3.setObjectName("command_edit_3")
        self.verticalLayout_5.addWidget(self.command_edit_3)
        self.command_edit_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_5)
        self.command_edit_4.setMinimumSize(QtCore.QSize(19, 28))
        self.command_edit_4.setObjectName("command_edit_4")
        self.verticalLayout_5.addWidget(self.command_edit_4)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(730, 390, 171, 135))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.saved_command_1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_6)
        self.saved_command_1.setObjectName("saved_command_1")
        self.verticalLayout_6.addWidget(self.saved_command_1)
        self.saved_command_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_6)
        self.saved_command_2.setObjectName("saved_command_2")
        self.verticalLayout_6.addWidget(self.saved_command_2)
        self.saved_command_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_6)
        self.saved_command_3.setObjectName("saved_command_3")
        self.verticalLayout_6.addWidget(self.saved_command_3)
        self.saved_command_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_6)
        self.saved_command_4.setObjectName("saved_command_4")
        self.verticalLayout_6.addWidget(self.saved_command_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(730, 260, 191, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.options_textEdit = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_4)
        self.options_textEdit.setObjectName("options_textEdit")
        self.verticalLayout_4.addWidget(self.options_textEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.end_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.end_button.setFont(font)
        self.end_button.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.end_button.setObjectName("end_button")
        self.horizontalLayout_3.addWidget(self.end_button)
        self.start_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_3.addWidget(self.start_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.send_data_text = QtWidgets.QTextEdit(parent=self.tab)
        self.send_data_text.setGeometry(QtCore.QRect(70, 520, 501, 31))
        self.send_data_text.setObjectName("send_data_text")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(730, 230, 191, 21))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.status_label = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("")
        self.status_label.setObjectName("status_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.status_label)
        self.save_txt_button = QtWidgets.QPushButton(parent=self.tab)
        self.save_txt_button.setGeometry(QtCore.QRect(640, 520, 91, 31))
        self.save_txt_button.setObjectName("save_txt_button")
        self.send_data_button = QtWidgets.QPushButton(parent=self.tab)
        self.send_data_button.setGeometry(QtCore.QRect(570, 520, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.send_data_button.setFont(font)
        self.send_data_button.setObjectName("send_data_button")
        self.label_22 = QtWidgets.QLabel(parent=self.tab)
        self.label_22.setGeometry(QtCore.QRect(0, 520, 71, 31))
        self.label_22.setObjectName("label_22")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(732, 28, 191, 231))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_16 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.port_comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.port_comboBox.setObjectName("port_comboBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.port_comboBox)
        self.label_17 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.baudrate_comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.baudrate_comboBox.setObjectName("baudrate_comboBox")
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
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.baudrate_comboBox)
        self.label_18 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_18)
        self.len_comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.len_comboBox.setObjectName("len_comboBox")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.len_comboBox)
        self.label_19 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_19)
        self.timeout_comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.timeout_comboBox.setObjectName("timeout_comboBox")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.timeout_comboBox.addItem("")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.timeout_comboBox)
        self.label_20 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_20)
        self.parity_comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.parity_comboBox.setObjectName("parity_comboBox")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.parity_comboBox)
        self.label_21 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.bit_comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.bit_comboBox.setObjectName("bit_comboBox")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bit_comboBox)
        self.label_24 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_24)
        self.bit_comboBox_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.bit_comboBox_2.setObjectName("bit_comboBox_2")
        self.bit_comboBox_2.addItem("")
        self.bit_comboBox_2.addItem("")
        self.bit_comboBox_2.addItem("")
        self.bit_comboBox_2.addItem("")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bit_comboBox_2)
        self.label_46 = QtWidgets.QLabel(parent=self.tab)
        self.label_46.setGeometry(QtCore.QRect(740, 10, 151, 16))
        self.label_46.setObjectName("label_46")
        self.refresh_button = QtWidgets.QPushButton(parent=self.tab)
        self.refresh_button.setGeometry(QtCore.QRect(890, 0, 31, 28))
        self.refresh_button.setObjectName("refresh_button")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 30, 681, 71))
        self.textEdit_3.setUndoRedoEnabled(False)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setAcceptRichText(False)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setGeometry(QtCore.QRect(90, 116, 681, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(820, 530, 101, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        main_window.setCentralWidget(self.centralwidget)
        self.actionAna_Ekran = QtGui.QAction(parent=main_window)
        self.actionAna_Ekran.setObjectName("actionAna_Ekran")
        self.actionHelp = QtGui.QAction(parent=main_window)
        self.actionHelp.setObjectName("actionHelp")

        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "AFCOM Client (A free COM port data transfer client)"))
        main_window.setStatusTip(_translate("main_window", "Mehmet Cagri Aksoy"))
        main_window.setWhatsThis(_translate("main_window", "Serial Communication Program Mehmet Cagri Aksoy"))
        self.label_23.setText(_translate("main_window", "Gathering Data (Rx)"))
        self.command_edit_1.setText(_translate("main_window", "..."))
        self.command_edit_2.setText(_translate("main_window", "..."))
        self.command_edit_3.setText(_translate("main_window", "..."))
        self.command_edit_4.setText(_translate("main_window", "..."))
        self.saved_command_1.setText(_translate("main_window", "Command 1"))
        self.saved_command_2.setText(_translate("main_window", "Command 2"))
        self.saved_command_3.setText(_translate("main_window", "Command 3"))
        self.saved_command_4.setText(_translate("main_window", "Command 4"))
        self.label_11.setText(_translate("main_window", "Connection Options:"))
        self.end_button.setText(_translate("main_window", "STOP"))
        self.start_button.setText(_translate("main_window", "START"))
        self.label_8.setText(_translate("main_window", "Port Status :"))
        self.status_label.setText(_translate("main_window", "Not Connected"))
        self.save_txt_button.setText(_translate("main_window", "Save as .txt"))
        self.send_data_button.setText(_translate("main_window", "SEND"))
        self.label_22.setText(_translate("main_window", "Tx Data:"))
        self.label_16.setText(_translate("main_window", "Selected Port:"))
        self.label_17.setText(_translate("main_window", "Baud Rate:"))
        self.baudrate_comboBox.setItemText(0, _translate("main_window", "9600"))
        self.baudrate_comboBox.setItemText(1, _translate("main_window", "57600"))
        self.baudrate_comboBox.setItemText(2, _translate("main_window", "115200"))
        self.baudrate_comboBox.setItemText(3, _translate("main_window", "110"))
        self.baudrate_comboBox.setItemText(4, _translate("main_window", "300"))
        self.baudrate_comboBox.setItemText(5, _translate("main_window", "1200"))
        self.baudrate_comboBox.setItemText(6, _translate("main_window", "2400"))
        self.baudrate_comboBox.setItemText(7, _translate("main_window", "4800"))
        self.baudrate_comboBox.setItemText(8, _translate("main_window", "19200"))
        self.baudrate_comboBox.setItemText(9, _translate("main_window", "38400"))
        self.label_18.setText(_translate("main_window", "Length (B):"))
        self.len_comboBox.setItemText(0, _translate("main_window", "8"))
        self.len_comboBox.setItemText(1, _translate("main_window", "7"))
        self.len_comboBox.setItemText(2, _translate("main_window", "6"))
        self.len_comboBox.setItemText(3, _translate("main_window", "5"))
        self.label_19.setText(_translate("main_window", "Timeout:"))
        self.timeout_comboBox.setItemText(0, _translate("main_window", "2"))
        self.timeout_comboBox.setItemText(1, _translate("main_window", "3"))
        self.timeout_comboBox.setItemText(2, _translate("main_window", "4"))
        self.timeout_comboBox.setItemText(3, _translate("main_window", "5"))
        self.timeout_comboBox.setItemText(4, _translate("main_window", "10"))
        self.timeout_comboBox.setItemText(5, _translate("main_window", "30"))
        self.timeout_comboBox.setItemText(6, _translate("main_window", "50"))
        self.timeout_comboBox.setItemText(7, _translate("main_window", "100"))
        self.label_20.setText(_translate("main_window", "Parity:"))
        self.parity_comboBox.setItemText(0, _translate("main_window", "None"))
        self.parity_comboBox.setItemText(1, _translate("main_window", "Even"))
        self.parity_comboBox.setItemText(2, _translate("main_window", "Odd"))
        self.parity_comboBox.setItemText(3, _translate("main_window", "Mark"))
        self.parity_comboBox.setItemText(4, _translate("main_window", "Space"))
        self.label_21.setText(_translate("main_window", "StopBits:"))
        self.bit_comboBox.setItemText(0, _translate("main_window", "1"))
        self.bit_comboBox.setItemText(1, _translate("main_window", "1.5"))
        self.bit_comboBox.setItemText(2, _translate("main_window", "2"))
        self.label_24.setText(_translate("main_window", "Flow Control:"))
        self.bit_comboBox_2.setItemText(0, _translate("main_window", "none"))
        self.bit_comboBox_2.setItemText(1, _translate("main_window", "Xon/Xoff"))
        self.bit_comboBox_2.setItemText(2, _translate("main_window", "RTS/CTS"))
        self.bit_comboBox_2.setItemText(3, _translate("main_window", "DSR/DTR"))
        self.label_46.setText(_translate("main_window", "Settings:           Refresh:"))
        self.refresh_button.setText(_translate("main_window", "↻"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("main_window", "Main Page"))
        self.textEdit_3.setHtml(_translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">The AFCOM (aka Serial communication GUI program) tool is a software application that allows users to send and receive data via the serial port (COM port) of their computer. The tool can be used for various purposes, such as testing, debugging, or communicating with other devices that use the serial protocol.</span></p></body></html>"))
        self.label.setText(_translate("main_window", "Feel free to ask any questions or bug report on: https://github.com/mcagriaksoy/Serial-Communication-GUI-Program"))
        self.label_3.setText(_translate("main_window", "Version 2024.04"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("main_window", "About"))
        self.actionAna_Ekran.setText(_translate("main_window", "Ana Ekran"))
        self.actionHelp.setText(_translate("main_window", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())
