import boto3

# Create a Translate client
translate = boto3.client("translate")


def translate_text(text, source_lang, target_lang):
    """
    Translate text using Amazon Translate.

    Args:
        text (str): Text to translate
        source_lang (str): Source language code (e.g., 'en')
        target_lang (str): Target language code (e.g., 'es')
    """

    # Perform the translation
    response = translate.translate_text(
        Text=text, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang
    )
    return response["TranslatedText"]


# Example usage
source_text = "Machine learning helps computers understand patterns in data."
translated = translate_text(source_text, "en", "fr")
print(f"Original: {source_text}")
print(f"Translated: {translated}")


"""Lesson 14 of 17
Summary
In this topic, you explored the following concepts:

•
Amazon Translate is a fully managed machine translation service that uses neural networks and deep learning to provide high-quality translations across 75 languages and over 5,550 language pairs.
•
There are three required parameters to work with Amazon Translate: the input text, source language, and target language. This makes it straightforward to use Amazon Translate either through the AWS Console or programmatically.

•Beyond basic translation, Amazon Translate offers advanced features, such as custom terminology for maintaining consistent brand names and technical terms. It also offers a brevity setting for controlling translation length, a formality setting for appropriate language tone, and profanity masking for content moderation.
•
Amazon Translate learns language patterns directly from large amounts of translated text, which allows it to capture subtle nuances in language and consider context for more accurate translations. You can request high-quality translations from your code using the AWS SDK for Python (boto3) client."""
