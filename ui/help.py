# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        if not HelpDialog.objectName():
            HelpDialog.setObjectName(u"HelpDialog")
        HelpDialog.resize(720, 480)
        HelpDialog.setMinimumSize(QSize(560, 400))
        self.rootLayout = QVBoxLayout(HelpDialog)
        self.rootLayout.setSpacing(12)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(18, 18, 18, 18)
        self.helpTitleLabel = QLabel(HelpDialog)
        self.helpTitleLabel.setObjectName(u"helpTitleLabel")

        self.rootLayout.addWidget(self.helpTitleLabel)

        self.helpTextEdit = QTextEdit(HelpDialog)
        self.helpTextEdit.setObjectName(u"helpTextEdit")
        self.helpTextEdit.setReadOnly(True)
        self.helpTextEdit.setFrameShape(QFrame.Shape.NoFrame)

        self.rootLayout.addWidget(self.helpTextEdit)

        self.helpFooterLabel = QLabel(HelpDialog)
        self.helpFooterLabel.setObjectName(u"helpFooterLabel")

        self.rootLayout.addWidget(self.helpFooterLabel)


        self.retranslateUi(HelpDialog)

        QMetaObject.connectSlotsByName(HelpDialog)
    # setupUi

    def retranslateUi(self, HelpDialog):
        HelpDialog.setWindowTitle(QCoreApplication.translate("HelpDialog", u"Help", None))
        self.helpTitleLabel.setText(QCoreApplication.translate("HelpDialog", u"AFCOM Client", None))
        self.helpFooterLabel.setText(QCoreApplication.translate("HelpDialog", u"AFCOM Client \u00b7 GPLv3 \u00b7 github.com/mcagriaksoy", None))
    # retranslateUi

