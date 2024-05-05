'''
Utility class for interacting with the API provided for the course.
API is stored in .dotenv file for safe upload to GitHub.
To test this you will need to have python-dotenv imported and use the os tools to access it.
'''

import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ApiUtility:
    def __init__(self):
        self.api_url = os.environ.get('API_URL')

    def get(self):
        response = requests.get(self.api_url)
        content = response.json()
        return content
    