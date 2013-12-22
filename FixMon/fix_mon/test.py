'''
Created on Dec 8, 2013

@author: ashish
'''

from logReader import  FixLogReader
from fixmon.models import Config
from FixMon import settings

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/../')

os.environ['DJANGO_SETTINGS_MODULE']='FixMon.settings'




lr = FixLogReader(logfile='/home/ashish/Downloads/Banzai/test.data')
lr.readAll()
