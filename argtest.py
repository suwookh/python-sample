import argparse

def arginit():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--dir", help="Director Name", required=True)
  args = parser.parse_args()
  return args

if __name__ == "__main__":
  # if used by script call, not as module
  print("Arg Parser test code")
  args = arginit()
  if args.dir:
    print(args.dir)