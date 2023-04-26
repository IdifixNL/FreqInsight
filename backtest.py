import tkinter as tk
from tkinter import ttk
import subprocess
import os
import re
import config

def run_backtest():
    location = config.location
    intervals = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "1d"]
    selected_intervals = [interval for interval, var in zip(intervals, interval_vars) if var.get()]
    intervals_str = " ".join([f"--timeframe {interval}" for interval in selected_intervals])
    strategy = strategy_var.get()
    timerange = timerange_entry.get() + "-"
    command = f"docker-compose run --rm -v {location}:/freqtrade/user_data freqtrade backtesting --strategy {strategy} --timerange={timerange} {intervals_str}"
    os.chdir(location)
    subprocess.Popen(['xterm', '-hold', '-e', command])

def get_available_strategies():
    strategies_path = config.strategies_path
    strategy_files = os.listdir(strategies_path)
    available_strategies = []
    for file in strategy_files:
        with open(os.path.join(strategies_path, file), 'r') as f:
            content = f.read()
            match = re.search(r'class\s+(.*?)\s*\(\s*IStrategy', content)
            if match:
                strategy_name = match.group(1)
                available_strategies.append(strategy_name)
    return available_strategies

root = tk.Tk()
root.title("Backtest")

backtest_frame = tk.Frame(root, padx=10, pady=10)
backtest_frame.pack()

interval_frame = tk.Frame(root, padx=10, pady=10)
interval_frame.pack()

strategy_frame = tk.Frame(root, padx=10, pady=10)
strategy_frame.pack()

timerange_frame = tk.Frame(root, padx=10, pady=10)
timerange_frame.pack()

backtest_button = tk.Button(backtest_frame, text="Run Backtest", command=run_backtest)
backtest_button.pack()

intervals = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "1d"]
interval_vars = [tk.BooleanVar() for _ in intervals]
for i, interval in enumerate(intervals):
    cb = tk.Checkbutton(interval_frame, text=interval, variable=interval_vars[i])
    cb.pack(side=tk.LEFT)

strategy_options = get_available_strategies()
strategy_var = tk.StringVar()
strategy_var.set(strategy_options[0])
strategy_dropdown = ttk.OptionMenu(strategy_frame, strategy_var, strategy_options[0], *strategy_options)
strategy_dropdown.pack()

timerange_label = tk.Label(timerange_frame, text="Timerange")
timerange_label.pack(side=tk.LEFT)

timerange_entry = tk.Entry(timerange_frame, width=20)
timerange_entry.pack(side=tk.LEFT)

root.mainloop()
