import argparse
import time

def secwait(sec):
    sec = int(sec)
    for i in range(0, sec):
      time.sleep(1)
      print(i+1, "seconds.")

def arginit():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--second", help="Seconds to print.")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    # if used by script call, not as module
    print("Arg Parser test code")
    args = arginit()
    if args.second:
        secwait(args.second)