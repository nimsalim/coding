print("AnyCompany Adoption Certificate Generator")

# Ask staff how many certificates they want to print
num_certificates = input("How many certificates would you like to print? ")

try:
    # Try to convert input to an integer
    count = int(num_certificates)

    # Print the certificates
    for i in range(count):
        print("Certificate", i + 1, "- Congratulations on your new pet!")

# Catch specific ValueError if input is not a number
except ValueError:
    print("Please enter a valid **number**, like 3 or 5.")

# Catch any other unexpected errors
except Exception as e:
    print("Something unexpected went wrong.")
    print("Error message:", e)
    print("Error type:", type(e))
