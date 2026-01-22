'''
Objective: Count and print the number of lines in a file.
Instructions:
Use the attached text file "file1.txt"
Write a Python script that opens the file, reads through it line by line, counts how many lines it has,
and prints the total count.
Expected result:
Total number of lines: 5
'''

file = open("file1.txt", "r")
lines = file.readlines()
print(len(lines))

'''**************************************'''
'''OR ANOTHER WAY TO SOLVE IT'''
'''**************************************'''

count = 0

with open("file1.txt", "r") as file:
    for line in file:
        count += 1

print("Total number of lines:", count)
