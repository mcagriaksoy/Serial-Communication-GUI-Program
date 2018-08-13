__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import pyqtSlot, QSize, QRect 
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QMainWindow, QWidget, QLabel, QTextEdit, QListWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
import sys, time, threading
from random import randint
import serial


class qt(QMainWindow):	

	def __init__(self):
		
		QMainWindow.__init__(self)
		loadUi('qt.ui',self)
		self.setWindowTitle('Seri Haberlesme TEST')
		self.pushButton.clicked.connect(self.on_pushButton_clicked)
		self.x=0
		while self.x<5:
			self.listWidget.addItem('deneme')
			self.x=self.x+1

	#def on_Cbox_activated(self):
		

	def on_pushButton_clicked(self):
		self.completed = 0
		while self.completed < 100 :
			self.completed += 0.001
			self.progressBar.setValue(self.completed)
		self.textEdit.setText('Veri Aliniyor...')
		self.label_5.setText(self.combo.currentText())
		#self.label_5.setText('OK!')
		self.label_5.setStyleSheet('color: green')

		
	

	def on_pushButton_2_clicked(self):
		self.textEdit.setText('Durduruldu! Yeniden Baglanmak icin BAGLAN-a basin...')

				
		
		
		


def main():
	app=QApplication(sys.argv)
	widget=qt()
	widget.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
    main()




