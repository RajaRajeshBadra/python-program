#read, write, readline, writeline, open and close functions implemented
# sourcery skip: ensure-file-closed
Names = open("Names.txt", "w")  #create text file Names.txt
Names.write("Rajesh\n")
Names.write("Temp\n")
Names.close()

Names = open("Names.txt", "r")
print(Names.read())
Names.close()

Names = open("Names.txt", "a")
Names.writelines(["Hello! ", "are you fine?"])
Names.close()

Names = open("Names.txt", "r")
print(Names.read())
Names.close()

Names = open("Names.txt","r")
print(Names.readline())