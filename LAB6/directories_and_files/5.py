color = ['Purple', 'Blue', 'Pink', 'Black', 'Green', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())
