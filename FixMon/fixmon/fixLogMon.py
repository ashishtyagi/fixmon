'''
Created on Dec 5, 2013

@author: ashish
'''

import sys, os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class FixLogMonitor(PatternMatchingEventHandler):
    observer = {}
    def __init__(self, logdir=None, patterns=None):
        super(FixLogMonitor, self).__init__(patterns=patterns, ignore_directories=True, case_sensitive=True)
        self.observer = Observer()
        self.observer.schedule(self, logdir, recursive=False)
         
    def start(self):
        self.observer.start()
        
    def join(self, timeout=None):
        self.observer.join(timeout)
    
    def on_moved(self, event):
        super(FixLogMonitor, self).on_moved(event)
    
        what = 'directory' if event.is_directory else 'file'
        logging.info("Moved %s: from %s to %s", what, event.src_path,
                     event.dest_path)
    
    def on_created(self, event):
        super(FixLogMonitor, self).on_created(event)
    
        what = 'directory' if event.is_directory else 'file'
        logging.info("Created %s: %s", what, event.src_path)
   
    def on_modified(self, event):
        super(FixLogMonitor, self).on_modified(event)
        
        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)
