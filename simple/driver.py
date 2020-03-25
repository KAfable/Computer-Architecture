import sys

if len(sys.argv) != 2:
    print("usage: driver.py filename")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename) as f:
        for line in f:
            # ignore comments
            comment_split = line.split("#")
            # strip out whitesapec
            num = comment_split[0].strip()
            # ignore blank lines
            if num == '':
                # what does continue do?
                continue
            val = int(num, 2)
            print(val)

except FileNotFoundError:
    print("File not found")
    sys.exit(2)
