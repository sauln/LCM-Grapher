'''
lcmdata.py

Module for parsing LCM logs.

Nathaniel Saul plans to make fields of vectors saved into individual issues




'''

import numpy as np
import sys, csv
from copy import deepcopy
# for new-style classes: x.__class__ = type(x) and we can use super()
class lcmdata(object):  # use (object) to establish a new-style class
    '''
    '''
    def __init__(self,fieldlist=None):
        pass

    def addmsg(self,msg):
        ''' 
        Adding a new message to the collection
        '''

        #edits by Nathaniel Saul - to add online statistic computations


        fields = msg_getfields(msg)
        #print fields
        for f in fields:
            if f != "startTime":
                
                val = getattr(msg,f)
            #print f,
            #print val,
            #print type(val)
                if not(hasattr(self,f)):
                    if isinstance(val,float) \
                            or isinstance(val,int) \
                            or isinstance(val,str) \
                            or isinstance(val,unicode) \
                            or isinstance(val,long):
                        setattr(self,f,[])

                    #right here - don't this suck...
                    elif isinstance(val,tuple):
                        setattr(self,f,[])
                        val = list(val)
                    elif isinstance(val,list):
                        setattr(self,f,[])
                        val = list(val)   
                    else:
                        print("Don't know what to do withy field %s of type %s" \
                                %(f,type(val)))
                    
                try:
                    getattr(self,f).append(val)
                except:
                    print "lcmdata: Error appending a new value!"
                    print f,
                    print val,
                    print type(val)
                    sys.exit()
    def add_val(self,attrname,val):
        '''
        val must be a scalar (int, str, long, float, etc.)
        '''
        if not(hasattr(self,attrname)):
            setattr(self,attrname,[])
        getattr(self,attrname).append(val)
            

    def toarrays(self):
        ''' convert all the data to numpy.arrays
            returns a new lcmdata where all the data is numpy.arrays
        '''
        fields = getfields(self)
        selfarrays = deepcopy(self)
        for f in fields:
            # check to make sure it is numeric
            setattr(selfarrays,f,
                    np.array(getattr(self,f)))
        return selfarrays

    def fieldtoArray(self, field):#real beta
        selfarray = deepcopy(self.field)
        setattr(selfarray, field, np.array(getattr(self,field)))
        return selfarray


    def todict(self):
        '''
        Convert lcmdata object to a dictionary.
        Handy for saving as a MATLAB file
        '''
        fields = getfields(self)
        mdict = dict()
        for f in fields:
            mdict[f]=np.array(getattr(self,f))

        return mdict
       
    def tocsv(self,fname):
        '''
        Write contents of the lcmdata structure to a CSV file
        Written for GSS lcm on Okeanos
        '''
        try:
            csvfile = open(fname,"w")
        except:
            print "Error opening file <%s>"%fname
            return False
        writer = csv.writer(csvfile)
        # Make a list of headers
        headers = []
        fields = getfields(self)
        for ff in fields:
            # Debugging
            #print ff,
            #print type(getattr(self,ff)),
            #print (getattr(self,ff)).shape,
            #print len((getattr(nrvNavData,ff)).shape)

            # Get shape of the array to determine if it is 1 or 2D
            sh = (getattr(self,ff)).shape
            if (len(sh) == 1):
                headers.append(ff)
            elif (len(sh) == 2):
                for ii in range(sh[1]):
                    headers.append("%s[%d]"%(ff,ii))
            else:
                print "Error with defining header for %s"%ff
                
        writer.writerow(headers)
        
        # Number of rows
        N = (getattr(self,fields[0])).shape[0]
        for ii in range(N):
            row = []
            for ff in fields:
                sh = (getattr(self,ff)).shape
                if (len(sh) == 1):
                    row.append(getattr(self,ff)[ii])
                elif (len(sh) == 2):
                    for jj in range(sh[1]):
                        row.append(getattr(self,ff)[ii][jj])
                        
            writer.writerow(row) 
        print "Wrote lcmdata structure (%d lines) to file: %s"%(N,fname)
# End of class definition

def getfields(struct):
    ''' 
    Return a list of the data fields
    '''
    dflt = dir(lcmdata())
    these = dir(struct)
    fields = [x for x in these if not(x in dflt)]
    return fields

def msg_getfields(lcm_msg):
    '''
    
    Return a list of data fields contained in a decoded LCM event
    '''
    full = dir(lcm_msg)
    # a little list comprehension to get rid of any attributes 
    # that start with an underscore 
    # or 
    fields = [x for x in full if not(x[0]=='_') 
              if not(x=='decode')
              if not(x=='encode')]
    return fields

    
    
