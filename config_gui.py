import tkinter as tk
import importlib
import os

def open_config_menu():
    config_menu = tk.Toplevel()
    config_menu.title("Configuration")

    # create a label and entry for the location variable
    location_label = tk.Label(config_menu, text="Data Location:")
    location_label.pack(side=tk.LEFT)
    location_entry = tk.Entry(config_menu, width=50)
    location_entry.insert(0, config.location)
    location_entry.pack(side=tk.LEFT)

    # create a label and entry for the strategy location variable
    strategy_label = tk.Label(config_menu, text="Strategies Path:")
    strategy_label.pack(side=tk.LEFT)
    strategy_entry = tk.Entry(config_menu, width=50)
    strategy_entry.insert(0, config.strategies_path)
    strategy_entry.pack(side=tk.LEFT)

    # create a button to save the new location and strategies_path values to the config file
    save_button = tk.Button(config_menu, text="Save", command=lambda: save_location(location_entry.get(), strategy_entry.get(), config_menu))
    save_button.pack()

def save_location(new_location, new_strategies_path, config_menu):
    config_path = "FreqInsight/config.py"

    # check if the config file exists
    if not os.path.isfile(config_path):
        # if the file doesn't exist, create it with default values
        with open(config_path, "w") as f:
            f.write("location = 'default_location'\n")
            f.write("strategies_path = 'default_strategies_path'\n")

    # write the new values to the config file
    with open(config_path, "w") as f:
        f.write(f"location = '{new_location}'\n")
        f.write(f"strategies_path = '{new_strategies_path}'\n")

    # reload the config module to use the new values of location and strategies_path
    importlib.reload(config)

    # destroy the configuration menu window
    config_menu.destroy()

# check if the config.py file exists and import it
if os.path.isfile("FreqInsight/freq-gui/config.py"):
    import config
else:
    # if the file doesn't exist, create it with default values and import it
    with open("FreqInsight/config.py", "w") as f:
        f.write("location = 'default_location'\n")
        f.write("strategies_path = 'default_strategies_path'\n")

    import config

root = tk.Tk()
root.withdraw()

# open the configuration menu on startup
open_config_menu()

root.mainloop()
