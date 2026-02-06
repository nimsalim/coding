with open("C:\\Users\\nbalh\\coding\\labs\\wk5\\pets.txt", "r") as source_file:
    source_file = source_file.read().upper()  # Read and convert content to uppercase
    with open("C:\\Users\\nbalh\\coding\\labs\\wk5\\final.txt", "w") as dest_file:
        dest_file.write(source_file)  # Write the modified content to a new file

# read the image in binary mode to get its size
with open("C:\\Users\\nbalh\\coding\\labs\\wk5\\pet_photo2.jpg", "rb") as file:
    image_data = file.read()
    image_size = len(image_data)  # Get the size of the image in bytes

# Append the image size information to final.txt
with open("C:\\Users\\nbalh\\coding\\labs\\wk5\\final.txt", "a") as dest_file:
    dest_file.write(f"\nImage file: pet_photo2.jpg\nsize: {image_size} bytes\n")
print(
    "File processing complete. 'final.txt' has been created with the modified content and image size information."
)
