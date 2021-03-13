#!/usr/bin/env python3

import os
import subprocess
import sys
import time
from datetime import datetime

SHELL_COMMAND = "ffmpeg -hide_banner -loglevel error -f v4l2 -r 25 -s 640x480 -i /dev/video0 -t 3600 /opt/recorder/output/recorder_CURRENTTIME.avi"

def main():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print("{now} Recorder Python script main function".format(now=now))
    while True:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        print("{now} Recorder Python script main function".format(now=now))
        command = SHELL_COMMAND.replace("CURRENTTIME", now)
        print("{now} Command: {command}".format(now=now, command=command))
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        try:
            output, error = process.communicate(timeout=3600)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            print("{now} Ended executing process".format(now=now))
        except subprocess.TimeoutExpired:
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            print("{now} Timeout of 1 hour expired. Continue with new execution.".format(now=now))
            pass
        except Exception as exception:
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            print("{now} Raised Exception: {exception}".format(exception=exception))
            sys.exit()


if __name__ == "__main__":
    main()
