#This module is the central control unit.  All threads and windows are owned by this unit.  It is the 'main' and executable that we want to run  

from PyQt4 import QtCore, QtGui
import sys 
# 3 Threads #

import lcmThread
reload(lcmThread)
import statThread
reload(statThread)
from modulePopup import modulePopup
import GUIWindow
reload(GUIWindow)

class lcmGrapher():
	def __init__(self, modules):
		self.modules = modules
		self.inModList = []
		self.beginQTimer()
		self.beginLCMThread()
		self.beginStatThread()
		self.setupMainWindow() 
		self.buildConnections()
		self.importMods(modules)

	def buildConnections(self):
		self.statThread.sigNewChannel.connect(self.main.tree.newTreeChannel)
		#self.lcmThread.sigNewChannel.connect(self.main.tree.newTreeChannel)
		#self.lcmThread.sigRemoveChannels.connect(self.main.tree.removeTreeChannels)
		if hasattr(self.lcmThread, 'errorWindow'):
			#refresh the error screen just to make 
			#sure it shows up in the front
			self.lcmThread.errorWindow.show()

	def beginLCMThread(self):
		'''
        This thread is the LCM listener. It uses senlcm to find 
		all of the types that lcm might use. When it receives a 
		message it associates that message to it's type. When it 
		discovers a new channel it will emit a signal intended to 
		be heard by the mainWindow. Every time it receives a new 
		message it emits a signal.  StatThread listens to this signal
		'''
		
		self.lcmThread = lcmThread.lcmThread() #modules
		self.lcmThread.start()

	def beginQTimer(self):
		'''
		This thread emits a signal that tells the GUI when to 
		update itself.  The rate can be adjusted by means that 
		aren't completely built
		'''
		self.timer = QtCore.QTimer()
		self.timer.setInterval(100)
		self.timer.start()

		#self.updateThread = updateThread.GUIupdateThread()
		#self.updateThread.start()        
	
	def beginStatThread(self):
		'''This thread receives messages from LCMThread every 
		time there is a new message.  Each 	message is stored 
		in this thread. This thread will compute statistics 
		about the messages, such as frequency.'''

		self.statThread = statThread.statThread()
		self.lcmThread.sigNewMsg.connect( self.statThread.newMsg )
		#self.lcmThread.sigNewChannel.connect( self.statThread.newChannel )
		self.lcmThread.sigTakeAttDict.connect( self.statThread.newAttDict )
		self.lcmThread.refreshAttDict()
		self.statThread.start()

	def setupMainWindow(self):
		self.main = GUIWindow.mainWindow(self.lcmThread, \
			self.statThread, self.timer)
		self.main.sigResetLCM.connect(self.resetLCM)
		self.main.sigOpenImporter.connect(self.openImporter)
		self.main.show()

	def openImporter(self, module=None):
		self.errorWindow = modulePopup(module) 
		self.errorWindow.refactorSize()
		self.errorWindow.sigMods.connect(self.importMods)
		self.errorWindow.show()

	def importMods(self, modules):
		'''
		normally, this function will import the modules and
		add the types from each module to the list-
		if it cannot import a module it will prompt for 
		the user to input it again
		'''
		oneSuccess = False
		badList = []
		if modules:
		    for module in modules:
				if module in self.inModList:
					pass
		            #print "We have already imported module %s" %module
				else:
					oneSuccess = self.lcmThread.importMod(module)
					if oneSuccess:
						self.inModList.append(module)
					else:
						badList.append(module)
		            	            
		else:
		    self.openImporter()

		if len(badList) >= 1: 
		    self.openImporter(badList)
		    self.main.statusBar().showMessage( "unable in import modules: %s" \
				% str(badList) )
		if oneSuccess:
			#if at least one of the modules were successfully 
			#imported, then we refactor
			self.main.statusBar().showMessage( \
				"successfully imported modules: %s" % self.inModList )
			self.lcmThread.refactorChannels()
			self.lcmThread.refreshAttDict()


	def resetLCM(self):
		self.main.tree.removeTreeChannels()
		self.beginLCMThread(self.modules)
		self.lcmThread.sigNewMsg.connect( self.statThread.newMsg )
		#self.lcmThread.sigNewChannel.connect( self.statThread.newChannel )
		#self.lcmThread.sigNewChannel.connect(self.main.tree.newTreeChannel)
		self.lcmThread.sigRemoveChannels.connect(self.main.tree.removeTreeChannels)
		self.lcmThread.sigTakeAttDict.connect( self.statThread.newAttDict )




def main( ):  
	app = QtGui.QApplication(sys.argv)
	guimanager = lcmGrapher(sys.argv[1:])
	if KeyboardInterrupt:
		sys.exit(app.exec_())

if __name__ == '__main__':
    main() 


