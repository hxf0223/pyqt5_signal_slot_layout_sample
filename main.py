#!/usr/bin/python3

'''
Signal-Slot sample
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QLCDNumber, QSlider, QGridLayout, QLabel, \
    QHBoxLayout, QVBoxLayout, QProgressBar, QPushButton, QMessageBox


class SignalSlotSample(QWidget):
    def __init__(self):
        super(SignalSlotSample, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.init_grp_box()
        self.init_layout()

        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.grpBox)
        self.hlayout.addLayout(self.ctrl_layout)
        self.setLayout(self.hlayout)

    def init_grp_box(self):
        self.grpBox = QGroupBox(self)
        self.lcdNumber = QLCDNumber(self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.pbar = QProgressBar(self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.pbar)
        self.vbox.addWidget(self.lcdNumber)
        self.vbox.addWidget(self.slider)
        self.grpBox.setLayout(self.vbox)

        self.setGeometry(600, 500, 500, 180)
        self.setWindowTitle("Signal & Slot")
        self.slider.valueChanged.connect(self.pbar.setValue)
        self.slider.valueChanged.connect(self.lcdNumber.display)

    def init_layout(self):
        self.ctrl_layout = QGridLayout()
        self.label1 = QLabel("Saved status:")
        self.lblSaved = QLabel()
        self.label2 = QLabel("Run Status:")
        self.lblRunStt = QLabel()
        self.btnSave = QPushButton("Save")
        self.btnRun = QPushButton("Run")
        self.btnStop = QPushButton("Stop")
        self.btnBind = QPushButton("Bind")
        self.btnUnbind = QPushButton("Unbind")

        self.ctrl_layout.addWidget(self.label1, 0, 0)
        self.ctrl_layout.addWidget(self.lblSaved, 0, 1)
        self.ctrl_layout.addWidget(self.label2, 1, 0)
        self.ctrl_layout.addWidget(self.lblRunStt, 1, 1)
        self.ctrl_layout.addWidget(self.btnSave, 2, 0)
        self.ctrl_layout.addWidget(self.btnRun, 2, 1)
        self.ctrl_layout.addWidget(self.btnStop, 2, 2)
        self.ctrl_layout.addWidget(self.btnBind, 3, 0)
        self.ctrl_layout.addWidget(self.btnUnbind, 3, 1)

        self.btnRun.clicked.connect(self.update_display_run)
        self.btnSave.clicked.connect(self.update_display_save)
        self.btnStop.clicked.connect(self.update_display_stop)

    def update_display_run(self):
        self.lblSaved.setText("Saved")
        self.lblRunStt.setText("Running")

    def update_display_save(self):
        self.lblSaved.setText("Saved")

    def update_display_stop(self):
        self.lblSaved.setText("")
        self.lblRunStt.setText("")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sss_ins = SignalSlotSample()
    sss_ins.show()

    sys.exit(app.exec_())