import sys
import Tkinter as tk
import tkMessageBox
import time
from decimal import Decimal

start_time = time.time()

time_period = Decimal(sys.argv[1])*60*60
# print(time_period)

alert_message = []
for arg in sys.argv:
    alert_message.append(arg)
alert_message = alert_message[2:]
print(alert_message)
count = 0

while True:
    now_time = time.time()
    if (int(now_time - start_time) % int(time_period) == 0 and count == 0):
        root = tk.Tk()
        root.withdraw()
        tkMessageBox.showwarning("Ubuntu Reminds", alert_message)
    else:
        count = 0
    # tm_year=2019, tm_mon=4, tm_mday=19, tm_hour=15, tm_min=35, tm_sec=7, tm_wday=4, tm_yday=109, tm_isdst=-1
