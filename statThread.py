"""

#TODO   Add statistical features, ie frequency of messages, range,  min&max, mean,  standard deviation 
#TODO   have statThread save data even when lcmThread restarts
#TODO   allow for export of data in a nice format
#TODO   seperate the vector values so they can be plotted individually.


"""

from PyQt4 import QtCore
from datetime import datetime
import time

import lcmdata
reload(lcmdata)
       
class statThread(QtCore.QThread):


	sigNewChannel = QtCore.pyqtSignal(object, 'QString', 'QString')
	def __init__(self):  # lcmThread):
		QtCore.QThread.__init__(self)
		self.attDict = dict()#Think of this as a list of all the attributes.  
		self.dataDict = dict()
	def newAttDict(self, attDict):
		self.attDict = attDict

	def newMsg(self, msg, channel, lcmType):
		'''
		gets called by the lcmThread signal
		Initiate a new channel- add to the  normal message- 
		'''

		channel = str(channel)
		#print channel
		#print lcmType
		#print self.dataDict

		if channel not in self.dataDict:
			print "add"
			self.dataDict[channel] = lcmdata.lcmdata()
			self.dataDict[channel].addmsg(msg)
			self.sigNewChannel.emit(self.dataDict[channel], channel, lcmType)
			self.dataDict[channel].startTime = self.getTime() 
			self.dataDict[channel].clockIn = []
			self.dataDict[channel].clockIn.append(0)
			self.dataDict[channel].count = 1
			self.dataDict[channel].frequency = 0
			self.dataDict[channel].calcAble = []
		else:
			self.dataDict[channel].addmsg(msg)
			since = ( self.getTime() - self.dataDict[channel].startTime ) / 1000000
			self.dataDict[channel].clockIn.append(since)
			self.dataDict[channel].count += 1
			elapsedTime = ((self.getTime()/1000000000) -\
				self.dataDict[channel].startTime)
			self.dataDict[channel].frequency = \
				round(elapsedTime / self.dataDict[channel].count , 3)
			print "here"
	
		"""
		if channel not in self.dataDict:
			''' If this is the first time we've heard this channel,
			init a new channel place'''
			
			self.dataDict[channel] = lcmdata.lcmdata()

			self.dataDict[channel].addmsg(msg)


			self.sigNewChannel.emit(self.dataDict[channel], channel)

			self.dataDict[channel].clockIn = []
			self.dataDict[channel].clockIn.append(0)
			self.dataDict[channel].startTime = self.getTime() 
			self.dataDict[channel].count = 1
			self.dataDict[channel].frequency = 0
			self.dataDict[channel].calcAble = []
		else:
			self.dataDict[channel].addmsg(msg)
			since = ( self.getTime() - self.dataDict[channel].startTime ) / 1000000 
			self.dataDict[channel].clockIn.append(since)
			self.dataDict[channel].count += 1
			elapsedTime = ((self.getTime()/1000000000) -\
				self.dataDict[channel].startTime)
			self.dataDict[channel].frequency = \
				round(elapsedTime / self.dataDict[channel].count , 3)
			
		"""
	

	def getTime(self):
		now = datetime.now()
		timestamp = now.microsecond
		timestamp = timestamp + now.second * 1000000
		timestamp = timestamp + now.minute * 1000000 * 60
		timestamp = timestamp + now.hour   * 1000000 * 60 * 60  
		timestamp = float(timestamp) 
		return timestamp

        
