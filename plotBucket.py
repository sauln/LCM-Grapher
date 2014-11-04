"""
This file contains the plotStruct and the plotBucket

The plotStruct is the container and respective functionality that correlates the plot and the tab within the plotBucket

PlotBucket is a container for all of the plotStructs.  It creates and destroys plots when needed. It is the interface for incoming plot commands


"""






"""

There is a lot of infrastructure built up to deal with vectors,
this must be fixed.

instead of plotting all items of a vector, we will plot just the item that is 



to do this, we need to 


"""










"""
signals:

plotStruct:
		sigCloseAll

plotBucket:
		sigStatusUpdate




"""











#TODO:  For some reason, when a new tab is created, it doesnt overwrite the previous tab.  while removing vector components from the plots


#Advanced plotting option window
import sys, inspect, os, time
import lcm
from PyQt4 import QtCore, QtGui
import time
import sip
import plotDisplay 

from collections import defaultdict


class plotTab(QtCore.QObject):
	def __init__(self, tagInfo, vectors, itemList):
		super(plotTab, self).__init__()

		"""Build the tab in the plotbucket for each individual plot"""
		tagDict, tag            = self.getTagList(itemList) 
		self.reshowBtn          = QtGui.QPushButton("Show Plot")
		self.plotExportBtn      = QtGui.QPushButton("Export Plot")
		self.applyAxisBtn    	= QtGui.QPushButton("Apply")
		self.applyRemoveBtn		= QtGui.QPushButton("Apply")
		self.closePlotBtn       = QtGui.QPushButton("Delete Plot") 
		self.axisCombo          = QtGui.QComboBox()
		self.removeCombo		= QtGui.QComboBox()
		formLayout              = QtGui.QFormLayout()   
		groupBox                = QtGui.QGroupBox("Plot Details")
		plotWidget              = QtGui.QWidget()
		axisChoiceLbl           = QtGui.QLabel("Choose x axis")
		removeLbl				= QtGui.QLabel("Remove")
		axisBox                 = QtGui.QHBoxLayout()
		btnHBox                 = QtGui.QHBoxLayout()
		layout                  = QtGui.QVBoxLayout()
		removeBox				= QtGui.QHBoxLayout()

		#now we have the tagDict and a list of 
		#the ones that are vectors and their length.
		#how do we want to go about removing them:  
		
		
		for each in tagDict.keys():
			# make the display look pretty.. in a very unsophisticated way!
			attStr = ''
			for att in tagDict[each]:
			    attStr = attStr + "%s\n" %att
			attStrLbl = QtGui.QLabel(attStr[:-1])
			if len(tagDict[each])==1:
			    # add just the first row: type and attribute
			    formLayout.addRow( str( each + ':'), \
					QtGui.QLabel( tagDict[each][0] ) )
			elif len(tagDict[each]) == 0:  
			    print "something is wrong, this should never happen"
			else:
			    # add the first row and all the rest of the attributes
			    formLayout.addRow(str( each + ':  '), \
					QtGui.QLabel(str( tagDict[each][0] )) )
			    for att in tagDict[each][1:]:
			        formLayout.addRow('', QtGui.QLabel(att) )




		self.reshowBtn.setDisabled(True)
		groupBox.setLayout(formLayout)
		groupBox.setFlat(True)

		#setup remove stuffs:
		removeBox.addWidget(removeLbl)
		self.removeCombo.setEditable(False)

		#recreate the tab also- but without the value;;;
		for each in tag:
			v = True
			for i in vectors:
				if each is i.name[1]:
					print "add tab combobox"
					print i.quantity
					print self.removeDict[each]
					v = False	
					for x in xrange(i.quantity):
						if str(x) not in self.removeDict[each]:
							self.removeCombo.addItem(str( each ) + " " + str(x))
							self.axisCombo.addItem(str( each ) + " " + str(x))
						else:			
							print "do not tab %s" % x
			if v:
				#print "adding this one thats not a vector %s" %each
				self.removeCombo.addItem(str(each))
				self.axisCombo.addItem(str(each))
				#self.axisCombo.addItem(str(each))


		removeBox.addWidget(removeLbl)
		removeBox.addWidget(self.removeCombo)
		removeBox.addWidget(self.applyRemoveBtn)

		#setup choose axis stuffs:
		self.axisCombo.addItem('time')
		self.axisCombo.setEditable(False)
		axisBox.addWidget(axisChoiceLbl)
		axisBox.addWidget(self.axisCombo)
		axisBox.addWidget(self.applyAxisBtn)


		#various btn options - close, apply changes, export plot...

		btnHBox.addWidget( self.reshowBtn )
		btnHBox.addWidget(self.plotExportBtn)
		btnHBox.addWidget(self.closePlotBtn)
	
		#place all the individual components on the display
		layout.addWidget( groupBox )
		layout.addLayout(axisBox)  
		layout.addLayout(removeBox)
		layout.addLayout(btnHBox)      
		plotWidget.setLayout(layout) 
 
		return plotWidget


