import tkinter as tk
import os
import subprocess
import config

def run_docker_command(days, intervals):
    intervals_str = " ".join([f"-t {i}" for i in intervals])
    command = f"docker-compose run freqtrade download-data --days {days} {intervals_str}"
    location = config.location
    os.chdir(location)
    subprocess.Popen(['xterm', '-e', command])

root = tk.Tk()
root.title("Data-downloader")
# create a label and entry for days input
days_label = tk.Label(root, text="Days:")
days_label.pack(side=tk.LEFT)
days_entry = tk.Entry(root)
days_entry.pack(side=tk.LEFT)

# create a checkbox for each interval
intervals = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "1d"]
interval_vars = [tk.BooleanVar() for _ in intervals]
for i, interval in enumerate(intervals):
    cb = tk.Checkbutton(root, text=interval, variable=interval_vars[i])
    cb.pack()

# create a button to start the download
button = tk.Button(root, text="Download Data", command=lambda: run_docker_command(days_entry.get(), [interval for interval, var in zip(intervals, interval_vars) if var.get()]))
button.pack()

root.mainloop()
