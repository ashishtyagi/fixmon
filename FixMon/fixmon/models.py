from django.db import models



class Config(models.Model):
    KEYS = (
        ('FixLogDir', 'FixLogDir'),
        ('BackDays', 'BackDays'),
    )
    key = models.CharField(max_length=50, primary_key=True, choices=KEYS)
    value = models.CharField()

class FixMsg(models.Model):
    receivedTimeStamp = models.DateTimeField('TimeStamp In QuickFix log file.', null=False)
    beginString = models.CharField(null=False)
    bodyLength = models.IntegerField(null=False)
    msgType = models.IntegerField(null=False)
    senderCompID = models.CharField(null=False)
    targetCompID = models.CharField(null=False)
    msgSeqNum = models.IntegerField(null=False)
    sendingTime = models.DateTimeField(null=False)
    text = models.CharField(null=False)
    xml =  models.CharField(null=False)
    
