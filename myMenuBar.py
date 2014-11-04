from PyQt4 import QtCore, QtGui

class myMenuBar(QtGui.QMenuBar):
    def __init__(self):
        super(myMenuBar, self).__init__() 
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.setupMenuFile()
        self.setupMenuTools()

    def setupMenuFile(self):
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.exit = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip('Exit application')
        self.exit.setObjectName("exit")
        self.exit.setText("exit")

	self.reset = QtGui.QAction('&Reset', self)
        self.reset.setStatusTip('reset lcm')
        self.reset.setObjectName("reset")
        self.reset.setText("reset")


        self.pause = QtGui.QAction(self)
        self.pause.setShortcut('Ctrl+B')
        self.pause.setStatusTip('Pause application')
        self.pause.setObjectName("pause")
        self.pause.setText("pause")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit)
        self.menuFile.addAction(self.reset)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))

    def setupMenuTools(self): 
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("Tools")
        self.menuTools.addSeparator()
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menubar.addAction(self.menuTools.menuAction()) 
        
        self.importMod = QtGui.QAction(self)
        self.importMod.setObjectName("import module")
        self.importMod.setStatusTip('import another lcmType module')
        self.importMod.setText("import module")

        self.plotBucket = QtGui.QAction(self)
        self.plotBucket.setObjectName("plotBucket")
        self.plotBucket.setText("plot Bucket")
        self.menuTools.addAction(self.plotBucket)
        self.menuTools.addAction(self.importMod)

