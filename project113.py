import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time


from_dir = r"C:/Users/krishashah/Downloads"
to_dir = r"C:/Users/krishashah/Desktop" 

class FileEvents_BluePrint(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!" )
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")
    def on_modified(self, event):
        print(f"Hey there!, {event.src_path} has been modified")
    def on_moved(self, event):
        print(f"Someone moved {event.src_path} tp {event.dest_path}")


myevent = FileEvents_BluePrint()

#Initialise the observer
myobserver = Observer()
myobserver.schedule(event_handler = myevent, path = from_dir, recursive = True)

myobserver.start()
try: 
    while(True):
        print("running")
        time.sleep(1)
except KeyboardInterrupt:
    print("stopped")
    myobserver.stop() 