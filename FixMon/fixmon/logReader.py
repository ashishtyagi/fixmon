'''
Created on Dec 8, 2013

@author: ashish
'''

# this file read quickfix logs and insert in DB.

import quickfix as fix
import quickfix44 as fix44
from fixmon.models import FixMsg
import datetime

class FixLogReader:
    logfile = {}
    def __init__(self, logfile=None):
        self.logfile = logfile
        
    def readAll(self):
        for txt in file(self.logfile):
            self.readLine(line=txt)
            #break;
        
    def readLine(self,line=None):
        try:
            txt = line.strip('\n')
            timeStamp = txt[:txt.index(' ')]
            print 'timestamp = ' + timeStamp
            data = txt[txt.index(' ') + 1 :]
            msg = fix.Message();
            msg.setString(data)
            print msg.getHeader().getField(52)
            fm = FixMsg(
                        ReceivedTimeStamp = datetime.datetime.strptime(timeStamp,"%Y%m%d-%H:%M:%S.%f").strftime('%Y-%m-%d %H:%M:%S.%f'),
                        RcvTime_SeqNum = timeStamp + '_' + msg.getHeader().getField(34),
                        BeginString = msg.getHeader().getField(8),
                        BodyLength = int(msg.getHeader().getField(9)),
                        MsgType = msg.getHeader().getField(35),
                        SenderCompID = msg.getHeader().getField(49),
                        TargetCompID = msg.getHeader().getField(56),
                        MsgSeqNum =int( msg.getHeader().getField(34)),
                        SendingTime = datetime.datetime.strptime(msg.getHeader().getField(52),"%Y%m%d-%H:%M:%S.%f").strftime('%Y-%m-%d %H:%M:%S.%f'),
                        CheckSum = int(msg.getTrailer().getField(10)),
                        text = data,
                        xml = msg.toXML()
                        )
            fm.save()
                        
        except Exception as exp_:
            print 'Exception = ' +str( exp_)
            pass
        else:
            print 'done.'
        
        
        