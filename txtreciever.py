import os
import requests
import pyperclip
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_and_copy_to_clipboard(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Get the content of the response
        content = response.text
        
        # Print content
        content_replaced = content.replace('\n', "<LF>").replace('\r', "<CR>").replace('\t', "<TAB>").replace(' ', "<SPACE>")
        print(content_replaced)

        # Copy the content to the clipboard
        pyperclip.copy(content)
        print("Content copied to clipboard successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Get the URL from the STORE_URL environment variable
    store_url = os.getenv('STORE_URL')

    if store_url is None:
        print("Error: STORE_URL not found in .env file")
    else:
        fetch_and_copy_to_clipboard(store_url)