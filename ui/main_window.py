# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1127, 633)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setMinimumSize(QSize(0, 0))
        main_window.setMaximumSize(QSize(9290, 4095))
        main_window.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon(QIcon.fromTheme(u"applications-development"))
        main_window.setWindowIcon(icon)
        main_window.setWindowOpacity(1.000000000000000)
        self.actionAna_Ekran = QAction(main_window)
        self.actionAna_Ekran.setObjectName(u"actionAna_Ekran")
        self.actionHelp = QAction(main_window)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionCheck_for_updates = QAction(main_window)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionReset_terminal = QAction(main_window)
        self.actionReset_terminal.setObjectName(u"actionReset_terminal")
        self.actionClear_Cache = QAction(main_window)
        self.actionClear_Cache.setObjectName(u"actionClear_Cache")
        self.actionExit = QAction(main_window)
        self.actionExit.setObjectName(u"actionExit")
        self.actionNew = QAction(main_window)
        self.actionNew.setObjectName(u"actionNew")
        self.actionBasic_View = QAction(main_window)
        self.actionBasic_View.setObjectName(u"actionBasic_View")
        self.actionAdvanced_View = QAction(main_window)
        self.actionAdvanced_View.setObjectName(u"actionAdvanced_View")
        self.actionPreferences = QAction(main_window)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionMinimize = QAction(main_window)
        self.actionMinimize.setObjectName(u"actionMinimize")
        self.actionFull_Screen = QAction(main_window)
        self.actionFull_Screen.setObjectName(u"actionFull_Screen")
        self.actionHelp_2 = QAction(main_window)
        self.actionHelp_2.setObjectName(u"actionHelp_2")
        self.actionSave_As = QAction(main_window)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave = QAction(main_window)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.send_button = QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_4.addWidget(self.send_button)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        self.verticalLayout_config = QVBoxLayout()
        self.verticalLayout_config.setSpacing(6)
        self.verticalLayout_config.setObjectName(u"verticalLayout_config")
        self.verticalLayout_config.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout_config = QFormLayout()
        self.formLayout_config.setObjectName(u"formLayout_config")
        self.formLayout_config.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_config.setFormAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_config.setHorizontalSpacing(4)
        self.formLayout_config.setVerticalSpacing(2)
        self.label_46 = QLabel(self.centralwidget)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_config.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_46)

        self.refresh_button = QPushButton(self.centralwidget)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(0, QFormLayout.ItemRole.FieldRole, self.refresh_button)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_config.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.port_comboBox = QComboBox(self.centralwidget)
        self.port_comboBox.setObjectName(u"port_comboBox")
        self.port_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(1, QFormLayout.ItemRole.FieldRole, self.port_comboBox)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_config.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.baudrate_comboBox = QComboBox(self.centralwidget)
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

        self.formLayout_config.setWidget(2, QFormLayout.ItemRole.FieldRole, self.baudrate_comboBox)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_config.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.len_comboBox = QComboBox(self.centralwidget)
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.addItem("")
        self.len_comboBox.setObjectName(u"len_comboBox")
        self.len_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(3, QFormLayout.ItemRole.FieldRole, self.len_comboBox)

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_config.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.timeout_comboBox = QComboBox(self.centralwidget)
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

        self.formLayout_config.setWidget(4, QFormLayout.ItemRole.FieldRole, self.timeout_comboBox)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_config.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.parity_comboBox = QComboBox(self.centralwidget)
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.setObjectName(u"parity_comboBox")
        self.parity_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(5, QFormLayout.ItemRole.FieldRole, self.parity_comboBox)

        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_config.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_29)

        self.bit_comboBox = QComboBox(self.centralwidget)
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.addItem("")
        self.bit_comboBox.setObjectName(u"bit_comboBox")
        self.bit_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(6, QFormLayout.ItemRole.FieldRole, self.bit_comboBox)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_config.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.flow_comboBox = QComboBox(self.centralwidget)
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.addItem("")
        self.flow_comboBox.setObjectName(u"flow_comboBox")
        self.flow_comboBox.setMaximumSize(QSize(120, 16777215))

        self.formLayout_config.setWidget(7, QFormLayout.ItemRole.FieldRole, self.flow_comboBox)


        self.verticalLayout_config.addLayout(self.formLayout_config)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_config.addWidget(self.label_12)

        self.options_textEdit = QTextEdit(self.centralwidget)
        self.options_textEdit.setObjectName(u"options_textEdit")
        self.options_textEdit.setMaximumSize(QSize(205, 16777215))
        self.options_textEdit.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_config.addWidget(self.options_textEdit)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        font.setBold(False)
        self.label_9.setFont(font)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font)
        self.status_label.setStyleSheet(u"")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.status_label)


        self.verticalLayout_config.addLayout(self.formLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.start_button.setFont(font1)
        self.start_button.setAutoFillBackground(False)
        self.start_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.start_button)


        self.verticalLayout_config.addLayout(self.horizontalLayout_5)

        self.verticalLayout_config.setStretch(0, 2)

        self.gridLayout_2.addLayout(self.verticalLayout_config, 0, 1, 1, 1)

        self.data_textEdit = QTextEdit(self.centralwidget)
        self.data_textEdit.setObjectName(u"data_textEdit")
        self.data_textEdit.setAutoFillBackground(False)
        self.data_textEdit.setFrameShape(QFrame.Shape.Box)
        self.data_textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.data_textEdit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)
        self.data_textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.data_textEdit, 0, 0, 1, 1)

        self.send_data_text = QTextEdit(self.centralwidget)
        self.send_data_text.setObjectName(u"send_data_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.send_data_text.sizePolicy().hasHeightForWidth())
        self.send_data_text.setSizePolicy(sizePolicy1)
        self.send_data_text.setMaximumSize(QSize(5000, 28))
        self.send_data_text.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.send_data_text.setFrameShape(QFrame.Shape.Box)
        self.send_data_text.setFrameShadow(QFrame.Shadow.Sunken)
        self.send_data_text.setAcceptRichText(False)

        self.gridLayout_2.addWidget(self.send_data_text, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(main_window)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1127, 33))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSetup = QMenu(self.menuBar)
        self.menuSetup.setObjectName(u"menuSetup")
        self.menuControl = QMenu(self.menuBar)
        self.menuControl.setObjectName(u"menuControl")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuWindow = QMenu(self.menuBar)
        self.menuWindow.setObjectName(u"menuWindow")
        main_window.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuSetup.menuAction())
        self.menuBar.addAction(self.menuControl.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSetup.addAction(self.actionPreferences)
        self.menuControl.addAction(self.actionReset_terminal)
        self.menuControl.addAction(self.actionClear_Cache)
        self.menuHelp.addAction(self.actionHelp_2)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuWindow.addAction(self.actionBasic_View)
        self.menuWindow.addAction(self.actionAdvanced_View)
        self.menuWindow.addSeparator()

        self.retranslateUi(main_window)

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
        self.actionAbout.setText(QCoreApplication.translate("main_window", u"About", None))
        self.actionCheck_for_updates.setText(QCoreApplication.translate("main_window", u"Check for Updates", None))
        self.actionReset_terminal.setText(QCoreApplication.translate("main_window", u"Reset terminal", None))
        self.actionClear_Cache.setText(QCoreApplication.translate("main_window", u"Clear Cache", None))
        self.actionExit.setText(QCoreApplication.translate("main_window", u"Exit", None))
        self.actionNew.setText(QCoreApplication.translate("main_window", u"New..", None))
        self.actionBasic_View.setText(QCoreApplication.translate("main_window", u"Basic View", None))
        self.actionAdvanced_View.setText(QCoreApplication.translate("main_window", u"Advanced View", None))
        self.actionPreferences.setText(QCoreApplication.translate("main_window", u"Preferences..", None))
        self.actionMinimize.setText(QCoreApplication.translate("main_window", u"Minimize", None))
        self.actionFull_Screen.setText(QCoreApplication.translate("main_window", u"Full Screen", None))
        self.actionHelp_2.setText(QCoreApplication.translate("main_window", u"Help", None))
        self.actionSave_As.setText(QCoreApplication.translate("main_window", u"Save As..", None))
        self.actionSave.setText(QCoreApplication.translate("main_window", u"Save", None))
        self.send_button.setText(QCoreApplication.translate("main_window", u"Push Data", None))
        self.label_46.setText(QCoreApplication.translate("main_window", u"Refresh Port(s):", None))
        self.refresh_button.setText(QCoreApplication.translate("main_window", u"\u21bb", None))
        self.label_22.setText(QCoreApplication.translate("main_window", u"Selected Port:", None))
        self.label_25.setText(QCoreApplication.translate("main_window", u"Baud Rate:", None))
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

        self.label_26.setText(QCoreApplication.translate("main_window", u"Length (B):", None))
        self.len_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"8", None))
        self.len_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"7", None))
        self.len_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"6", None))
        self.len_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"5", None))

        self.label_27.setText(QCoreApplication.translate("main_window", u"Timeout:", None))
        self.timeout_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"2", None))
        self.timeout_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"3", None))
        self.timeout_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"4", None))
        self.timeout_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"5", None))
        self.timeout_comboBox.setItemText(4, QCoreApplication.translate("main_window", u"10", None))
        self.timeout_comboBox.setItemText(5, QCoreApplication.translate("main_window", u"30", None))
        self.timeout_comboBox.setItemText(6, QCoreApplication.translate("main_window", u"50", None))
        self.timeout_comboBox.setItemText(7, QCoreApplication.translate("main_window", u"100", None))

        self.label_28.setText(QCoreApplication.translate("main_window", u"Parity:", None))
        self.parity_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"None", None))
        self.parity_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"Even", None))
        self.parity_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"Odd", None))
        self.parity_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"Mark", None))
        self.parity_comboBox.setItemText(4, QCoreApplication.translate("main_window", u"Space", None))

        self.label_29.setText(QCoreApplication.translate("main_window", u"StopBits:", None))
        self.bit_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"1", None))
        self.bit_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"1.5", None))
        self.bit_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"2", None))

        self.label_30.setText(QCoreApplication.translate("main_window", u"Flow Control:", None))
        self.flow_comboBox.setItemText(0, QCoreApplication.translate("main_window", u"None", None))
        self.flow_comboBox.setItemText(1, QCoreApplication.translate("main_window", u"Xon/Xoff", None))
        self.flow_comboBox.setItemText(2, QCoreApplication.translate("main_window", u"RTS/CTS", None))
        self.flow_comboBox.setItemText(3, QCoreApplication.translate("main_window", u"DSR/DTR", None))

        self.label_12.setText(QCoreApplication.translate("main_window", u"Connection Options:", None))
        self.label_9.setText(QCoreApplication.translate("main_window", u"Status :", None))
        self.status_label.setText(QCoreApplication.translate("main_window", u"Not Connected", None))
        self.start_button.setText(QCoreApplication.translate("main_window", u"CONNECT", None))
        self.send_data_text.setPlaceholderText(QCoreApplication.translate("main_window", u"Please enter the data want to sent...", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("main_window", u"Edit", None))
        self.menuSetup.setTitle(QCoreApplication.translate("main_window", u"Settings", None))
        self.menuControl.setTitle(QCoreApplication.translate("main_window", u"Control", None))
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", u"Help", None))
        self.menuWindow.setTitle(QCoreApplication.translate("main_window", u"Window", None))
    # retranslateUi

