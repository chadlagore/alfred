import subprocess

import schedule
import time
import os

def job():
    os.system('speedtest-cli --csv >> /home/ubuntu/alfred/output.log')

schedule.every(60).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
