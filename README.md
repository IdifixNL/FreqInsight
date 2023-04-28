# Disclaimer
 
 FreqInsight is provided under the MIT License and comes with no warranty or guarantee of any kind. The user assumes all responsibility for the usage of this software and the results obtained from it. Always backtest your trading strategies thoroughly before using them with real money.


# FreqInsight

FreqInsight is a project that provides a GUI for running FreqTrade commands in Docker.

## Table of Contents

* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Requirements

To use FreqInsight, you will need the following:

* FreqTrade running in Docker on your system. If you haven't set up FreqTrade in Docker yet, you can follow the installation instructions in the official documentation: https://www.freqtrade.io/en/stable/docker_quickstart/

* Python 3.6 or higher

* The following Python packages:

  * `docker`
  
  * `numpy`
  
  * `pandas`
  
  * `matplotlib`
  
  * `tkinter`

You can install these packages using `pip` by running the following command:

Make sure to run this command in a terminal window with administrator or superuser privileges to ensure that the packages are installed system-wide.

## Installation

To install and use FreqInsight, follow these steps:

1. Clone the FreqInsight repository to your local machine by running the following command:
   "git clone https://github.com/IdifixNL/FreqInsight.git"

2. Navigate to the FreqInsight directory and run `menu.py` to start the GUI:


3. If this is your first time running FreqInsight, you will see a warning message that the configuration file was not found. Click "OK" to close the message.

4. Next, click the "Configuration" button to open the configuration menu. In the configuration menu, fill in the following information:

* **Location**: The path to the directory where your FreqTrade user data is located. For example, if your FreqTrade user data is located in `/home/user/freqtrade/user_data`, enter `/home/user/freqtrade` as the location.

* **Strategies Path**: The path to the directory where your FreqTrade strategy files are located. For example, if your FreqTrade strategy files are located in `/home/user/freqtrade/strategies`, enter `/home/user/freqtrade/strategies` as the strategies path.

5. Once you have filled in the required information, click "Save" to save the configuration file and close the configuration menu.

6. You are now ready to use FreqInsight 

That's it! If you encounter any issues or have any questions, please refer to the project's GitHub issues page or documentation for assistance. https://github.com/IdifixNL/FreqInsight/issues




