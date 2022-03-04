#!/usr/bin/python3
import shutil,sys
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("usage :cp.py <source> <destination>")
        exit(1)
    print(sys.argv)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    shutil.copy(src,dst)

if __name__ == '__main__':
    main()