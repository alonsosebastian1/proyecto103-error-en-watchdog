import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import time
import random

from_dir ="C:/Users/alons/Downloads"
to_dir = "C:/Users/alons/Desktop/Archivos_Documentos"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"oye,{event.src_path}ha sido creado!")
    def on_deleted(self,event):
        print(f"Lo siento! alguien borro {event.src_path}")
event_handler = FileEventHandler()
observer = Observer()   
observer.schedule(event_handler,from_dir,recursive =True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("ejecutndo...")
except KeyboardInterrupt:
    print("detenido")
    observer.stop()