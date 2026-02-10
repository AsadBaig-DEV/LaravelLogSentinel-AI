import os
from services.log_watcher import LogWatcher

def run_sentinel():
  LOGS_TO_WATCH = "./laravel-logs"

  if not os.path.exists(LOGS_TO_WATCH):
    os.makedirs(LOGS_TO_WATCH)
    print(f"Created {LOGS_TO_WATCH} directory for log files.")

  print(f"LaravelLogsentinel-AI is watching {LOGS_TO_WATCH} for new log entries...")
  watcher = LogWatcher(LOGS_TO_WATCH)
  watcher.start()

if __name__ == "__main__":
  run_sentinel()