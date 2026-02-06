with open("C:\\Users\\nbalh\\coding\\labs\\wk5\\pet_photo1.jpg", "rb") as file:
    image_data = file.read()
    print(len(image_data))  # Prints the size of the image in bytes
