# r means read only file mode
# w means user can write in the file
with open('ibrahim.txt', 'w') as file:
    file.write('IBRAHIM')
    file.write('KHAN')

with open('file.txt', 'r') as reader:
    # [abc, bvdsf, cat, dog, elephant]
    content = reader.readlines()

    # [elephant, dog, cat, bvdsf, abc]
    reversed(content)

    with open('test.txt', 'w') as writer:
        for line in content:
            writer.writelines(content)
            print(content)

    with open('learn.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
