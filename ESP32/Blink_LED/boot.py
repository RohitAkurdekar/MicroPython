#Test
print("boot")

# write data in a file.
file1 = open("myfile.txt","w")

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.write(__name__)
file1.write("\n")
file1.close() #to change file access modes
 