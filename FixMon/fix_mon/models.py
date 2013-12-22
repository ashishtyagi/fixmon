from django.db import models


class Config(models.Model):
    KEYS = (
        ('FixLogDir', 'FixLogDir'),
        ('BackDays', 'BackDays'),
    )
    key = models.CharField(max_length=128, choices=KEYS)
    value = models.CharField(max_length=1048)
    
    def __str__(self):
        return self.key;

class Lookup(models.Model):
    tag = models.IntegerField(null=False)
    shortName = models.CharField(max_length=128,null=False)
    stringValue = models.CharField(max_length=128,null=False)
    
class ColumnConfig(models.Model):
    SOURCE_TYPES = (
        ('json', 'json'),
        ('xml', 'xml'),
    )
    
    name = models.CharField(max_length=64)
    position = models.IntegerField(null=False)
    sourceType = models.CharField(max_length=16, choices=SOURCE_TYPES)
    path = models.TextField('Xpath in case of xml source and field name in case of json')
    
    def __str__(self):
        return self.name;
    
class FixMsg(models.Model):
    ReceivedTimeStamp = models.DateTimeField('TimeStamp In QuickFix log file.', null=False)
    RcvTime_SeqNum = models.CharField(max_length=64, primary_key=True) # just to avoid dups 
    BeginString = models.CharField(max_length=128,null=False)
    BodyLength = models.IntegerField(null=False)
    MsgType = models.CharField(max_length=4, null=False)
    SenderCompID = models.CharField(max_length=128,null=False)
    TargetCompID = models.CharField(max_length=128,null=False)
    MsgSeqNum = models.IntegerField(null=False)
    SendingTime = models.DateTimeField(null=False)
    CheckSum = models.IntegerField(null=False)
    text = models.TextField('actual data of fix message')
    xml =  models.TextField('XML form of fix message')
    
    def __str__(self):
        return self.RcvTime_SeqNum + ' 35 = ' + self.MsgType;
    
class NewOrderSingle(models.Model):
    fixMsg = models.OneToOneField(FixMsg)
    ClOrdID = models.CharField( primary_key=True, max_length=128,null=False)
    Side = models.CharField(max_length=1,null=False)
    TransactTime = models.DateTimeField(null=False)
    OrdType = models.CharField(max_length=1,null=False)
    PriceType = models.CharField(max_length=1)
    instrument = models.CharField(max_length=128,null=False)
    
class ExecutionReport(models.Model):
    fixMsg = models.OneToOneField(FixMsg)
    order = models.ForeignKey(NewOrderSingle)   
    OrderID = models.CharField(max_length=128,null=False)
    ExecID = models.CharField(primary_key=True, max_length=128,null=False)
    OrdStatus = models.CharField(max_length=1,null=False)
    
    
    