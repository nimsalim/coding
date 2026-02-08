# Import the required boto3 library
import boto3

# Create an Amazon Rekognition client
rekognition = boto3.client("rekognition")


def detect_labels(image_path, max_labels=10):
    """
    Detects labels in images using Amazon Rekognition.

    Parameters:
        image_path: Path to the local image file
        max_labels: Maximum number of labels to return (default: 10)
    """
    # Read the image file
    with open(image_path, "rb") as image:
        image_bytes = image.read()

    # Perform label detection
    response = rekognition.detect_labels(
        Image={"Bytes": image_bytes}, MaxLabels=max_labels
    )

    # Extract and return the label names
    labels = []
    for label in response["Labels"]:
        labels.append(label["Name"])

    return labels


# Test your function with this example call:
result = detect_labels("assets/sample_image.jpeg", max_labels=5)
print("Labels detected:", result)
