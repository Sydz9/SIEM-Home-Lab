import os
from datetime import datetime

base_path = r"C:\Local-SIEM-Lab"
log_dir = os.path.join(base_path, "logs")
log_file = os.path.join(log_dir, "security_audit.log")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    print(f"Created directory: {log_dir}")

try:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, "a") as f:
        f.write(f"{timestamp} | user=admin | status=FAILURE | ip=1.1.1.1\n")
    print(f"SUCCESS! File written to: {log_file}")
except Exception as e:
    print(f"ERROR: Could not write file. Reason: {e}")
