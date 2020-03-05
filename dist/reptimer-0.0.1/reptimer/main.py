#!/usr/bin/env python
import subprocess
import time


def timer(seconds):
    time.sleep(seconds)
    subprocess.run(["afplay", "/System/Library/Sounds/Tink.aiff", "-v", "20"])
