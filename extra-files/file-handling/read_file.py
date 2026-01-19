file = open('read.txt')

# full file read
print(file.read())

# it will read first 5 characters of file
print(file.read(5))

# read one single complete line at a time
print((file.readline()))

# read all data even with next line '\n'
# ['asd\n', 'cvd\n', 'qwe\n', 'rty\n', 'fgh\n', 'zxc\n', 'mkl']
print((file.readlines()))

# print whole file data one by one until it gets ""
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

# print all file line by line
# if we directly print file.readlines() it will print file data but in list format
for line in file.readlines():
    print(line)

# close file
file.close()
