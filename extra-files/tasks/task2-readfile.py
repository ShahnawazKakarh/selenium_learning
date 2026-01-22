file = open('file1.txt')

for line in file.readlines():
    print(line.strip())

file.close()
