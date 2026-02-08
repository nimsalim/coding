import boto3
import json
import base64
from pathlib import Path


def detect_ingredients_from_image(image_path):
    """Read image file and detect ingredients using Rekognition"""
    try:
        # TODO 1: Read the image file
        with open(image_path, "rb") as image:
            image_bytes = image.read()

        # TODO 2: Initialize Rekognition client to detect ingredients
        rekognition = boto3.client("rekognition")
        # TODO 3: Call detect_labels method and get response
        response = rekognition.detect_labels(
            Image={"Bytes": image_bytes},
            MaxLabels=10,
        )

        # TODO 4: Extract food items from response and save them into the food_items list
        food_items = []
        for label in response["Labels"]:
            food_items.append(label["Name"])

        return food_items

    except Exception as e:
        print(f"Error in processing image or detecting ingredients: {str(e)}")
        return None


def generate_recipe(ingredients, pet_info):
    """Generate recipe using Amazon Bedrock"""
    try:
        # TODO 1: Initialize Bedrock client

        # TODO 2: Format ingredients into prompt string

        # TODO 3: Create request body for Nova model

        # TODO 4: Call Bedrock and handle response

        return recipe

    except Exception as e:
        print(f"Error in recipe generation: {str(e)}")
        return None


def generate_recipe_image(recipe_name):
    """Generate an image of the recipe using Bedrock's Nova Canvas"""
    try:
        # Configure client with appropriate timeout
        from botocore.config import Config

        bedrock = boto3.client("bedrock-runtime", config=Config(read_timeout=300))

        prompt = f"A appetizing bowl of {recipe_name} pet food, professional food photography style"

        # Request body following Nova Canvas format
        request_body = {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {"text": prompt},
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "cfgScale": 8.0,
                "height": 512,
                "width": 512,
                "seed": 0,
            },
        }

        response = bedrock.invoke_model(
            modelId="amazon.nova-canvas-v1:0",
            body=json.dumps(request_body),
            accept="application/json",
            contentType="application/json",
        )

        response_body = json.loads(response["body"].read())

        # Check for errors in the response
        if "error" in response_body and response_body["error"] is not None:
            print(f"Error from model: {response_body['error']}")
            return None

        # Get base64 image and decode
        base64_image = response_body["images"][0]
        base64_bytes = base64_image.encode("ascii")
        image_bytes = base64.b64decode(base64_bytes)

        # Save the generated image
        output_path = "generated_recipe.png"
        with open(output_path, "wb") as file:
            file.write(image_bytes)

        return output_path
    except Exception as e:
        print(f"Error generating recipe image: {str(e)}")
        return None


def save_recipe(recipe, output_file):
    """Save the generated recipe to a file"""
    try:
        # TODO: Implement file saving functionality

        return True
    except Exception as e:
        print(f"Error saving recipe: {str(e)}")
        return False


def main():
    # Pet information
    pet_info = {"breed": "Golden Retriever", "age": 2}

    print("Reading image and detecting ingredients...")
    # TODO 1: Call detect_ingredients_from_image()

    print("Found these ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

    print("\nGenerating recipe...")
    # TODO 2: Call generate_recipe()

    print("Saving recipe...")
    # TODO 3: Call save_recipe()

    # Extract recipe name from the generated text
    recipe_name = recipe_text.split("\n")[0].replace("Recipe Name:", "").strip()

    # Generate and save recipe image
    print("\nGenerating recipe image...")
    image_path = generate_recipe_image(recipe_name)
    if image_path:
        print(f"Recipe image has been saved to {image_path}")
    else:
        print("Failed to generate recipe image")


main()
