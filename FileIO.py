outfile = open("Test.txt", "w")
outfile.write("Test")
outfile.close()
# opens file in write mode and automatically closes it in one statement
with open("test1.txt", "w") as outfile:
    outfile.write("This is a test, this is a test")

# opens file in read mode and automatically closes it in one statement
with open("test1.txt", "r") as infile:
    print(infile.readline())

# write one line to a text file
with open("Test.txt", "w") as file:
    file.write("John Cleese\t")
with open("Test.txt", "r") as infile:
    print(infile.readline())

# append one line to a text file
with open("Test.txt", "a") as file:
    file.write("John Cleese1\t")
with open("Test.txt", "r") as infile:
    print(infile.read())

#read entire file as a list
with open("Test.txt") as file:
    members = file.readlines();
    print(members)
    for member in members:
        print(member)

#write list to a file
strings = ["Eric Idle", "Eric Idle1", "Eric Idle2"]
with open("Test.txt", "w") as str_file:
    for string in strings:
        str_file.write(string +"\t")


