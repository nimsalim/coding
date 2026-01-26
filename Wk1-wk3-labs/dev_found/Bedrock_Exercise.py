# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Connect to Amazon Bedrock.
bedrock = boto3.client("bedrock-runtime")

# Ask the user for inputs.

# validate pet type before proceeding
max_retries = 3
retry_count = 0

while retry_count < max_retries:
    pet_type = input("Enter your pet type (dog/cat): ").strip().lower()
    if pet_type in ["dog", "cat"]:
        break   
    retry_count += 1
    remaining = max_retries - retry_count
    if remaining > 0:
        print(f"Invalid input. Please enter either 'dog' or 'cat'. {remaining} attempts remaining.")
    else:
        print("Maximum attempts reached. Exiting.")
        exit()
# Collect other input
pet_name = input("Enter your pet's name: ")
ingredients = input("Enter your ingredients separated by commas: ")
allergies = input("Enter any allergies separated by commas (press Enter if none): ")

prompt = f"What are the nutritional benefits and considerations of these ingredients for a {pet_type}: {ingredients} recipe?"
if allergies:
    prompt += f" Also discuss alternatives for these allergies: {allergies}." 
prompt += " Please include a disclaimer about consulting with a veterinarian."

# Set up request parameters.
max_tokens = int(input("Enter max tokens (default 600): ") or "600")
temperature = float(input("Enter temperature 0.0-1.0 (default 0.7): ") or "0.7")

# Create request with the Amazon Nova Lite model
request = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": prompt
                }
            ]
        }
    ],
    "inferenceConfig": {
        "maxTokens": max_tokens, # TODO: Add the maxTokenCount key and assign the value of max_tokens.
        "temperature": temperature,
        "topP": 0.9
    }
}

# Send the request to Bedrock and generate the recipe.
response = bedrock.invoke_model(
    modelId="amazon.nova-lite-v1:0",
    body=json.dumps(request)
)

# Process and display the recipe.
response_body = json.loads(response["body"].read())
print(f"\nRecipe generated with {max_tokens} max tokens and a temperature of {temperature}.\n")
if response_body["output"]["message"]["content"][0]["text"].startswith(" - The generated text has been blocked"):
    print("I apologize, but I cannot provide specific pet food recipes. For your pet's safety, please consult with a veterinarian about proper nutrition and diet plans.")
else:
    print(response_body["output"]["message"]["content"][0]["text"])