def getTagList(itemList):
	#takes the itemList and gives us it in a format we can more readily display
	tagDict = dict()
	tag = [x[1] for x in itemList]
	#we want to make this item list into a dictionary    
	for each in itemList:
		if each[0] in tagDict.keys():
		    pass
		else:
		    tagDict[each[0]] = []
		tagDict[each[0]].append(each[1])

	return (tagDict, tag)



class plotStruct(QtCore.QObject):
	'''
		This is a container for the plot and its associated plot bucket tab

		This struct has 2 components, it wraps up the tab that displays information about the plot, and holds the plot.

		going to seperate the tab now.

	'''
	sigCloseAll = QtCore.pyqtSignal(object)

	def __init__(self, statThread, timer,itemList):
		super(plotStruct,self).__init__()
		self.statThread = statThread
		self.timer = timer
		self.itemList = itemList

		self.removeDict = defaultdict(list)
		self.buildPlotAndTab()
			

	def buildPlotAndTab(self):
		tagDict, tag = getTagList(self.itemList) 
		plot = plotDisplay.multiPlot(self.statThread, \
			self.timer, self.itemList, self.printplus(tagDict), \
			 "clockIn", self.removeDict)

		if plot != None:
			self.plot = plot
			self.plot.plot.sigPlotClosed.connect(self.plotClosed)
		
			self.tab = plotTab( (tagDict, tag), \
				plot.vectors, self.itemList )
			

			'''these are to be dismantled'''
			self.tab.applyAxisBtn.clicked.connect(self.applyAxis)
	 		self.tab.applyRemoveBtn.clicked.connect(self.applyRemove)
			''''''
			self.tab.closePlotBtn.clicked.connect(self.closePlot)
			self.tab.plotExportBtn.clicked.connect(self.exportPlot)
			self.tab.reshowBtn.clicked.connect(self.reshowPlot) 


	#This should be seperated so we can use the identical funciton elsewhere...                
	def printplus(self, obj):
		"""returns a string of the data for display purposes"""
		tag = ''
		for k, v in sorted(obj.items()):
			vstr = ''
			for each in v:
			    vstr = vstr  +str(each)+ ', '
			vstr = vstr[:-2]
			#print str(vstr) + 'vstr'
			tag += u'{0}: {1}\n'.format(k, vstr)
		return tag


	'''
	def getTagStr(self, itemList):
		"""this returns a simple string listing all the attributes"""
		lbl = tuple(itemList)
		tag = [x[1] for x in itemList]
		tagStr = str(tag[0])
		for each in tag[1:]:
			tagStr = tagStr +', ' +each
		return tagStr


	'''

	def reshowPlot(self):
		self.plot.plot.show()
		self.reshowBtn.setDisabled(True)


	def closePlot(self):
		#this button will delete the plot and the tab.
		self.plot.plot.hide()
		self.sigCloseAll.emit(self.itemList)

	def plotClosed(self):
		#the x button on the plot makes the plot invisible.  this button allows us to reshow the plot
		self.reshowBtn.setDisabled(False)

	def exportPlot(self):
		self.plot.plot.export()



	''' TODO  we do not want to be able to do this anymore.  '''
	def applyRemove(self):
		#this should removea vector component from the plot.
		thisText = self.removeCombo.currentText()
		#first we need to figure out exactly which value to remove.  
		text = str(thisText).split( );
		self.removeDict[text[0]].append(text[1])
		print "removeDict"
		print self.removeDict
		print thisText
		self.buildPlotAndTab()
		print "apply remove of vector - not yet implemented"


	''' TODO this function will be removed.  we do not want to be able to change axis on the fly. '''

	def applyAxis(self):#changes the axis
		#this will refactor the plot so we have a new x axis
		thisText = self.axisCombo.currentText()
		if thisText != 'time':
			for each in self.itemList:#need to get the complete tuple from the item that was selected
				if thisText == each[1]:
					xAxis = each   
			plot = plotDisplay.multiPlot(self.statThread, self.timer, self.itemList, title = str(xAxis), xAxis = xAxis)
		else:
			plot = plotDisplay.multiPlot(self.statThread, self.timer, self.itemList)

		if hasattr(plot, "plot"):
			self.plot = plot
			self.plot.plot.sigPlotClosed.connect(self.plotClosed)
		else:
			print "Sorry, this plot cannot be created.  Did you try to set a vector as the x-axis? Or maybe you wanted to plot a string?"





