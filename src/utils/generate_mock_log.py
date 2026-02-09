import os
import random
from datetime import datetime
from pathlib import Path

# Professional Laravel Error Templates
ERROR_TEMPLATES = [
    {
        "level": "ERROR",
        "message": "Column not found: 1054 Unknown column 'user_id' in 'field list'",
        "trace": "at /var/www/html/vendor/laravel/framework/src/Illuminate/Database/Connection.php:671"
    },
    {
        "level": "CRITICAL",
        "message": "Maximum execution time of 30 seconds exceeded",
        "trace": "at /var/www/html/app/Http/Controllers/ReportController.php:142"
    },
    {
        "level": "ERROR",
        "message": "Call to a member function getClientOriginalExtension() on null",
        "trace": "at /var/www/html/app/Http/Controllers/InsuranceController.php:89"
    }
]

def generate_daily_mock_log():
    # 1. Create logs directory if it doesn't exist
    log_dir = Path("laravel-logs")
    log_dir.mkdir(exist_ok=True)

    # 2. Get today's filename (09-02-2026.log)
    today_str = datetime.now().strftime("%d-%m-%Y")
    file_path = log_dir / f"{today_str}.log"

    # 3. Create a realistic Laravel log entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error = random.choice(ERROR_TEMPLATES)
    
    log_entry = (
        f"[{timestamp}] local.{error['level']}: {error['message']} \n"
        f"Stack trace:\n#0 {error['trace']}\n"
        f"#1 /var/www/html/public/index.php(55): Illuminate\\Foundation\\Http\\Kernel->handle(Object(Illuminate\\Http\\Request))\n"
        f"{'-'*50}\n"
    )

    # 4. Append to today's log file
    with open(file_path, "a") as f:
        f.write(log_entry)
    
    print(f"Mock log entry added to: {file_path}")

if __name__ == "__main__":
    generate_daily_mock_log()