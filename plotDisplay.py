
'''
Nathaniel Saul - 2014 


This module contains the classes that handle building the plots and their customizations.  


features:


needed features:
	user defined axis:
		refactor how the user defined axis is used.  Currently we check 
		if it is defined at almost every step
	y scale rescale:
		currently there is no ability to rescale the y axis 
		manually.  everything is autoscaled
	remove vector components:
		this is half done.  gui stuffs are present.  need to create 
		structure to keep track of which ones are deleted and
		then how to replot.
	consolidate 3 classes:
		the 3 classes are a relic of earlier stuffs. 
		I think plotfather and multiplot can be combined into 1
	
	make export plot more apparent

	Destroy the plotBucket - this should be restructured completely. 


'''


'''
	The downsample should be depricated.



'''












from pyqtgraph.Qt import QtGui, QtCore
import numpy
import pyqtgraph
import os
import datetime
import time
import itertools



pyqtgraph.setConfigOption('background', 'b')
pyqtgraph.setConfigOption('foreground', 'k')




"""

There are 2 components:

	the actual plot
		

	, and a gui wrapper.


"""











"""
signals:

sigPlotClosed
sigNewLowerBound
sigStatusUpdate








"""



class MyPlot(pyqtgraph.PlotWidget):
	""" 
	This class holds:
	the viewBox adjustment, the removal of the right click menus,
	export functions, the closeEvents, and whatever find signal does

	"""

	sigPlotClosed = QtCore.pyqtSignal()
	sigNewLowerBound = QtCore.pyqtSignal(float)
	sigStatusUpdate = QtCore.pyqtSignal( 'QString' )
	def __init__(self, tite):  
		super(MyPlot, self).__init__(title = tite)
		self.enableAutoRange('y' , 1)
		self.viewBox = self.getViewBox()
		self.viewBox.sigRangeChangedManually.connect(self.findSignal)
		menu = self.getMenu()
		menuitmes = [k for k,v in menu.__dict__.items() ]#if isinstance(v, pyqtgraph.QtGui.QWidget)]
		self.plotItem.ctrlMenu = None  # get rid of 'Plot Options'
		self.scene().contextMenu = None  # get rid of 'Export'
		self.addLegend()

	def export(self):
		'''
		will export the function to the current 
		working directory and then move it to /plots/, 
		a directory within the cwd
		'''
		cwd = os.getcwd()
		newpath = cwd + "/plots"
		if not os.path.exists(newpath): 
			os.makedirs(newpath)
		exporter = pyqtgraph.exporters.ImageExporter.ImageExporter(self.plotItem)
		name = '%s.png' % time.time()
		exporter.export(name)    
		newName = "./plots/%s" %name
		os.rename(name, newName)
		self.sigStatusUpdate.emit("plot %s exported successfully" % newName)

	def closeEvent(self, ev):
		'''
		This will send a signal to close the window when needed. 
		'''
	
		self.sigPlotClosed.emit()

	def findSignal(self):
		'''
		When the user drags the graph to the right, a new lower bound is set
		'''
		lowerBound = self.viewBox.getState()['targetRange'][0][0]
		self.sigNewLowerBound.emit(lowerBound)


