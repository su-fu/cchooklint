import sys

if "rm -rf" in sys.argv:
    sys.exit(2)  # block dangerous commands
