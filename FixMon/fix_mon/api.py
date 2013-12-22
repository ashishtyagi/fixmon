'''
Created on Dec 8, 2013

@author: ashish
'''

from tastypie.resources import ModelResource
from fixmon.models import FixMsg, ColumnConfig

class ColumnConfigResource(ModelResource):
    class Meta:
        queryset = ColumnConfig.objects.all();
        resource_name = 'column'

class FixMsgResource(ModelResource):
    class Meta:
        queryset = FixMsg.objects.all()
        resource_name = 'fixMsg'