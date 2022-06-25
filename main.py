
import platform
import psutil
import tkinter as tk
from tkinter import ttk
import psutil
import platform
import socket
import uuid
import re

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title('Hardware and Software Analyzer')

        window_w = 600
        window_h = 400

        screen_w = self.winfo_screenmmwidth()
        screen_h = self.winfo_screenmmheight()

        center_x = int(screen_w)
        center_y = int(screen_h)

        self.geometry(f'{window_w}x{window_h}+{center_x}+{center_y}')

    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def System():
        system_data = {
            "Network name " : platform.node(),
            "Operating system" : platform.system(),
            "Version" : platform.version(),
            "Machine" : platform.machine(),
            "Architecture" : platform.architecture(),
            "Ip-Address" : socket.gethostbyname(socket.gethostname()),
            "Mac-Address" : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}
        }
        print(system_data)

    def CPU():
        cpufreq = psutil.cpu_freq()
        cpu_data = {
            "Physical cores" : psutil.cpu_count(logical=False),
            "Total cores" : psutil.cpu_count(logical=True),
            "Max Frequency" : f"{cpufreq.max:.2f}Mhz",
            "Min Frequency" : f"{cpufreq.min:.2f}Mhz",
            "Current Frequency" : f"{cpufreq.current:.2f}Mhz",
            "Total CPU Usage" : f"{psutil.cpu_percent()}%"
        }
        print(cpu_data)

    def RAM():
        svmem = psutil.virtual_memory()
        ram_data = {
            "Total" : get_size(svmem.total),
            "Available" : get_size(svmem.available),
            "Used" : get_size(svmem.used),
            "Percentage" : f"{svmem.percent}%"
        }
        print(ram_data)

    def DISK():
        partitions = psutil.disk_partitions()
        pass

    def GPU():
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()