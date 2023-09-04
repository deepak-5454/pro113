import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define a custom event handler by subclassing FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified.')

    def on_created(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been created.')

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been deleted.')

    def on_moved(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been moved to {event.dest_path}.')

# Create an observer and point it to the directory you want to watch
path = "/path/to/your/directory"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)

# Start watching for file system events
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the observer when the user presses Ctrl+C
    observer.stop()

# Wait for the observer to finish
observer.join()
