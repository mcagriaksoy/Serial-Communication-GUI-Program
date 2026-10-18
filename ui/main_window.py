# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1080, 720)
        main_window.setMinimumSize(QSize(820, 560))
        icon = QIcon()
        icon.addFile(u":/res/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        main_window.setWindowIcon(icon)
        self.actionNew = QAction(main_window)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave = QAction(main_window)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(main_window)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(main_window)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCopy = QAction(main_window)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionSelect_All = QAction(main_window)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        self.actionClear_Screen = QAction(main_window)
        self.actionClear_Screen.setObjectName(u"actionClear_Screen")
        self.actionClear_Cache = QAction(main_window)
        self.actionClear_Cache.setObjectName(u"actionClear_Cache")
        self.actionReset_terminal = QAction(main_window)
        self.actionReset_terminal.setObjectName(u"actionReset_terminal")
        self.actionPreferences = QAction(main_window)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionBasic_View = QAction(main_window)
        self.actionBasic_View.setObjectName(u"actionBasic_View")
        self.actionAdvanced_View = QAction(main_window)
        self.actionAdvanced_View.setObjectName(u"actionAdvanced_View")
        self.actionHelp_2 = QAction(main_window)
        self.actionHelp_2.setObjectName(u"actionHelp_2")
        self.actionCheck_for_updates = QAction(main_window)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(14, 14, 14, 14)
        self.terminalPanel = QWidget(self.centralwidget)
        self.terminalPanel.setObjectName(u"terminalPanel")
        self.terminalLayout = QVBoxLayout(self.terminalPanel)
        self.terminalLayout.setSpacing(6)
        self.terminalLayout.setObjectName(u"terminalLayout")
        self.terminalLayout.setContentsMargins(0, 0, 0, 0)
        self.terminalHeaderLayout = QHBoxLayout()
        self.terminalHeaderLayout.setSpacing(8)
        self.terminalHeaderLayout.setObjectName(u"terminalHeaderLayout")
        self.terminalTitleLabel = QLabel(self.terminalPanel)
        self.terminalTitleLabel.setObjectName(u"terminalTitleLabel")

        self.terminalHeaderLayout.addWidget(self.terminalTitleLabel)

        self.terminalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.terminalHeaderLayout.addItem(self.terminalSpacer)

        self.rxCountLabel = QLabel(self.terminalPanel)
        self.rxCountLabel.setObjectName(u"rxCountLabel")

        self.terminalHeaderLayout.addWidget(self.rxCountLabel)

        self.txCountLabel = QLabel(self.terminalPanel)
        self.txCountLabel.setObjectName(u"txCountLabel")

        self.terminalHeaderLayout.addWidget(self.txCountLabel)

        self.clearButton = QPushButton(self.terminalPanel)
        self.clearButton.setObjectName(u"clearButton")

        self.terminalHeaderLayout.addWidget(self.clearButton)


        self.terminalLayout.addLayout(self.terminalHeaderLayout)

        self.data_textEdit = QTextEdit(self.terminalPanel)
        self.data_textEdit.setObjectName(u"data_textEdit")
        self.data_textEdit.setReadOnly(True)
        self.data_textEdit.setFrameShape(QFrame.Shape.NoFrame)

        self.terminalLayout.addWidget(self.data_textEdit)


        self.gridLayout.addWidget(self.terminalPanel, 1, 0, 1, 1)

        self.configPanel = QWidget(self.centralwidget)
        self.configPanel.setObjectName(u"configPanel")
        self.configPanel.setMinimumSize(QSize(198, 0))
        self.configPanel.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout_config = QVBoxLayout(self.configPanel)
        self.verticalLayout_config.setSpacing(12)
        self.verticalLayout_config.setObjectName(u"verticalLayout_config")
        self.verticalLayout_config.setContentsMargins(0, 0, 0, 0)
        self.connectionGroup = QGroupBox(self.configPanel)
        self.connectionGroup.setObjectName(u"connectionGroup")
        self.formLayout_config = QFormLayout(self.connectionGroup)
        self.formLayout_config.setObjectName(u"formLayout_config")
        self.formLayout_config.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_config.setHorizontalSpacing(10)
        self.formLayout_config.setVerticalSpacing(8)
        self.refresh_button = QPushButton(self.connectionGroup)
        self.refresh_button.setObjectName(u"refresh_button")

        self.formLayout_config.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.refresh_button)

        self.label_22 = QLabel(self.connectionGroup)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_config.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.port_comboBox = QComboBox(self.connectionGroup)
        self.port_comboBox.setObjectName(u"port_comboBox")

        self.formLayout_config.setWidget(1, QFormLayout.ItemRole.FieldRole, self.port_comboBox)

        self.label_25 = QLabel(self.connectionGroup)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_config.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.baudrate_comboBox = QComboBox(self.connectionGroup)
        self.baudrate_comboBox.setObjectName(u"baudrate_comboBox")

        self.formLayout_config.setWidget(2, QFormLayout.ItemRole.FieldRole, self.baudrate_comboBox)

        self.label_26 = QLabel(self.connectionGroup)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_config.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.len_comboBox = QComboBox(self.connectionGroup)
        self.len_comboBox.setObjectName(u"len_comboBox")

        self.formLayout_config.setWidget(3, QFormLayout.ItemRole.FieldRole, self.len_comboBox)

        self.label_28 = QLabel(self.connectionGroup)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_config.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.parity_comboBox = QComboBox(self.connectionGroup)
        self.parity_comboBox.setObjectName(u"parity_comboBox")

        self.formLayout_config.setWidget(4, QFormLayout.ItemRole.FieldRole, self.parity_comboBox)

        self.label_29 = QLabel(self.connectionGroup)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_config.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_29)

        self.bit_comboBox = QComboBox(self.connectionGroup)
        self.bit_comboBox.setObjectName(u"bit_comboBox")

        self.formLayout_config.setWidget(5, QFormLayout.ItemRole.FieldRole, self.bit_comboBox)

        self.label_30 = QLabel(self.connectionGroup)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_config.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.flow_comboBox = QComboBox(self.connectionGroup)
        self.flow_comboBox.setObjectName(u"flow_comboBox")

        self.formLayout_config.setWidget(6, QFormLayout.ItemRole.FieldRole, self.flow_comboBox)

        self.label_27 = QLabel(self.connectionGroup)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_config.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.timeout_comboBox = QComboBox(self.connectionGroup)
        self.timeout_comboBox.setObjectName(u"timeout_comboBox")

        self.formLayout_config.setWidget(7, QFormLayout.ItemRole.FieldRole, self.timeout_comboBox)

        self.label = QLabel(self.connectionGroup)
        self.label.setObjectName(u"label")

        self.formLayout_config.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEnd_comboBox = QComboBox(self.connectionGroup)
        self.lineEnd_comboBox.setObjectName(u"lineEnd_comboBox")

        self.formLayout_config.setWidget(8, QFormLayout.ItemRole.FieldRole, self.lineEnd_comboBox)


        self.verticalLayout_config.addWidget(self.connectionGroup)

        self.start_button = QPushButton(self.configPanel)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout_config.addWidget(self.start_button)

        self.statusRowLayout = QHBoxLayout()
        self.statusRowLayout.setSpacing(6)
        self.statusRowLayout.setObjectName(u"statusRowLayout")
        self.statusDot = QLabel(self.configPanel)
        self.statusDot.setObjectName(u"statusDot")
        self.statusDot.setMinimumSize(QSize(12, 12))
        self.statusDot.setMaximumSize(QSize(12, 12))

        self.statusRowLayout.addWidget(self.statusDot)

        self.status_label = QLabel(self.configPanel)
        self.status_label.setObjectName(u"status_label")

        self.statusRowLayout.addWidget(self.status_label)

        self.statusSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.statusRowLayout.addItem(self.statusSpacer)


        self.verticalLayout_config.addLayout(self.statusRowLayout)

        self.infoGroup = QGroupBox(self.configPanel)
        self.infoGroup.setObjectName(u"infoGroup")
        self.infoGroup.setMaximumSize(QSize(16777215, 130))
        self.infoLayout = QVBoxLayout(self.infoGroup)
        self.infoLayout.setObjectName(u"infoLayout")
        self.options_textEdit = QTextEdit(self.infoGroup)
        self.options_textEdit.setObjectName(u"options_textEdit")
        self.options_textEdit.setReadOnly(True)
        self.options_textEdit.setFrameShape(QFrame.Shape.NoFrame)

        self.infoLayout.addWidget(self.options_textEdit)


        self.verticalLayout_config.addWidget(self.infoGroup)

        self.configSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_config.addItem(self.configSpacer)


        self.gridLayout.addWidget(self.configPanel, 1, 1, 1, 1)

        self.sendFrame = QFrame(self.centralwidget)
        self.sendFrame.setObjectName(u"sendFrame")
        self.sendFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.sendFrame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 8, 12, 8)
        self.send_data_text = QTextEdit(self.sendFrame)
        self.send_data_text.setObjectName(u"send_data_text")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_data_text.sizePolicy().hasHeightForWidth())
        self.send_data_text.setSizePolicy(sizePolicy)
        self.send_data_text.setMinimumSize(QSize(0, 40))
        self.send_data_text.setMaximumSize(QSize(16777215, 72))
        self.send_data_text.setAcceptRichText(False)

        self.horizontalLayout.addWidget(self.send_data_text)

        self.indicate_button = QRadioButton(self.sendFrame)
        self.indicate_button.setObjectName(u"indicate_button")
        self.indicate_button.setMinimumSize(QSize(18, 18))
        self.indicate_button.setMaximumSize(QSize(18, 18))
        self.indicate_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.indicate_button)

        self.send_button = QPushButton(self.sendFrame)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setMinimumSize(QSize(120, 40))

        self.horizontalLayout.addWidget(self.send_button)


        self.gridLayout.addWidget(self.sendFrame, 2, 0, 1, 1)

        self.donateButton = QPushButton(self.centralwidget)
        self.donateButton.setObjectName(u"donateButton")
        self.donateButton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.donateButton, 2, 1, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(main_window)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1080, 26))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSetup = QMenu(self.menuBar)
        self.menuSetup.setObjectName(u"menuSetup")
        self.menuControl = QMenu(self.menuBar)
        self.menuControl.setObjectName(u"menuControl")
        self.menuWindow = QMenu(self.menuBar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        main_window.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuSetup.menuAction())
        self.menuBar.addAction(self.menuControl.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClear_Screen)
        self.menuEdit.addAction(self.actionClear_Cache)
        self.menuSetup.addAction(self.actionPreferences)
        self.menuControl.addAction(self.actionReset_terminal)
        self.menuWindow.addAction(self.actionBasic_View)
        self.menuWindow.addAction(self.actionAdvanced_View)
        self.menuHelp.addAction(self.actionHelp_2)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"AFCOM Client - Serial Communication GUI", None))
        self.actionNew.setText(QCoreApplication.translate("main_window", u"New", None))
        self.actionSave.setText(QCoreApplication.translate("main_window", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("main_window", u"Save As\u2026", None))
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("main_window", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("main_window", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_All.setText(QCoreApplication.translate("main_window", u"Select All", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_All.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear_Screen.setText(QCoreApplication.translate("main_window", u"Clear Screen", None))
        self.actionClear_Cache.setText(QCoreApplication.translate("main_window", u"Clear Buffers", None))
        self.actionReset_terminal.setText(QCoreApplication.translate("main_window", u"Reset Terminal", None))
        self.actionPreferences.setText(QCoreApplication.translate("main_window", u"Preferences\u2026", None))
#if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionBasic_View.setText(QCoreApplication.translate("main_window", u"Basic View", None))
        self.actionAdvanced_View.setText(QCoreApplication.translate("main_window", u"Advanced View", None))
        self.actionHelp_2.setText(QCoreApplication.translate("main_window", u"Help", None))
#if QT_CONFIG(shortcut)
        self.actionHelp_2.setShortcut(QCoreApplication.translate("main_window", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionCheck_for_updates.setText(QCoreApplication.translate("main_window", u"Check for Updates", None))
        self.actionAbout.setText(QCoreApplication.translate("main_window", u"About", None))
        self.terminalTitleLabel.setText(QCoreApplication.translate("main_window", u"Terminal", None))
        self.rxCountLabel.setText(QCoreApplication.translate("main_window", u"RX 0 B", None))
        self.txCountLabel.setText(QCoreApplication.translate("main_window", u"TX 0 B", None))
        self.clearButton.setText(QCoreApplication.translate("main_window", u"Clear", None))
        self.data_textEdit.setPlaceholderText(QCoreApplication.translate("main_window", u"Received data will appear here\u2026", None))
        self.connectionGroup.setTitle(QCoreApplication.translate("main_window", u"Connection", None))
        self.refresh_button.setText(QCoreApplication.translate("main_window", u"\u27f3  Scan ports", None))
        self.label_22.setText(QCoreApplication.translate("main_window", u"Port", None))
        self.label_25.setText(QCoreApplication.translate("main_window", u"Baud", None))
        self.label_26.setText(QCoreApplication.translate("main_window", u"Data", None))
        self.label_28.setText(QCoreApplication.translate("main_window", u"Parity", None))
        self.label_29.setText(QCoreApplication.translate("main_window", u"Stop", None))
        self.label_30.setText(QCoreApplication.translate("main_window", u"Flow", None))
        self.label_27.setText(QCoreApplication.translate("main_window", u"Timeout", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Line end", None))
        self.start_button.setText(QCoreApplication.translate("main_window", u"CONNECT", None))
        self.statusDot.setText("")
        self.status_label.setText(QCoreApplication.translate("main_window", u"Not connected", None))
        self.infoGroup.setTitle(QCoreApplication.translate("main_window", u"Device", None))
        self.options_textEdit.setPlaceholderText(QCoreApplication.translate("main_window", u"Connect to a device to see its details.", None))
        self.send_data_text.setPlaceholderText(QCoreApplication.translate("main_window", u"Type data to send and press Enter\u2026", None))
#if QT_CONFIG(tooltip)
        self.indicate_button.setToolTip(QCoreApplication.translate("main_window", u"Indicates that data is being transmitted", None))
#endif // QT_CONFIG(tooltip)
        self.indicate_button.setText("")
        self.send_button.setText(QCoreApplication.translate("main_window", u"Send", None))
#if QT_CONFIG(shortcut)
        self.send_button.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.donateButton.setText(QCoreApplication.translate("main_window", u"\u2615  Support", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("main_window", u"Edit", None))
        self.menuSetup.setTitle(QCoreApplication.translate("main_window", u"Settings", None))
        self.menuControl.setTitle(QCoreApplication.translate("main_window", u"Connection", None))
        self.menuWindow.setTitle(QCoreApplication.translate("main_window", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", u"Help", None))
    # retranslateUi

