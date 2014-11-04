import sys, inspect, os, time
import lcm
from PyQt4 import QtCore, QtGui
import time
import sip

class modulePopup(QtGui.QWidget):
    sigMods = QtCore.pyqtSignal(object)
    def __init__(self, module):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Module Importer')
        self.errLayout = QtGui.QVBoxLayout() 
        if module: 
            self.errorLbl2 = QtGui.QLabel("Unable to import module %s\n Did you set up your PYTHONPATH? \nPlease refer to the setup instructions in README.txt \n"%module)
            self.errLayout.addWidget(self.errorLbl2)

        self.errorLbl1 = QtGui.QLabel("Please enter the name of a folder where\n we can find the lcm type definitions.\
                        \n\nDelimit multiple entries by a comma ','")
        self.errLayout.addWidget(self.errorLbl1)

        self.lineEdit = QtGui.QLineEdit()
        self.enterBtn = QtGui.QPushButton("Enter")
        self.enterBtn.setAutoDefault(True)
        self.enterBtn.clicked.connect(self.process)
        self.hbox = QtGui.QHBoxLayout() 
        self.hbox.addWidget(self.lineEdit)
        self.hbox.addWidget(self.enterBtn)

        self.errLayout.addLayout(self.hbox)
        self.setLayout(self.errLayout)


    def refactorSize(self):
        size = self.sizeHint()
        self.setGeometry(275,175, size.width(), size.height())

    def process(self):
        #processes the modules on button click. 
        #TODO -- This is not graceful at all- actually, a little embarrassing-- How do make this more pythonic?
        modString = str(self.lineEdit.text())
        finList = []
        modList = modString.split(',')
        for each in modList:
            finList.append(each.strip())
        self.sigMods.emit(finList)
        self.close()

    def close(self):
        self.deleteLater()
        self = None
