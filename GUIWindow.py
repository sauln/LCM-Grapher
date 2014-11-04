import os
import sys
import copy
from PyQt4 import QtCore, QtGui
import datetime  

import plotDisplay
reload(plotDisplay)
import myMenuBar 
reload(myMenuBar)
from myDockWidget import myDockWidget
from myDockWidget import mySpecialDockWidget
from myTreeWidget import myTreeWidget
from plotBucket import plotBucket

class mainWindow(QtGui.QMainWindow):
	sigResetLCM = QtCore.pyqtSignal()
	sigOpenImporter = QtCore.pyqtSignal()

	def __init__(self, lcmThread, statThread, timer, parent=None):
		super(mainWindow, self).__init__() 
		self.setWindowTitle('LCM Plotting Utility')
		self.statThread             = statThread
		self.timer					= timer
		#self.updateThread           = updateThread
		self.lcmThread              = lcmThread
		self.setup() 
		self.docks = dict() 
 		self.statusBar().showMessage('Ready') 

	def setup(self):
		'''inital setup'''
		self.ui                     = QtGui.QMainWindow()   
		self.ui.centralLayout       = QtGui.QHBoxLayout() 
		self.ui.centralWidget       = QtGui.QWidget()
		self.spacerItem             = QtGui.QSpacerItem( 5,5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
		self.setGeometry(0,0,650,350) 
		self.setupMenu()
		self.setupTree() 
		self.setupTypeDock()
		self.setupPlotBucket()

		self.tree.sigPlotBtnClicked.connect(self.plotBucket.plotNet)
		self.tree.treeWidget.itemPressed.connect(self.updateOnDeck)
		self.ui.centralWidget.setLayout(self.ui.centralLayout) 
		self.setCentralWidget(self.ui.centralWidget)  
	
	def setupMenu(self):
		'''initial setup of the top menu bar'''
		self.menubar = myMenuBar.myMenuBar()
		#self.menubar.pause.triggered.connect(self.pauseThreads)
		self.menubar.exit.triggered.connect(self.quit)
		self.menubar.reset.triggered.connect(self.reset)
		self.menubar.plotBucket.triggered.connect(self.openPlotBucketGUI)
		self.menubar.importMod.triggered.connect(self.modPopup)
		self.setMenuBar(self.menubar.menubar)


	def setupTree(self):
		'''initial setup of the channel and attribute tree'''
		self.tree = myTreeWidget(self.statThread)
		self.ui.centralLayout.addWidget(self.tree)


	def setupTypeDock(self): 
		'''initial setup of the dock for data display'''   
		self.specialDock = mySpecialDockWidget()
		self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.specialDock)
		self.specialDock.sigDockDropped.connect(self.newDock)


	def setupPlotBucket(self): 
		'''initial setup of the plot bucket''' 
		self.plotBucket = plotBucket(self.statThread, self.timer)
		self.plotBucket.sigStatusUpdate.connect(self.statusUpdate)



	def openPlotBucketGUI(self):
		'''Opens the plot bucket window'''
		size = self.geometry()
		self.plotBucket.openGUI(size)

	def statusUpdate(self, message):
		'''Updates the status bar on the bottom with the new message '''
		self.statusBar().showMessage(message) 

	def modPopup(self):
		'''Now sends a signal to _______ to tell it to open the module importer'''
		self.sigOpenImporter.emit()
		#self.lcmThread.openImporter()
		#self.lcmThread.errorWindow.show()

	def updateOnDeck(self, item):
		'''when a type/channel(treeWidget parent) is clicked, 
		we remember it in case it is dragged to the dock widget'''
		self.typeOnDeck = item.text(0)

	def newDock(self):
		'''add a new dock only if this particular dock doesn't already exist'''
		disChan, disType =  str(self.typeOnDeck).split('/')
		self.newestDock = disChan
		if not disChan in self.docks.keys():
			self.docks[disChan] = myDockWidget(disChan, disType, \
				self.statThread, self.timer)

		#TODO I think some of these signals are deprecated
			self.docks[disChan].sigDockDropped.connect(self.newDock)
			self.docks[disChan].sigDockTracker.connect(self.refactorDisplay)
			self.docks[disChan].sigFloatTracker.connect(self.refactorDisplay)
			self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.docks[disChan])
		else:
			self.docks[disChan].show()

	def refactorDisplay(self):
		'''When there are no open typeDocks we will show the special spacer dock'''
		count = 0
		for each in self.docks.values():
			if each.isVisible() and not each.isFloating():
				count = count + 1               
			if count == 0:
				self.specialDock.show()
			else:
				self.specialDock.hide()

	def closeEvent(self, event):
		self.quit()

	def reset(self):
		self.sigResetLCM.emit()

	def quit(self):
		self.lcmThread.running = False
		self.statThread.running = False
		os._exit(1) 
		return True

