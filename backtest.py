import tkinter as tk
import subprocess
import os
import config

def run_backtest():
    location = config.location
    intervals = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "1d"]
    selected_intervals = [interval for interval, var in zip(intervals, interval_vars) if var.get()]
    intervals_str = " ".join([f"--timeframe {interval}" for interval in selected_intervals])
    strategy = strategy_var.get()
    command = f"docker-compose run --rm -v {location}:/freqtrade/user_data freqtrade backtesting --strategy {strategy} --timerange=20230101- {intervals_str}"
    os.chdir(location)
    subprocess.Popen(['xterm', '-hold', '-e', command])

root = tk.Tk()
root.title("Backtest")

backtest_frame = tk.Frame(root, padx=10, pady=10)
backtest_frame.pack()

interval_frame = tk.Frame(root, padx=10, pady=10)
interval_frame.pack()

strategy_frame = tk.Frame(root, padx=10, pady=10)
strategy_frame.pack()

backtest_button = tk.Button(backtest_frame, text="Run Backtest", command=run_backtest)
backtest_button.pack()

intervals = ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "1d"]
interval_vars = [tk.BooleanVar() for _ in intervals]
for i, interval in enumerate(intervals):
    cb = tk.Checkbutton(interval_frame, text=interval, variable=interval_vars[i])
    cb.pack(side=tk.LEFT)

strategies_path = "/home/nico/Documents/projects/trader/dev-freq/ft_userdata/user_data/strategies"
strategies = os.listdir(strategies_path)
strategy_var = tk.StringVar()
strategy_var.set(strategies[0])
strategy_dropdown = tk.OptionMenu(strategy_frame, strategy_var, *strategies)
strategy_dropdown.pack()

root.mainloop()
