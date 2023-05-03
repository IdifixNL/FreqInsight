import tkinter as tk
from tkinter import ttk
import subprocess
import os
import re
import config
import json


def run_hyperopt():
    location = config.location
    strategy = strategy_var.get()
    spaces = " ".join([name for name, var in space_vars.items() if var.get()])
    epochs = epochs_entry.get()
    timeframe = timeframe_var.get()
    hyperopt_loss = hyperopt_loss_var.get()
    timerange = timerange_entry.get() + "-"
    cpu = cpu_entry.get()
    coin_pair = coin_pairs_var.get()
    command = f"docker-compose run --rm -v {location}:/freqtrade/user_data freqtrade hyperopt --strategy {strategy} --spaces {spaces} -e {epochs} --timeframe {timeframe} --hyperopt-loss {hyperopt_loss} --timerange {timerange} -j {cpu} --pairs {coin_pair}"
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


config_path = config.config_location

def read_config_data(config_path):
    with open(config_path, "r") as file:
        config_data = json.load(file)
    return config_data

config_data = read_config_data(config_path)


def get_coin_pairs():
    pair_whitelist = config_data["exchange"]["pair_whitelist"]
    return pair_whitelist

def init_coin_pairs_dropdown(frame, coin_pairs):
    coin_pairs_label = tk.Label(frame, text="Select a coin pair:")
    coin_pairs_label.pack(side=tk.LEFT)

    coin_pairs_var = tk.StringVar()
    coin_pairs_dropdown = ttk.Combobox(frame, textvariable=coin_pairs_var, values=coin_pairs)
    coin_pairs_dropdown.pack(side=tk.LEFT)

    return coin_pairs_var



# Get coin pairs from the config_data variable
coin_pairs = get_coin_pairs()

# Create the main window and initialize the dropdown menu
root = tk.Tk()
root.title("Hyperopt")

coin_pairs_frame = tk.Frame(root, padx=10, pady=10)
coin_pairs_frame.pack()
coin_pairs_var = init_coin_pairs_dropdown(coin_pairs_frame, coin_pairs)

strategy_frame = tk.Frame(root, padx=10, pady=10)
strategy_frame.pack()


root.title("Hyperopt")

strategy_frame = tk.Frame(root, padx=10, pady=10)
strategy_frame.pack()

timeframe_frame = tk.Frame(root, padx=10, pady=10)
timeframe_frame.pack()

timerange_frame = tk.Frame(root, padx=10, pady=10)
timerange_frame.pack()

epochs_frame = tk.Frame(root, padx=10, pady=10)
epochs_frame.pack()

cpu_frame = tk.Frame(root, padx=10, pady=10)
cpu_frame.pack()

hyperopt_loss_frame = tk.Frame(root, padx=10, pady=10)
hyperopt_loss_frame.pack()

spaces_frame = tk.Frame(root, padx=10, pady=10)
spaces_frame.pack()

strategy_label = tk.Label(strategy_frame, text="Strategy")
strategy_label.pack(side=tk.LEFT)

strategy_options = get_available_strategies()
strategy_var = tk.StringVar(root)
strategy_var.set(strategy_options[0])
strategy_dropdown = tk.OptionMenu(strategy_frame, strategy_var, *strategy_options)
strategy_dropdown.pack(side=tk.LEFT)

timeframe_label = tk.Label(timeframe_frame, text="Timeframe")
timeframe_label.pack(side=tk.LEFT)

timeframe_options = ["1m", "3m", "5m", "15m", "30m", "1h", "4h", "1d"]
timeframe_var = tk.StringVar(root)
timeframe_var.set(timeframe_options[0])
timeframe_dropdown = ttk.OptionMenu(timeframe_frame, timeframe_var, *timeframe_options)
timeframe_dropdown.pack(side=tk.LEFT)

timerange_label = tk.Label(timerange_frame, text="Timerange")
timerange_label.pack(side=tk.LEFT)

timerange_entry = tk.Entry(timerange_frame, width=20)
timerange_entry.pack(side=tk.LEFT)

epochs_label = tk.Label(epochs_frame, text="Epochs")
epochs_label.pack(side=tk.LEFT)

epochs_entry = tk.Entry(epochs_frame, width=20)
epochs_entry.pack(side=tk.LEFT)

cpu_label = tk.Label(cpu_frame, text="Number of CPUs")
cpu_label.pack(side=tk.LEFT)

cpu_entry = tk.Scale(cpu_frame, from_=1, to=16, orient=tk.HORIZONTAL, length=200)
cpu_entry.pack(side=tk.LEFT)

hyperopt_loss_label = tk.Label(hyperopt_loss_frame, text="Hyperopt Loss")
hyperopt_loss_label.pack(side=tk.LEFT)

hyperopt_loss_options = [
    "SharpeHyperOptLoss",
    "SortinoHyperOptLoss",
    "CalmarHyperOptLoss",
    "ProfitDrawDownHyperOptLoss",
    "SharpeHyperOptLossDaily",
    "SortinoHyperOptLossDaily",
    "MaxDrawDownHyperOptLoss",
    "MaxDrawDownRelativeHyperOptLoss",
    "OnlyProfitHyperOptLoss",
    "ShortTradeDurHyperOptLoss",
]

hyperopt_loss_var = tk.StringVar(root)
hyperopt_loss_var.set(hyperopt_loss_options[0])

hyperopt_loss_dropdown = ttk.OptionMenu(hyperopt_loss_frame, hyperopt_loss_var, *hyperopt_loss_options)
hyperopt_loss_dropdown.pack(side=tk.LEFT)

spaces_label = tk.Label(spaces_frame, text="Spaces")
spaces_label.pack(side=tk.LEFT)

space_names = ["all", "buy", "sell", "roi", "stoploss", "trailing", "protection", "trades", "default"]
space_vars = {name: tk.BooleanVar() for name in space_names}
for name in space_names:
    space_var = space_vars[name]
    space_checkbox = tk.Checkbutton(spaces_frame, text=name, variable=space_var)
    space_checkbox.pack(side=tk.LEFT)


hyperopt_button = tk.Button(root, text="Run Hyperopt", command=run_hyperopt)
hyperopt_button.pack()

root.mainloop()