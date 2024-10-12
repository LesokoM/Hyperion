f = open("example.txt", 'r+')

# ************ Example 2 ************
print("\nExample 2: ")
for line in f:
        print("The first character of this line is: " + line[0] + "\n")
        print("The entire line is: " + line)

f.close()


# ************ Example 3 ************
# We could build up all lines of the text file into a large string called contents as follows:

print("\nExample 3: ")
contents = ""
with open('PART 10\example.txt', 'r+') as f: # Open the file again!
        for line in f:
                contents = contents + line


print(contents)


# ************ Example 4 ************
print("\nExample 4: ")

f = open('PART 10\example.txt','r+', encoding='utf-8') # Open the file again!
# Notice in the code above how we pass an extra optional arugment through to the open function.
# This arguments specifies the encoding of the file.
newContents = f.read()
print(newContents)

f.close() # Always close files when done with them.