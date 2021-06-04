def reverse_slicing(s):
    return s[::-1]

textfile = open("file.txt")
lines = textfile.readlines()
for line in lines:
    print(reverse_slicing(line))