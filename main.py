import subprocess

import schedule
import time


def job():
    subprocess.check_call(['speedtest-cli', '--csv', '>>', 'output.log'])

schedule.every(20).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(30)
