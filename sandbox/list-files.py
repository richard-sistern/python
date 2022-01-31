import os, time

# Use 'r' to ignore slashes
path = r"c:\temp"
now = time.time()

for f in os.listdir(path):
    # Join path and file
    filename = os.path.join(path, f)
    
    if os.path.isfile(filename):
        print(filename)