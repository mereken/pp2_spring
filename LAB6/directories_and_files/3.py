import os

path = r'c:\Users\AdminPC\Desktop\pp2_spring'

if os.path.exists(path):
    print("The path exists.")
    print("Filename:", os.path.basename(path))
    print("Directory portion:", os.path.dirname(path))
else:
    print("The path does not exist.")
