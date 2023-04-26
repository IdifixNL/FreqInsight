import tkinter as tk
from tkinter import messagebox
import os


def open_backtest_gui():
    backtest_file_path = "FreqInsight/backtest.py"
    if os.path.isfile(backtest_file_path):
        os.system(f"/usr/bin/python3 {backtest_file_path}")
    else:
        messagebox.showerror("Error", "Backtest file not found.")


def open_hyperopt_gui():
    hyperopt_file_path = "FreqInsight/hyperopt.py"
    if os.path.isfile(hyperopt_file_path):
        os.system(f"/usr/bin/python3 {hyperopt_file_path}")
    else:
        messagebox.showerror("Error", "Hyperopt file not found.")


def open_download_data_gui():
    download_data_file_path = "FreqInsight/downloaddata.py"
    if os.path.isfile(download_data_file_path):
        os.system(f"/usr/bin/python3 {download_data_file_path}")
    else:
        messagebox.showerror("Error", "Download data file not found.")


def open_config_gui():
    config_gui_file_path = "FreqInsight/config_gui.py"
    if os.path.isfile(config_gui_file_path):
        os.system(f"/usr/bin/python3 {config_gui_file_path}")
    else:
        messagebox.showerror("Error", "Config GUI file not found.")


# Check if config file exists, display warning if not
if not os.path.isfile("FreqInsight/config.py"):
    messagebox.showwarning("Warning", "Configuration file not found. Please run configuration first.")

root = tk.Tk()
root.title("Main Menu")

menu_frame = tk.Frame(root, padx=10, pady=10)
menu_frame.pack()

backtest_button = tk.Button(menu_frame, text="Backtest", command=open_backtest_gui)
backtest_button.pack()

hyperopt_button = tk.Button(menu_frame, text="Hyperopt", command=open_hyperopt_gui)
hyperopt_button.pack()

download_data_button = tk.Button(menu_frame, text="Download Data", command=open_download_data_gui)
download_data_button.pack()

config_button = tk.Button(menu_frame, text="Configuration", command=open_config_gui)
config_button.pack()

root.mainloop()