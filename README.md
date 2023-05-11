# Disclaimer
 
 FreqInsight is provided under the MIT License and comes with no warranty or guarantee of any kind. The user assumes all responsibility for the usage of this software and the results obtained from it. Always backtest your trading strategies thoroughly before using them with real money.


This application is under development active development

# FreqInsight

Currently moved over to Flask framework

FreqInsight is a project that provides a GUI for running FreqTrade commands 

See here what current status is of the parts that being developt

Datadownload  Currently under construction
Backtest            :Planned
Hyperopt            :planned
Scheduler for tasks :Planned


## Table of Contents

* [Disclaimer](#disclaimer)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)


## Requirements

To use FreqInsight, you will need the following:

* FreqTrade running in Docker on your system. If you haven't set up FreqTrade in Docker yet, you can follow the installation instructions in the official documentation: [FreqTrade Docker Quickstart](https://www.freqtrade.io/en/stable/docker_quickstart/)

* Python 3.6 or higher

* The following Python package:
  - `docker`
  - `flask`

You can install the `docker` package using `pip` by running the following command:

pip install docker flask



Make sure to run this command in a terminal window with administrator or superuser privileges to ensure that the packages are installed system-wide.

## Installation

To install and use FreqInsight, follow these steps:

1. Clone the FreqInsight repository to your local machine by running the following command:
   git clone https://github.com/IdifixNL/FreqInsight.git



## Usage

1. Open a terminal

2. Navigate to the FreqInsight directory.

3. Start the app with command from inside a terminal "python3 app.py" to start the Flask application.

4. Open a web browser and go to `http://localhost:5000` to access FreqInsight.

5. Go to Configuration from the top menu bar

6. Fill in User Data Path from where your Freqtrade docker location and press Save


## Contributing

Contributions to FreqInsight are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [FreqInsight GitHub repository](https://github.com/IdifixNL/FreqInsight).

## License

FreqInsight is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
