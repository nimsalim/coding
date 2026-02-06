# _io.TextIOWrapper name='pet_store_inventory.txt' mode='r' encoding='cp1252'>
# Open the file in read mode ("r")
file = open("pet_store_inventory.txt", "r")

# Read the entire content of the file
content = file.read()

# Since .read() returns the contents of a file as a string, the variable storing the output of file.read(), which in this case is content, will store a string.
# It will therefore have access to built-in string methods in Python, such as .upper(), .lower(), and more.
# Update your print statement shown in the following code snippet—you will see that the output will be all uppercase when you run the Python script.
# Print the content
print(content)
print(content.upper())
print(content.lower())
file.close()  # When you open a file using the open() function, it returns a file object.
# This file object contains methods and attributes that you can use to interact with the file.# It is a good practice to close the file after you are done with it to free up system resources.
print(
    "\nThe file is now closed."
)  # This will display the file object information, including the file name, mode, and encoding.
