import os

file = 'test_8.py'

if not os.path.exists(file):
    print("No such file")

location = r'C:\Users\AdminPC\Desktop\pp2_spring'

path = os.path.join(location, file)

os.remove(path)