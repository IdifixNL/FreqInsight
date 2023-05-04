import os
from flask import render_template, request
from backtest import run_backtest


def index():
    return render_template('index.html')

def run_backtest_route():
    # get the form data from the request object
    strategy = request.form.get('strategy')
    dry_run_wallet = request.form.get('dry_run_wallet')
    timeframe = request.form.get('timeframe')
    timerange = request.form.get('timerange')

    # run the backtest using the form data
    result = run_backtest(strategy, dry_run_wallet, timeframe, timerange)

    return render_template('result.html', result=result)
