import platform
import psutil
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title('Hardware and Software Analyzer')
        # window size
        window_w = 600
        window_h = 400

        # get the screen dimension
        screen_w = self.winfo_screenmmwidth()
        screen_h = self.winfo_screenmmheight()

        # find center point
        center_x = int(screen_w)
        center_y = int(screen_h)

        #size and position of a window
        self.geometry(f'{window_w}x{window_h}+{center_x}+{center_y}')

        # initialize data
        self.options = ('System', 'CPU', 'GPU', 'RAM', 'Drives')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self)
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.options[0],
            *self.options)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

    def sysinfo():
        system_info = {
            "Operating system" : platform.system(),
            "Network name " : platform.node(),
            "Architecture name" : platform.architecture()
        }
        return system_info



if __name__ == "__main__":
    app = App()
    app.mainloop()