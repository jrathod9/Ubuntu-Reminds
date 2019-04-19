import sys
import Tkinter as tk
import tkMessageBox
from decimal import Decimal
# for arg in sys.argv:
    # print(arg)
# print(sys.argv[1])
time = Decimal(sys.argv[1])
print(time)
root = tk.Tk()
root.withdraw()
alert = "Ubuntu Reminds"
tkMessageBox.showwarning(alert, 'ITS TIME')
