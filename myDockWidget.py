import sys
import copy
from PyQt4 import QtCore, QtGui
import datetime

class mySpecialDockWidget(QtGui.QDockWidget):
    '''
	This is the place holder dock that keeps a space open for us to drag a dock onto. 
	It is only present when there are no docks on the gui.
	'''
    sigDockDropped = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(mySpecialDockWidget, self).__init__(parent=parent)
        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)   
        self.txtLbl = QtGui.QLabel('drag type/channel \nfrom tree to here\n for more detailed view')
        self.txtLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.txtLbl)
        self.widget = QtGui.QWidget()
        self.widget.setLayout(self.layout)
        self.widget.setContentsMargins(-10,-10,0,0)
        self.widget.setMinimumWidth(250)
        self.setAcceptDrops(True)
        self.setWidget(self.widget)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, e):
        e.accept()
        self.sigDockDropped.emit()

class myDockWidget(QtGui.QDockWidget):
	'''
	This is the 'detailed type desription.'  When a type label from the tree widget is draged 
	into the type widget or onto another dock widget, we add a new dock associated with that type.

	Each dock displays the most recent message (at the time of the update.)  
	'''

	#sigNewDroppedDock = QtCore.pyqtSignal( 'QString', 'QString',object,object)
	sigDockDropped = QtCore.pyqtSignal()
	sigDockTracker = QtCore.pyqtSignal('QString', bool)
	sigFloatTracker = QtCore.pyqtSignal('QString', bool)

	def __init__(self, disChan, disType, statThread, timer, parent=None):
		super(myDockWidget, self).__init__(parent=parent)
		self.horizonBox     = dict()
		self.attributeLbl   = dict()
		self.statThread     = statThread
		self.timer   = timer
		self.disChan        = disChan
		self.disType        = disType

		self.visibilityChanged.connect(self.dockTracker)
		self.topLevelChanged.connect(self.floatTracker)
		self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
		self.setAcceptDrops(True)
		self.setWindowTitle("Type: %s    Channel: %s" % (disType, disChan, ) )
		self.setupWidget()

	def dockTracker(self, visibility):
		'''lets us know when we add or remove new dock'''
		self.sigDockTracker.emit(str(self.disChan), visibility)

	def floatTracker(self, floating):
		'''This keeps track of docks that are free floating. Defines behavior for floating/not floating '''
		if floating:
			self.refactorTable()     
			self.setAcceptDrops(False)
			self.sigFloatTracker.emit(str(self.disChan), floating)
		else:
			self.setAcceptDrops(True)
			self.sigFloatTracker.emit(str(self.disChan), floating)

	def setupWidget(self):
		self.checkBox           = dict()    
		self.horizonBox         = dict()
		self.dataLbl            = dict()
		self.attLbl             = dict()
		self.timer.timeout.connect(self.update)
		self.tableView      = QtGui.QTableWidget()
		self.tableView.setColumnCount(2)
		self.tableView.verticalHeader().hide()
		self.tableView.horizontalHeader().setStretchLastSection(True)   
		self.tableView.horizontalHeader().setClickable(True)
		self.tableView.setHorizontalHeaderLabels(['attribute', 'value'])  
		self.lblFreq        = QtGui.QTableWidgetItem('frequency')
		self.freq           = QtGui.QTableWidgetItem("0 Hz")
		self.tableView.insertRow(0)
		self.tableView.setItem(0,0, self.lblFreq)
		self.tableView.setItem(0,1, self.freq)
        
		#accounts for when the channel was undecodable
		if self.disType == "unknown":
			self.addRow( "count" )
		else: 
			self.addRow( "count" )
			for att in reversed(self.statThread.attDict[self.disType]): 
				self.addRow(att)

		self.refactorTable()
		self.setWidget(self.tableView)

	def dragEnterEvent(self, event):
			event.accept()

	def dropEvent(self, e):
		e.accept()
		self.sigDockDropped.emit()

	def refactorTable(self):
		'''trying to get the sizing correct. '''
		self.tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
		self.tableView.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

		rect = self.tableView.geometry()
		tableWidth = 2 + self.tableView.verticalHeader().width()
		for x in range(0, self.tableView.columnCount() ):
			tableWidth += self.tableView.columnWidth(x)
		rect.setWidth(tableWidth)

		tableHeight = 2 + self.tableView.horizontalHeader().height()
		for x in range(0, self.tableView.rowCount() ):
			tableHeight += self.tableView.rowHeight(x) 
		rect.setHeight(tableHeight)

		self.tableView.setGeometry(rect)
    


	def update(self):
		'''updates the type widget when it receives a cue from from Qtimer'''
		elapsedTime = (self.getTime() - self.statThread.dataDict[self.disChan].startTime) / 1000000
		frequency = round(elapsedTime / self.statThread.dataDict[self.disChan].count , 3)
		self.freq.setText("%s Hz" % frequency)
		if self.disType == "unknown":
			dataC = self.statThread.dataDict[self.disChan].count
			dataF = self.statThread.dataDict[self.disChan].frequency
			self.dataLbl["count"].setText(str(dataC))
		else:
			for att in self.statThread.attDict[self.disType]:
				if att == "startTime":
					data = self.statThread.dataDict[self.disChan].startTime
				else:
					exec('data = self.statThread.dataDict[self.disChan].%s[-1]' %att)
				if att == 'utime' or att == 'timestamp':
					self.dataLbl[str(att)].setText(str(data))
				else:
					#print type(data)
					if type(data) == unicode:#data is a string- output the whole thing
						self.dataLbl[str(att)].setText(data)
					elif type(data) == tuple and len(data) < 25:                    
						self.dataLbl[str(att)].setText(str(data))
					elif len(str(data)) < 10:
						self.dataLbl[str(att)].setText(str(data))
					else:
						output = str(data)[0:11] + '...'
						self.dataLbl[str(att)].setText(output)
			dataC = self.statThread.dataDict[self.disChan].count
			self.dataLbl["count"].setText(str(dataC))

	def getTime(self):
		'''Formats the time for the display'''
		now = datetime.datetime.now()
		timestamp = now.microsecond
		timestamp = timestamp + now.second * 1000000
		timestamp = timestamp + now.minute * 1000000 * 60
		timestamp = timestamp + now.hour   * 1000000 * 60 * 60  
		timestamp = float(timestamp) 
		return timestamp

	def addRow(self, att):
		att = str(att)
		self.attLbl[att] = QtGui.QTableWidgetItem()
		self.dataLbl[att] = QtGui.QTableWidgetItem()

		self.tableView.insertRow(0)
		self.attLbl[att].setText(str(att))
		self.dataLbl[att].setText( "0" )

		self.tableView.setItem(0,0, self.attLbl[att])
		self.tableView.setItem(0,1, self.dataLbl[att])

