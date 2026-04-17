import os
from datetime import datetime

# This defines exactly where we are
base_path = r"C:\Local-SIEM-Lab"
log_dir = os.path.join(base_path, "logs")
log_file = os.path.join(log_dir, "security_audit.log")

# STEP 1: Force the folder to exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    print(f"Created directory: {log_dir}")

# STEP 2: Try to write
try:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, "a") as f:
        f.write(f"{timestamp} | user=admin | status=FAILURE | ip=1.1.1.1\n")
    print(f"SUCCESS! File written to: {log_file}")
except Exception as e:
    print(f"ERROR: Could not write file. Reason: {e}")