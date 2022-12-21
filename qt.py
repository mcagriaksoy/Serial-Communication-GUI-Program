__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'

import sys, os, serial, serial.tools.list_ports, warnings
from PyQt5.QtCore import *
import time
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

#GUI interactions
import winsound

# MULTI-THREADING

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(str)

    @pyqtSlot()
    def __init__(self):
        super(Worker, self).__init__()
        self.working = True

    def work(self):
        while self.working:
            if ser.isOpen():
                line = ser.readline().decode('utf-8')
            else:
                line = ''

            if line != '':
                print(line)
                time.sleep(0.1)
                self.intReady.emit(line)

        self.finished.emit()

class qt(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        loadUi('qt.ui', self)

        self.thread = None
        self.worker = None
        self.pushButton.clicked.connect(self.start_loop)
        self.pushBtnClicked = False
        self.CopyFlag = 0

    def loop_finished(self):
        print('Loop Finished')

    def start_loop(self):
        #Verify the correct COM Port
        try:
            mytext = "\n"  # Send first enter
            global ser
            ser = serial.Serial(self.cb_Port.currentText(), 115200, timeout=1)  # (ports[0], 115200)    #('COM1', 115200, timeout=1)
            ser.write(mytext.encode())
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("COM Port Error!")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Selected COM port does not exist. Please verify the COM port Number.")
            msgBox.exec()
            self.label_5.setText("Not Connected")
            self.label_5.setStyleSheet('color: red')
            return

        self.worker = Worker()   # a new worker to perform those tasks
        self.thread = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(self.thread)  # move the worker into the thread, do this first before connecting the signals

        self.thread.started.connect(self.worker.work) # begin our worker object's loop when the thread starts running

        self.worker.intReady.connect(self.onIntReady)

        self.pushButton_2.clicked.connect(self.stop_loop)      # stop the loop on the stop button click

        self.worker.finished.connect(self.loop_finished)       # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)         # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        self.thread.start()

    def stop_loop(self):
        self.worker.working = False
        self.label_5.setText("Not Connected")
        self.label_5.setStyleSheet('color: red')
        ser.close()

    def onIntReady(self, i):
        if i != '':
            self.textEdit_3.append("{}".format(i))
            print(i)
            if i.find('CINE Frames') != -1:
                #IQ file stored make beep
                winsound.Beep(1740, 800)

            if self.ck_AuSC.isChecked():
                #Auto Copy files
                if i.find('io copy j:') != -1:
                    #First autocopy condition
                    self.CopyFlag = 1

                if i.find('nvdbg>') != -1 and self.CopyFlag == 1:
                    count = self.sb_Num.value()
                    if count < 10:
                        numb = '0' + str(count)
                    else:
                        numb = str(count)

                    mytext = "io copy j:" + self.txtIQfile.toPlainText() + numb + ".iq " + self.cb_Drive.currentText() + "\n"
                    ser.write(mytext.encode())

                    #Check for final file copy
                    if count == self.sb_NumFin.value():
                        self.ck_AuSC.setCheckState(False)
                        self.sb_NumFin.setEnabled(False)
                        self.CopyFlag = 0
                        mytext = "\n"       #Clear buffer
                        ser.write(mytext.encode())
                    else:
                        self.sb_Num.setValue(count + 1)


    # TXT Save
    def on_pushButton_5_clicked(self):
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return

        fileName = QFileDialog.getSaveFileName(self, 'Select location to Log', "", '*.txt')
        if not fileName:
            return

        with open(fileName[0], 'w') as f:
            my_text = self.textEdit_3.toPlainText()
            f.write(my_text)

        self.textEdit_3.append("Log Saved in :" + fileName[0] + "\r\n")
        self.pushBtnClicked = True

    def on_pushButton_2_clicked(self):
        self.textEdit.setText('Stopped! Please click CONNECT...')

    def on_pb_Clr_clicked(self):
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return

        #Clear serial screen
        self.textEdit_3.setText('')
        mytext = "\n"  # Clear buffer
        ser.write(mytext.encode())

        self.pushBtnClicked = True

    def on_pushButton_clicked(self):
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return

        # Port Detection START
        ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'USB' in p.description
        ]

        if not ports:
            ports = ['NONE']

        self.label_11.setText(ports[0])
        # Port Detection END

        if ports[0] != 'NONE':
            #Start the progress bar
            self.completed = 0
            while self.completed < 100:
                self.completed += 0.001
                self.progressBar.setValue(self.completed)
            self.textEdit.setText('Data Gathering...')
            self.label_5.setText("CONNECTED!")
            self.label_5.setStyleSheet('color: green')
            x = 1
            self.textEdit_3.setText(":")

        self.pushBtnClicked = True


    def on_pushButton_3_clicked(self):
        # Send data from serial port:
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return
        mytext = self.textEdit_2.toPlainText() + "\n"
        print(mytext.encode())
        ser.write(mytext.encode())
        self.pushBtnClicked = True

    def on_pb_Free_clicked(self):
        # Send Freeze command from serial port:
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return
        mytext = "cine freeze\n"
        print(mytext.encode())
        ser.write(mytext.encode())
        self.pushBtnClicked = True

    def on_ck_AuSC_clicked(self):
        # Auto Store/Copy active
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return

        if self.ck_AuSC.isChecked():
            self.sb_NumFin.setEnabled(True)
        else:
            self.sb_NumFin.setEnabled(False)

        self.pushBtnClicked = True

    def on_pb_Unfre_clicked(self):
        # Send Unfreeze command from serial port:
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return
        mytext = "cine unfreeze\n"
        print(mytext.encode())
        ser.write(mytext.encode())
        self.pushBtnClicked = True

    def on_pb_List_clicked(self):
        # Send List dir command from serial port:
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return
        mytext = "io dir " + self.cb_Drive.currentText() + "\n"
        print(mytext.encode())
        ser.write(mytext.encode())
        self.pushBtnClicked = True

    def on_pb_Brow_clicked(self):
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return
        # select folder with files to rename
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if not folder:
            return

        self.txt_Dir.setText(folder)
        self.pushBtnClicked = True
        winsound.Beep(1740, 800)

    def on_pb_Rena_clicked(self):
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return

        if self.txtIQfile.toPlainText() == "" or self.txt_Dir.toPlainText() == "":
            msgBox = QMessageBox()
            msgBox.setWindowTitle("No IQ File Name!")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("There is not an IQ File Name or Directory. Please specify the File Name and Directory first.")
            msgBox.exec()
            self.pushBtnClicked = True
            return

        # go across files and rename those
        folder = self.txt_Dir.toPlainText()
        for count, filename in enumerate(os.listdir(folder)):
            if count < 10:
                numb = '0' + str(count)
            else:
                numb = str(count)

            dst = self.txtIQfile.toPlainText() + numb + ".mov"
            src = folder + '/' + filename
            dst = folder + '/' + dst

            os.rename(src, dst)

        self.pushBtnClicked = True

    def on_pb_StCo_clicked(self):
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return

        if self.txtIQfile.toPlainText() == "":
            msgBox = QMessageBox()
            msgBox.setWindowTitle("No IQ File Name!")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("There is not an IQ File Name. Please specify the File Name first.")
            msgBox.exec()
            self.pushBtnClicked = True
            return

        # Check if auto-increment index
        if self.ck_Auto.isChecked():
            count = self.sb_Num.value()
            if count < 10:
                numb = '0' + str(count)
            else:
                numb = str(count)

            #check for store command
            if self.ch_Store.isChecked():
                mytext = "cine store j:" + self.txtIQfile.toPlainText() + numb + ".iq 2363 2442 2 1\n"
                ser.write(mytext.encode())

            # check for copy command
            if self.ch_Copy.isChecked():
                mytext = "io copy j:" + self.txtIQfile.toPlainText() + numb + ".iq " + self.cb_Drive.currentText() + "\n"
                ser.write(mytext.encode())

            self.sb_Num.setValue(count+1)

        else:
            # check for store command
            if self.ch_Store.isChecked():
                mytext = "cine store j:" + self.txtIQfile.toPlainText() + ".iq 2363 2442 2 1\n"
                ser.write(mytext.encode())

            # check for copy command
            if self.ch_Copy.isChecked():
                mytext = "io copy j:" + self.txtIQfile.toPlainText() + ".iq " + self.cb_Drive.currentText() + "\n"
                ser.write(mytext.encode())

        self.pushBtnClicked = True

def run():
    app = QApplication(sys.argv)
    widget = qt()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()