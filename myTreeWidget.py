#myTreeWidget

import sys
import copy
from PyQt4 import QtCore, QtGui
import datetime
import plotDisplay
reload(plotDisplay)
import sip
import lcmdata
import numpy as np

"""
TODO

We will have to add a third tier to the tree to accomodate for vectors




"""










class myTreeWidget(QtGui.QWidget):
    #builds the treeWidge that allows us to see all of the channels that the GUI hears.  
    sigPlotBtnClicked = QtCore.pyqtSignal(object)
    def __init__(self, statThread):
        super(myTreeWidget, self).__init__() 
        self.statThread     = statThread
        self.channel        = dict()
        self.plots          = dict()
        self.checkedList    = []
        self.childList      = []
        self.treeWidget     = QtGui.QTreeWidget()
        self.plotBtn        = QtGui.QPushButton("plot")
        self.vTreeLayout    = QtGui.QVBoxLayout()
        self.setup()
        #print self.getContentsMargins()
        self.setContentsMargins(0,0,-8,0)
        
    def setup(self):
        self.setMinimumSize(200,200)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setHeaderHidden(True)   
        self.treeWidget.itemChanged.connect(self.handleChanged)
        self.plotBtn.clicked.connect(self.plotDisplay)
        self.vTreeLayout.addWidget(self.treeWidget)
        self.vTreeLayout.addWidget(self.plotBtn)
        self.setLayout(self.vTreeLayout)
        
    def plotDisplay(self):
        #emits a message intended for plotBucket to create a new plot, then clears all of the checkboxes
        chckedList = sorted(copy.deepcopy(self.checkedList))
        if not self.checkedList:
            print 'Please check at least one attribute to be plotted' 
        else:
            self.sigPlotBtnClicked.emit(chckedList) 
        self.clearCheckBoxes()
     
   
    def clearCheckBoxes(self):
        #goes through a list of all of the children and makes them unchecked-
            #we could probably only go to the ones that are checked...
        for each in self.childList:
            each.setCheckState(0, QtCore.Qt.Unchecked)
        #print str( self.checkedList ) + "myTreeWidget.clearCheckBoxes"

    def removeTreeChannels(self, undecodableList = 1):
		if undecodableList == 1:
			for channel in self.channel.keys():
				sip.delete(self.channel[channel])
			self.checkedList = []
			self.childList = []
			self.channel.clear()
		else:
			for channel in undecodableList:
				try:
					sip.delete(self.channel[channel])
				except:
					pass
					#print "%s must not have been there before" %channel
    
    def newTreeChannel(self, msg, channel, lcmType):
		print lcmType
		#lcmType = "pose_t"
		#print dir(msg)
		#print dir(lcmdata.lcmdata)
		#print "here"
		#print type(msg)


		#
		fields = lcmdata.getfields(msg)
		print fields
		print dir(msg)
		print msg.__class__
		for each in fields:
			print msg.__dict__[each]
		#fields1 = lcmdata.msg_getfields(msg)

		#print fields1
		#for each in msg.__dict__.keys():
		#	print msg.__dict__[each]
		#	print each
		#	print max(np.shape(msg.__dict__[each]))




        #Builds the tree based on the messages that lcmThread hears
		channel     = str(channel)
		parent      = self.treeWidget.invisibleRootItem()
		column      = 0
		title = "%s"%channel#/%s" % (channel, lcmType)
		self.channel[channel] = self.addParent(parent, column, title, str(channel))
		#only adds the children if the channel was decodable-  clunky
		if lcmType != "unknown":
			self.channel[channel].setExpanded(False)
			#we need lcmThread.attDict out.
			for att in self.statThread.attDict[str(lcmType)]:

				#print self.statThread.dataDict.keys()
				#print "stop"
				#print type(self.statThread.dataDict[str(att)])
				child = self.addChild(self.channel[channel], column, '%s' %str(att), 'data %s' %str(att))
				self.childList.append(child)


    def addParent(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded (True)
        return item

    def addChild(self, parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setCheckState (column, QtCore.Qt.Unchecked)
        return item

    def handleChanged(self, item, column):
        # keep track of which boxes checked and unchecked. 
        self.settingUp = False #makes it not do unexpected things while the children are being initiated.
        if item.checkState(column) == QtCore.Qt.Checked:
            parent      = item.parent()
            parentstr   = parent.text(0).split('/')
            self.checkedList.append((str(parentstr[0]), str(item.text(column))))
        if item.checkState(column) == QtCore.Qt.Unchecked:
            try: #this needs to be checked - i wrote it so long ago I am unsure how necessary it is.
                parent      = item.parent()
                parentstr   = parent.text(0).split('/')
            except:
                self.settingUp = True  
            if not self.settingUp:
                chckTuple = (  str(parentstr[0]), str(item.text(column))  )
                if chckTuple in self.checkedList:
                    self.checkedList.remove(chckTuple)

