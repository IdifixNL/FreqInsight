import subprocess

def run_backtest():
    result = subprocess.run(['docker-compose', 'up', '-d'], capture_output=True)
    if result.returncode == 0:
        return 'Started'
    else:
        return f'Error: {result.stderr.decode("utf-8")}'

def run_test():
    return 'This is a test message.'