class plotBucket(QtGui.QWidget):


	'''plotBucket is the owner of all of the plots.  It has a gui component where you can edit the settings for all of the plots and see which plots are open and it has the individual plots
	'''

	#sigExportSuccess = QtCore.pyqtSignal( 'QString' )
	sigStatusUpdate = QtCore.pyqtSignal( 'QString' )

	def __init__(self, statThread, timer, downSample = 0):
		QtGui.QWidget.__init__(self)
		self.firstPlot      = True
		self.statThread     = statThread
		self.timer   = timer
		self.downSample     = downSample
		self.plots          = dict() 
		self.setupGui()
	
	def cleanList(self, itemList):
		#removes unplottable bits (strings) from the list
		badList = []
		for each in itemList:
			typeOf = self.getType(each)
			#print itemList
			if typeOf == unicode or typeOf == str:
			    self.sigStatusUpdate.emit( 'Attributes of type String cannot be plotted.' )
			    badList.append(each)
		newList = [x for x in itemList if x not in badList]
		return newList




	def getTagStr(self, itemList):#TODO - there is a more pythonic way of doing this
		#this returns a simple string listing all the attributes
		lbl = tuple(itemList)
		tag = [x[1] for x in itemList]
		tagStr = str(tag[0])
		for each in tag[1:]:
			tagStr = tagStr +', ' +each
		return tagStr


	def plotNet(self, itemList):
		'''This first recieves the command to create a new plot.  
			It then processes the item list and decides if we really do want to plot it
			if the plot already exists, it just reshows it.
		'''

		#clean things
		'''What is this doing?  we have lots of clean strings, and pretty prints,
		please consolodate '''
		cleanList = self.cleanList(itemList)
		tupList = tuple(cleanList)


		#why is the first case special?
		if self.firstPlot:
			self.outerTabWidget.setCurrentIndex(0)
			self.firstPlot = False



		# This builds the plots and sticks things where they need to be
		#this plot already exits so we just show it


		if tupList in self.plots.keys():  
			''' If the plot was created, but just
 			closed, then we reshow it'''
			if not self.plots[tupList].plot.plot.isVisible(): 
				self.plots[tupList].reshowPlot()
		else: #build a new plot
			''' 
			if not, we build a new plot
			''' 
			self.plots[tupList] = plotStruct(self.statThread, \
				self.timer, cleanList )
			self.plots[tupList].plot.setDownSample(self.downSample)

			self.plots[tupList].sigCloseAll.connect(self.closeTab)
			self.plots[tupList].plot.plot.sigStatusUpdate.\
				connect(self.statusUpdate)

			self.plotTabWidget.addTab(self.plots[tupList].tab, \
				self.getTagStr(cleanList))
			self.plotTabWidget.setCurrentIndex(\
				self.plotTabWidget.indexOf( self.plots[tupList].tab )) 
	   

	def statusUpdate(self, word):
		''' Looks like this will push a status bar update through '''
		self.sigStatusUpdate.emit(word)

	def applyNewSettings(self):
		#fix this function.  currently, we want it to display in hz, 
		#timer works in ms.  so, 

		''' changes the update frequency and backlog of data shown 
		these will probably be redesigned '''
		self.timer.setInterval(1000 /  float(self.freqLineEdit.text()) )
		self.setDownSample( (int(self.downSampleLineEdit.text()) * -1) )

	def resetCurrentValues(self):
		''' If the person changes them, this will reset to original'''

		self.downSampleLineEdit.setText( str( -1* self.downSample ) )
		self.freqLineEdit.setText( str( ( 1000/ self.timer.interval() ) ) )#timer.interval() is in ms, freq displays in hz

	def setDownSample(self, newdownSample):
		#controls how much data is plotted
		''' Should move this loop into the plot class...'''
		self.downSample = newdownSample
		for each in self.plots.keys():
			self.plots[each].plot.setDownSample(self.downSample)

	def closeTab(self, itemList):
		#This will actually delete the tab and plot from memory
		index = self.plotTabWidget.indexOf( self.plots[tuple(itemList)].tab )
		self.plotTabWidget.removeTab( index )   
		del self.plots[tuple(itemList)]

	def getType(self, plotTuple):
		#returns the type of items in plotTuple
		exec 'array = self.statThread.dataDict[plotTuple[0]].%s' %plotTuple[1] 
		return type(array[0])

	def openGUI(self, size = None):
		if size == None:
			#print 'pick a new size'
			newSize = QtCore.QRect(650,0,250,200)
		else:
			#make it sit right next to the mainwindow.  
			(xp1, yp1, xp2, yp2) = size.getCoords()
			newSize = QtCore.QRect(xp2+65, yp1, 150, yp2-yp1)

		self.setGeometry(newSize)
		self.show()

	def setupGui(self):
		self.setWindowTitle("Plot Bucket")
		self.outerTabWidget = QtGui.QTabWidget()
		self.outerLayout = QtGui.QVBoxLayout()
		self.setupPlottingTab()
		self.setupSettingsTab()
		self.outerTabWidget.setCurrentIndex(1)
		self.outerLayout.addWidget(self.outerTabWidget)
		self.setLayout(self.outerLayout) 

	def setupSettingsTab(self):
		self.settingsLayout = QtGui.QVBoxLayout()
		#frequency stuffs
		self.freqLbl = QtGui.QLabel('Update Frequency:')
		self.freqLineEdit = QtGui.QLineEdit(  str(( 1000 / (self.timer.interval()) )) )#in milliseconds
		self.freqUnits = QtGui.QLabel('Hz')
		self.freqHBox = QtGui.QHBoxLayout()
		self.freqHBox.addWidget(self.freqLineEdit)
		self.freqHBox.addWidget(self.freqUnits) 
		#downSample stuffs
		self.downSampleLbl = QtGui.QLabel('Update Down Sample: \nset to 0 for entire history')
		self.downSampleLineEdit = QtGui.QLineEdit( str(-1 * self.downSample) )
		self.downSampleUnits = QtGui.QLabel('points')
		self.downSampleHBox = QtGui.QHBoxLayout()
		self.downSampleHBox.addWidget(self.downSampleLineEdit)
		self.downSampleHBox.addWidget(self.downSampleUnits)
		#buttons
		self.applyBtn = QtGui.QPushButton('apply')
		self.applyBtn.clicked.connect(self.applyNewSettings)
		self.resetBtn = QtGui.QPushButton('reset')
		self.resetBtn.clicked.connect(self.resetCurrentValues)
		self.hBtnBox = QtGui.QHBoxLayout()
		self.hBtnBox.addWidget(self.applyBtn)
		self.hBtnBox.addWidget(self.resetBtn) 
		self.settingsLayout.addWidget(self.freqLbl)
		self.settingsLayout.addLayout(self.freqHBox)  
		#self.settingsLayout.addWidget(self.downSampleLbl)
		#self.settingsLayout.addLayout(self.downSampleHBox)
		self.settingsLayout.addLayout(self.hBtnBox)
		settingsWidget = QtGui.QWidget()
		settingsWidget.setLayout(self.settingsLayout)
		self.outerTabWidget.addTab(settingsWidget, "settings")

	def setupPlottingTab(self):
		#this sets up the tab area that the plotStruct will add tabs to
		plotWidget = QtGui.QWidget()
		self.plotLayout = QtGui.QVBoxLayout()
		self.plotTabWidget = QtGui.QTabWidget()
		self.plotTabWidget.setTabBar(FingerTabWidget(width=75,height=25))
		self.plotTabWidget.setTabPosition(2)# ?    
		self.plotLayout.addWidget(self.plotTabWidget)
		plotWidget.setLayout(self.plotLayout)
		self.outerTabWidget.addTab(plotWidget, "plots")





class FingerTabWidget(QtGui.QTabBar):
	# http://stackoverflow.com/questions/3607709/how-to-change-text-alignment-in-qtabwidget
	#allows for horiztonal tabs along the vertical

	#TODO  - I want to make the tabText highlightable so that if it is really long we can scroll through it
	def __init__(self, *args, **kwargs):
		self.tabSize = QtCore.QSize(kwargs.pop('width'), kwargs.pop('height'))
		super(FingerTabWidget, self).__init__(*args, **kwargs)

	def paintEvent(self, event):
		painter = QtGui.QStylePainter(self)
		option = QtGui.QStyleOptionTab()

		#painter.begin(self)
		for index in range(self.count()):
			self.initStyleOption(option, index)
			tabRect = self.tabRect(index)
			tabRect.moveLeft(10)
			painter.drawControl(QtGui.QStyle.CE_TabBarTabShape, option)
			painter.drawText(tabRect, QtCore.Qt.AlignVCenter |\
			                 QtCore.Qt.TextDontClip, \
			                 self.tabText(index));
		painter.end()
	def tabSizeHint(self,index):
		return self.tabSize