class multiPlot(QtGui.QMainWindow):


	'''TODO If the xAxis is user determined then it is a tuple otherwise it xAxis is a string... this is a bad design...'''

	def __init__(self, statThread, timer,  plotThese, \
		title = "stop here", xAxis = 'clockIn', removeDict = []):
		super(multiPlot, self).__init__()


		self.statThread = statThread
		self.timer = timer
		self.timer.timeout.connect(self.update)
		self.xAxis = xAxis
		self.title = title
		self.removeDict = removeDict


		self.lbl = "plot"
		self.downSample = 0
		self.colorList = ['b', 'g', 'r', 'c','m', 'y', 'k', 'w']
		self.vectList   = []
		self.vectors = []
		self.curve = dict()



		if self.xAxis == 'clockIn':
			self.plotList = plotThese
			self.userDefdAxis = False
		else:
		    if self.getType(xAxis) is list or self.getType(xAxis) is tuple:
		        return
		    else:
		        self.plotList = [x for x in plotThese if x != self.xAxis]
		        self.userDefdAxis = True
		self.setupPlot() 


	def getArray(self, plotTuple):
		exec 'array = self.statThread.dataDict[plotTuple[0]].%s' %plotTuple[1]
		return array    #[self.downSample:]

	def getType(self, plotTuple):
		exec 'array = self.statThread.dataDict[plotTuple[0]].%s' %plotTuple[1] 
		return type(array[0])

	def getDownSample(self):
		return self.downSample

	def setDownSample(self, newDownSample): 
		self.downSample = newDownSample


	def setupPlot(self):
		numplot = 0
		self.plot = MyPlot(self.title)
		self.plot.sigNewLowerBound.connect(self.newLowerBound)


		for each in self.plotList: 
			typeOf = self.getType(each)
			if typeOf is list or typeOf is tuple:	
				
				#	here we use this new structure to to deal with 
				#	seperating the vectors better - 

				vectInfo = vectStruct(each, len(self.getArray(each)[0]))
				self.vectors.append(vectInfo)
				self.plotVectors(each, numplot)
			else:
				if self.userDefdAxis:#determine axis, 
					xAxis = self.getArray(self.xAxis)
				else:
					xAxis = self.getArray((each[0], self.xAxis))#get

				att = each[1]
				self.curve[att] = self.plot.plot(x = xAxis, \
								y = self.getArray(each), \
								pen = self.colorList[numplot], \
								name = str(att))
				numplot = numplot +1
		 
		if self.userDefdAxis:#because 'clockIn' isn't a good label
		    self.lbl = str(self.xAxis)
		else:
		    self.lbl = 'time'

		#self.plot.setWindowTitle('Plo')
		self.plot.setLabel('bottom', self.lbl)
		self.plot.show()

	def plotVectors(self, vector, numplot):

		#print "plotVectors"
		#print self.removeDict

		#print vector


		data = self.getArray(vector)
		if self.userDefdAxis:#determine axis
		    xAxis = self.getArray(self.xAxis)
		else:
		    xAxis = self.getArray((vector[0],'clockIn'))[1:]

		if vector[1] in self.removeDict.keys():
			self.vectList = self.removeDict[vector[1]]
			print "this vector has an item to remove"



		for i in range(0, len(self.getArray(vector)[0])):
			#print "vectList?"
			#print i
			#print self.vectList
			#print i
			if str(i) not in self.vectList: #what is vectList??
				#print "is this not registering? %s %s" %(i, self.vectList)
				eachArray = [row[i] for row in itertools.islice(data, 1, None)]
				self.curve[i] = self.plot.plot(x=xAxis, \
				y=eachArray ,pen = self.colorList[numplot % 8 ], \
				name = str(vector[1] + ' '+str(i)) )
				numplot = numplot +1
    
	def updateVectors(self, each, xAxis):
		data = self.getArray(each)
		for i in range(0, len(self.getArray(each)[0])):
			if str(i) not in self.vectList:
				eachArray = [row[i] for row in itertools.islice(data, 1, None)]
				self.curve[i].setData(xAxis[self.downSample:], \
				eachArray[self.downSample:], clear = True)

	def update(self):
		for each in self.plotList:			
			typeOf = self.getType(each)
			if typeOf is list or typeOf is tuple:
				#print "its a list!!"
				if self.userDefdAxis:#determine axis
					xAxis = self.getArray(self.xAxis)
				else:
					xAxis = self.getArray((each[0],'clockIn'))[1:]

				self.updateVectors(each, xAxis)
				#update the vector
			else:
				if self.userDefdAxis:#axis is clock in
					xAxis = self.getArray(self.xAxis)
				else:
					xAxis = self.getArray((each[0], self.xAxis))


				#normal update
				self.curve[each[1]].setData(xAxis[self.downSample:], \
							self.getArray(each)[self.downSample:], clear = True)
				
		dataUpperBound = xAxis[-1]
		viewBoxUpperBound =  self.plot.viewBox.getState()['viewRange'][0][1]

		if dataUpperBound > viewBoxUpperBound:
			self.plot.enableAutoRange(axis=self.plot.viewBox.XAxis, enable=True, x=None, y=None)

	def newLowerBound(self, lowerBound):

		#deals with when the user manually pans the plot over,  
		if not self.userDefdAxis: #the axis is not user defined, it is 'clockIn'
		    xAxis = self.getArray((self.plotList[0][0],'clockIn'))[1:]
		    i = 0
		    while lowerBound > xAxis[i]:
		        i = i+1

		    self.setDownSample(i)

		else: #the x-axis is user defined.  
	   	#TODO this has not been implemented:
		    xAxis = self.getArray(self.xAxis)[1:]

		self.plot.enableAutoRange(True)
		




class vectStruct():
	""" 
	This is a simple structure to hold the vector and how many dimensions the vector has
	"""
	def __init__(self, name, quantity):
		self.name = name
		self.quantity = quantity









class PlotFather(QtGui.QMainWindow):

	'''
	THIS IS  NOW OBSOLETE

	BEEN ABSORBED INTO multiplot

	this holds some of the low level functions for the plotting needs.

	let's combine with the myplot
	 


	#sigPlotExportSuccess = QtCore.pyqtSignal( 'QString' )
	#sigStatusUpdate = QtCore.pyqtSignal( 'QString' )

	'''
	def __init__(self, statThread, timer, downSample = 0, vectList = []): #, statThread, timer):   
		super(PlotFather, self).__init__()
		#plt.plotItem.ctrlMenu = None  # get rid of 'Plot Options'
		#>>> plt.scene().contextMenu = None  # get rid of 'Export'
		self.downSample = downSample
		self.statThread = statThread
		self.timer = timer
		self.colorList = ['b', 'g', 'r', 'c','m', 'y', 'k', 'w']
		self.timer.timeout.connect(self.update)
		self.lbl = "plot"
		self.vectList = vectList;

	def getArray(self, plotTuple):
		exec 'array = self.statThread.dataDict[plotTuple[0]].%s' %plotTuple[1]
		return array    #[self.downSample:]

	def getType(self, plotTuple):
		exec 'array = self.statThread.dataDict[plotTuple[0]].%s' %plotTuple[1] 
		return type(array[0])

	def getDownSample(self):
		return self.downSample

	def setDownSample(self, newDownSample): 
		self.downSample = newDownSample






#attempt to get a better rightclick menu...
#self.myMenu()
"""
self.ctrlMenu = QtGui.QMenu()
self.ctrlMenu.setTitle('Plot Options')
self.subMenus = []

sm = QtGui.QMenu('Export')
act = QtGui.QWidgetAction(self)
act.setDefaultWidget(self.export)
sm.addAction(act)
self.subMenus.append(sm)
self.ctrlMenu.addMenu(sm)
"""




#def buildMenu(self):
#	myMenu 


#def myMenu(self, pos):
#	self.plotItem.menu = QtGui.QMenu()
#	self.plotItem.menu.addAction(self.export, 'export')
#	self.menu.exec_(self.mapToGlobal(event.pos())) 





