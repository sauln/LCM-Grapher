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
    def __init__(self):  # lcmThread):
        QtCore.QThread.__init__(self)
        self.attDict = dict()#Think of this as a list of all the attributes.  
        self.dataDict = dict()

    def newAttDict(self, attDict):
        self.attDict = attDict

    def newChannel(self, msg, channel, lcmType):#gets called by the lcmThread signal
        #Initiate a new channel- add to the  normal message- 

        channel = str(channel)
        self.dataDict[channel] = lcmdata.lcmdata()
        self.dataDict[channel].addmsg(msg)
        self.dataDict[channel].clockIn = []
        self.dataDict[channel].clockIn.append(0)
        self.dataDict[channel].startTime = self.getTime()  #time.clock()  #self.getTime() )
        self.dataDict[channel].count = 1
        self.dataDict[channel].frequency = 0
        self.dataDict[channel].calcAble = []




    def newMsg(self, msg, channel):
        channel = str(channel)
        self.dataDict[channel].addmsg(msg)   
        since = ( self.getTime() - self.dataDict[channel].startTime ) / 1000000 
        self.dataDict[channel].clockIn.append(since)
        self.dataDict[channel].count += 1
        elapsedTime = ((self.getTime()/1000000000) - self.dataDict[channel].startTime)
        self.dataDict[channel].frequency = round(elapsedTime / self.dataDict[channel].count , 3)

    def getTime(self):
        now = datetime.now()
        timestamp = now.microsecond
        timestamp = timestamp + now.second * 1000000
        timestamp = timestamp + now.minute * 1000000 * 60
        timestamp = timestamp + now.hour   * 1000000 * 60 * 60  
        timestamp = float(timestamp) 
        return timestamp

        
