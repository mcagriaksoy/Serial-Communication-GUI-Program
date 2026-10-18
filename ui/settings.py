# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFontComboBox, QFormLayout,
    QGroupBox, QLabel, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 330)
        Dialog.setMinimumSize(QSize(460, 300))
        self.rootLayout = QVBoxLayout(Dialog)
        self.rootLayout.setSpacing(14)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(18, 18, 18, 18)
        self.appearanceGroup = QGroupBox(Dialog)
        self.appearanceGroup.setObjectName(u"appearanceGroup")
        self.formLayout = QFormLayout(self.appearanceGroup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(10)
        self.themeLabel = QLabel(self.appearanceGroup)
        self.themeLabel.setObjectName(u"themeLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.themeLabel)

        self.themeComboBox = QComboBox(self.appearanceGroup)
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.themeComboBox.setObjectName(u"themeComboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.themeComboBox)

        self.languageLabel = QLabel(self.appearanceGroup)
        self.languageLabel.setObjectName(u"languageLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.languageLabel)

        self.languageComboBox = QComboBox(self.appearanceGroup)
        self.languageComboBox.addItem("")
        self.languageComboBox.addItem("")
        self.languageComboBox.setObjectName(u"languageComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.languageComboBox)

        self.fontLabel = QLabel(self.appearanceGroup)
        self.fontLabel.setObjectName(u"fontLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.fontLabel)

        self.fontComboBox = QFontComboBox(self.appearanceGroup)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.fontComboBox)

        self.fontSizeLabel = QLabel(self.appearanceGroup)
        self.fontSizeLabel.setObjectName(u"fontSizeLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.fontSizeLabel)

        self.fontSize_spinBox = QSpinBox(self.appearanceGroup)
        self.fontSize_spinBox.setObjectName(u"fontSize_spinBox")
        self.fontSize_spinBox.setMinimum(6)
        self.fontSize_spinBox.setMaximum(48)
        self.fontSize_spinBox.setValue(11)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.fontSize_spinBox)

        self.timestampsLabel = QLabel(self.appearanceGroup)
        self.timestampsLabel.setObjectName(u"timestampsLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.timestampsLabel)

        self.timestampsCheckBox = QCheckBox(self.appearanceGroup)
        self.timestampsCheckBox.setObjectName(u"timestampsCheckBox")
        self.timestampsCheckBox.setChecked(False)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.timestampsCheckBox)


        self.rootLayout.addWidget(self.appearanceGroup)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rootLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.rootLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Preferences", None))
        self.appearanceGroup.setTitle(QCoreApplication.translate("Dialog", u"Appearance", None))
        self.themeLabel.setText(QCoreApplication.translate("Dialog", u"Theme", None))
        self.themeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"System default", None))
        self.themeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Dark", None))
        self.themeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Light", None))

        self.languageLabel.setText(QCoreApplication.translate("Dialog", u"Language", None))
        self.languageComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"English", None))
        self.languageComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"T\u00fcrk\u00e7e", None))

        self.fontLabel.setText(QCoreApplication.translate("Dialog", u"Terminal font", None))
        self.fontSizeLabel.setText(QCoreApplication.translate("Dialog", u"Font size", None))
        self.timestampsLabel.setText(QCoreApplication.translate("Dialog", u"Logging", None))
        self.timestampsCheckBox.setText(QCoreApplication.translate("Dialog", u"Timestamp received lines", None))
    # retranslateUi

