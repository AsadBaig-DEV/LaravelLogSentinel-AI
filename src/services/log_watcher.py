import time
import os
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LogHandler(FileSystemEventHandler):
  def __init__(self, log_dir):
    self.log_dir = Path(log_dir)
    self.last_position = 0
    self.current_log_file = self._get_today_log_path()

    if self.current_log_file.exists():
      self.last_position = self.current_log_file.stat().st_size

  def _get_today_log_path(self):
    """Calculates the filename based on DD-MM-YYYY format"""
    today_str = datetime.now().strftime("%d-%m-%Y")
    return self.log_dir / f"{today_str}.log"
  
  def on_modified(self, event):
    today_log = self._get_today_log_path()

    if not event.is_directory and Path(event.src_path) == today_log:
      self._process_new_entries(today_log)

  def _process_new_entries(self, file_path):
    """Reads only the newly appended line form the log."""
    with open(file_path, 'r') as f:
      f.seek(self.last_position)
      new_data = f.read()
      self.last_position = f.tell()

      if new_data.strip():
        print(f"\n [New Log Entry] at {datetime.now().strftime('%H:%M:%S')}")
        print(f"--- Content Start ---\n {new_data.strip()}\n--- Content End ---")

class LogWatcher:
  def __init__(self, directory_to_watch):
    self.directory = directory_to_watch
    self.event_handler = LogHandler(self.directory)
    self.observer = Observer()

  def start(self):
    self.observer.schedule(self.event_handler, self.directory, recursive=False)
    self.observer.start()
    print(f"Watching {self.directory} for new log entries...")

    try:
      while True:
        time.sleep(1)
    except KeyboardInterrupt:
      self.observer.stop()
    self.observer.join()

if __name__ == "__main__":

  LOGS_PATH = "./laravel-logs"
  if not os.path.exists(LOGS_PATH):
    os.makedirs(LOGS_PATH)

  watcher = LogWatcher(LOGS_PATH)
  watcher.start()