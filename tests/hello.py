import sys

print('Hello world') # Stdout only printed when Failed

try:
    1/2
except Exception as e:
    sys.exit(e)


