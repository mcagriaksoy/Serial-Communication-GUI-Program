__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'

import sys, serial, threading, time
from PyQt5.QtCore import QSize, QRect, QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QMainWindow, QWidget, QLabel, QTextEdit, QListWidget, \
    QListView
from PyQt5.uic import loadUi

ser = serial.Serial('/dev/ttyUSB0', 9600)

end = False


class Foo(QThread):

    def connect(self):
        connect(pushButton_2, SIGNAL("clicked()"), on_pushButton_2_clicked)


# MULTI-THREADING
class Worker(QObject):
    log = pyqtSignal(str)
    finished = pyqtSignal(str)

    def __init__(self):
        super(Worker, self).__init__()
        self.working = True
    def work(self):

        while self.working:

            line = ser.readline().decode('utf-8')
            print(line)
            self.log.emit(self.line)
            #if line != '':
            #    self.textEdit_3.append(line)
            time.sleep(1)
        #self.finished.emit()


class qt(QMainWindow):

    def __init__(self):

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        QMainWindow.__init__(self)
        loadUi('qt.ui', self)
        self.comboBox_0.activated.connect(self.load_value0)
        self.comboBox_1.activated.connect(self.load_value1)
        self.x = 0


        self.thread = None
        self.worker = None
        self.pushButton.clicked.connect(self.start_loop)


    def loop_finished(self):
        print('Looped Finished')

    def start_loop(self, textEdit_4=None):
        global line
        self.thread = QThread()
        self.thread.start()
        self.thread.log.connect(self.aa)
        self.but1.setEnabled(False)

        self.thread = QThread()  # a new thread to run our background tasks in
        self.worker = Worker()  # a new worker to perform those tasks
        self.worker.moveToThread(
            self.thread)  # move the worker into the thread, do this first before connecting the signals

        self.thread.started.connect(self.worker.work)  # begin our worker object's loop when the thread starts running
        self.pushButton_2.clicked.connect(self.stop_loop)  # stop the loop on the stop button click
        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)  # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        # make sure those last two are connected to themselves or you will get random crashes

        self.thread.start()

    def aa(self):
        self.textEdit_3.append(line)

    def stop_loop(self):
        self.worker.working = False

    def load_value0(self, index0):
        # portadi
        self.a2 = self.comboBox_0.itemText(index0)
        print(self.comboBox_0.itemText(index0))
        self.x = 2

    def load_value1(self, index1):
        # baudrate
        b2 = self.comboBox_1.itemText(index1)

        print(self.comboBox_1.itemText(index1))
        self.x = 1

    def on_pushButton_4_clicked(self):
        if self.x is not 0:
            def create_serial_obj(a2, b2):

                return serial.Serial(a2, b2)

            print('basarili')
        else:
            print('hata')
            self.textEdit.setText('Lütfen Port ve Hızı girin!')

    def on_pushButton_2_clicked(self):
        self.textEdit.setText('Durduruldu! Yeniden Baglanmak icin BAGLAN-a basin...')

    def on_pushButton_clicked(self):
        # if self.x==0 :
        # ser.open()
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.001
            self.progressBar.setValue(self.completed)
        self.textEdit.setText('Veri Aliniyor...')
        # self.label_5.setText('OK!')
        self.label_5.setStyleSheet('color: green')
        x = 1
        self.textEdit_3.setText(":")




    # exception code here
    # self.listWidget.insertItems(ser.readline())

    def on_pushButton_3_clicked(self):

        mytext = self.textEdit_2.toPlainText()
        ser.write(mytext.encode())

    # def on_pushButton_2_clicked(self):

    # ser.close()
    #   self.textEdit.setText('Durduruldu! Yeniden Baglanmak icin BAGLAN-a basin...')


def run():
    app = QApplication(sys.argv)
    widget = qt()
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
