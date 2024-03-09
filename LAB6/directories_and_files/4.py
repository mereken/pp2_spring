
def file_length(file):
        with open(file) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_length("test.txt"))
