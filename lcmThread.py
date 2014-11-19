import sys, inspect, os, time
import lcm
from PyQt4 import QtCore, QtGui
import time
import sip
from modulePopup import modulePopup

#Sometimes this thread does not hear all of the channels.  We need some sort of reset button that will make it work again.
'''Listens to LCM and decodes the messages.  signs up new channels and sends arriving messages where they need to go.  It also imports all of modules'''

class lcmThread(QtCore.QThread):  
	sigNewMsg           = QtCore.pyqtSignal(object, 'QString',  'QString')
		#every time a new message comes in, we send the decoded message to the statThread
	sigUndecodeMsg      = QtCore.pyqtSignal('QString')
		#if a message is undecodable then we still send it to statThread
	sigRemoveChannels   = QtCore.pyqtSignal(object)
		#to refactor the display when new modules have been imported
	sigTakeAttDict      = QtCore.pyqtSignal(object)

	def __init__(self): #modules):
		QtCore.QThread.__init__(self)
		self.lc                 = lcm.LCM()
		self.running = True
		#self.modules            = modules   #modules that we want to import
		self.inModList          = []        
			#modules that have been successfully imported
		self.attDict            = dict()    
			#key - type;                value - list of attributes
		self.classTypeDict      = dict() 
		self.classNameDict 		= dict()  
			#key - channel;             value - class definition for that type
		self.typeList           = []        
			#the list of types.  
		self.undecodableList   = []         
			#list of channels that cannot be decoded
		self.ignoreList = ["LCM_TUNNEL_INTROSPECT",
				  'LCM_SELF_TEST',
				  "att_imu.RAW"]

		self.findTypes()
   
	def refreshAttDict(self):
		self.findTypes()
		self.sigTakeAttDict.emit(self.attDict)
		


         
	def refactorChannels(self):
		'''
		new modules have been imported, must update all of our lists. 
		remove potentially unwanted stuff from the treeWidget.  
		find all the new good types.  
		reset the unwanted stuff list-- 
		anonHandler will rebuild this list if necessary
		'''
		self.sigRemoveChannels.emit(self.undecodableList)
		self.findTypes()
		self.undecodableList = [] #remove everything from the undecodeableList, they will be readded if need be





	def run(self):
		#opens up the thread to subscribe to all -  
		self.subscription = self.lc.subscribe(".*", self.anonHandler)     
		#print("running")
		while self.running:
		    self.lc.handle()             
	
	def importMod(self, module):
		#print "check 2 lcmThread.importMod"
		try:
		    exec 'global %s' %module
		    exec 'import %s' %module 
		    exec 'self.typeList.extend(inspect.getmembers(%s,inspect.isclass))' %module 
		    return 1   
		except Exception:
		    return 0   

	def findTypes(self):#   
		#this gets all of the attributes and types 
		#fills the attDict
		for each in self.typeList:
		    self.attDict[each[0]] = ( [x for x in dir(each[1]) if not(x[0]=='_')
		        if not(x=='decode')
		        if not(x=='encode')] )

		self.sigTakeAttDict.emit(self.attDict)#give the attDict to the statThread

	def anonHandler(self, channel, data):
		'''
		Everytime a message is heard, this method decodes it, 
		stores the data where it needs to be stored and emits a 
		signal.  If the message is not decodable then it	
		handles it properly'''
		
		success = False
		if channel in self.ignoreList:
		    pass
		elif channel in self.undecodableList:
		    self.sigNewMsg.emit(None, channel, "unknown")

		elif channel in self.classTypeDict:
		    msg = self.classTypeDict[channel].decode(data)           
		    self.sigNewMsg.emit(msg, channel, self.classNameDict[channel])


		else:
		    #brute force method for decode a message 
			#for the first time we've come across the channel
			#print self.typeList
			for lcmtype in self.typeList:
				try:
					msg = lcmtype[1].decode(data)
					self.classTypeDict[channel] = lcmtype[1]#stores the class/type definition associated with the channel
					self.classNameDict[channel] = lcmtype[0]
					self.sigNewMsg.emit(msg, channel, self.classNameDict[channel])               
					success = True              
				except ValueError:
					pass
			if not success:
				self.undecodableList.append(channel)
				self.sigNewMsg.emit(None, channel, "unknown" )
				print "channel %s was undecodable"%channel

	def __del__(self):
		self.wait()

	'''
	def importMods(self, modules):
		#normally, this function will import the modules and add the types from each module to the list-
		#if it cannot import a module it will prompt for the user to input it again
		#it needs to tell us if it successfully imports a module
		oneSuccess = False
		badList = []
		if modules:
		    for module in modules:
		        if module in self.inModList:
		            pass
		            #print "We have already imported module %s" %module
		        else:
		            try:
		                exec 'global %s' %module
		                exec 'import %s' %module 
		                exec 'self.typeList.extend(inspect.getmembers(%s,inspect.isclass))' %module 
		                self.inModList.append(module)
		                oneSuccess = True    
		            except Exception:
		                badList.append(module)                 
		else:
		    self.openImporter()
		if len(badList) >= 1: 
		    self.openImporter(badList)

			#change the statusBar
		    print "unable in import the following modules: %s" % str(badList)
		if oneSuccess:#if at least one of the modules were successfully imported, then we refactor
		    self.refactorChannels()

	'''	      
