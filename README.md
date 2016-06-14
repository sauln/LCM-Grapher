Version Beta!
Please visit http://code.google.com/p/lcm-graphing-utility/

This tool allows real-time visualization of defined LCM messages in an easy to operate graphical interface. It facilitates in the analysis of robot operations data and can help to streamline development of robotic control systems by giving the user the ability to observe LCM message passing in real time and graph the streaming data in various ways. This tool has been written in Python and uses PyQt for the GUI aspects and PyqtGraph for all plotting operations.  It was designed and built by Nathaniel Saul under the supervision of Professor Bingham, with lots of help from Jeff Delmerico.  Work for this project was funded by the University of Hawaii at Manoa's Field Robotics Laboratory and an undergraduate research grant from the College of Engineering. 


Contact: Nathaniel Saul 
         sauln@hawaii.edu

If you have this README I assume you have have the code for the tool. If not you can get it here:  https://code.google.com/p/lcm-graphing-utility/source/browse/

Dependencies:
  * Qt 4.7 or 4.8
  * pyqtGraph 0.9.8:            http://www.pyqtgraph.org
  * pyqt4:                      http://www.riverbankcomputing.com/software/pyqt/download
  * Python Version 2.7:         http://www.python.org/download/releases/2.7/
  * NumPy:                      http://www.numpy.org
  * SciPy:                      http://www.scipy.org 
  * LCM 1.0.0:                  https://code.google.com/p/lcm/ 
 
Warning: For older versions of Ubuntu (10.04 or earlier), you will not be able to upgrade your Qt4 installation through the package manager because Qt 4.6 is the latest supported release. See the instructions on the http://code.google.com/p/lcm-graphing-utility/wiki/UbuntuLucidInstallation page to upgrade your Qt and PyQt packages accordingly.


SETUP:

After installing all of the dependencies we will need to create the python lcmtype bindings.  
If you have already set up FVS then the build process should have created the python lcmtypes in trunk/python/lcmtypes/senlcm.  If you are not using FVS then you must run the lcm-gen for python: http://lcm.googlecode.com/svn/www/manpages/lcm-gen.html.

We then need to add the path to this generated folder to our PYTHONPATH.  You can either add this path manually in the terminal or add the following line to your .bashrc file:
export PYTHONPATH=$Your/Path/To/The/Directory/Containing/The/lcmTypes

for FVS users, it could look like 
export PYTHONPATH=$FVS_ROOT/trunk/python/lcmtypes

You can add multiple paths.




OPERATION/Tutorial:

The 'main' file of the program is the lcm-grapher.py.  Open the program with:
$python lcm-grapher.py 
You will immediately be prompted to declare the folder where lcmtypes is. If you have more than 1 folder you will have to open the input window again with file->import module. 
Alternatively, you can send the folder names in as an argument when you open the program:
$python lcm-grapher.py senlcm folder2 folder3


There are 2 main interfaces.  The first and main one is very similar to the lcm-spy.  It will show information on all of the channels and lcmtypes.  On the left you have a tree which shows each received channel and the associated attributes.  This is the interface that allows us to plot.  The right side of the window starts out empty.  Dragging a type/channel over to this area opens up a detailed view of the values being passed over this channel.  


Basic functionality:
  * drag an type/channel over to the drop area to see a more detailed view of the type/channel
  * open up a new plot- use the check boxes and click plot
  * adjust things about the plot - x axis- 

Definitions:
  * back logged data
  * update frequency





 


    
