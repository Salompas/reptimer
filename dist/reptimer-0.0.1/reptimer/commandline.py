import sys
import reptimer


def main():
    try:
        minutes, seconds = sys.argv[1:]
    except:
        with open("./doc.txt", "r") as doc:
            print(doc.read())
        sys.exit()

    try:
        reptimer.timer(int(minutes) * 60 + int(seconds))
    except KeyboardInterrupt:
        print("Stopping timer.")
