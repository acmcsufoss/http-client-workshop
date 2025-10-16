import sys
import requests

# Optional error checking
if len(sys.argv) != 2:
    print("Error: expected one argument")
    sys.exit(1)

# Read pokemon from command line args
pokemon = sys.argv[1]

print(f"Name: {pokemon}")
