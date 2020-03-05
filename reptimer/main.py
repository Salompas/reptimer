#!/usr/bin/env python
import sys
import subprocess
import time


try:
    min, sec = sys.argv[1:]
except:
    with open("./doc.txt", "r") as doc:
        print(doc.read())
    sys.exit()

try:
    while True:
        time.sleep(int(min) * 60 + int(sec))
        subprocess.run(["afplay", "/System/Library/Sounds/Tink.aiff", "-v", "20"])
except KeyboardInterrupt:
    print("Stopping timer.")
