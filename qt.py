import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi


class qt(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		loadUi('qt.ui',self)
		self.setWindowTitle('Seri Haberlesme TEST')
		self.pushButton.clicked.connect(self.on_pushButton_clicked)
	
	def on_pushButton_clicked(self):
		self.label.setText('Basarili :' +self.lineEdit.text())

def main():
	app=QApplication(sys.argv)
	widget=qt()
	widget.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
    main()
