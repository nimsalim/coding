import unittest
from unittest.mock import patch, MagicMock
import requests

class TestAPIRequest(unittest.TestCase):
    """Test suite for the API request functionality in lesson1.py"""
    
    @patch('requests.get')
    @patch('builtins.print')
    def test_successful_request_with_200_status(self, mock_print, mock_get):
        """Test successful HTTP request with status code 200"""
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response
        
        # Act
        response = requests.get("https://google.com")
        if response.status_code == 200:
            print("Got the data!")
            data = response.json()
        
        # Assert
        mock_get.assert_called_once_with("https://google.com")
        mock_print.assert_called_once_with("Got the data!")
        assert data == {'key': 'value'}
    
    @patch('requests.get')
    @patch('builtins.print')
    def test_failed_request_with_404_status(self, mock_print, mock_get):
        """Test failed HTTP request with status code 404"""
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        # Act
        response = requests.get("https://google.com")
        if response.status_code == 200:
            print("Got the data!")
            data = response.json()
        
        # Assert
        mock_get.assert_called_once_with("https://google.com")
        mock_print.assert_not_called()
    
    @patch('requests.get')
    def test_json_parsing_on_success(self, mock_get):
        """Test that response.json() is called when status is 200"""
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'message': 'success'}
        mock_get.return_value = mock_response
        
        # Act
        response = requests.get("https://google.com")
        if response.status_code == 200:
            data = response.json()
        
        # Assert
        mock_response.json.assert_called_once()
    
    @patch('requests.get')
    def test_request_endpoint(self, mock_get):
        """Test that the correct endpoint is being called"""
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Act
        requests.get("https://google.com")
        
        # Assert
        mock_get.assert_called_once_with("https://google.com")


if __name__ == '__main__':
    unittest.main()


import random
def generate_random_number():
    random_number = random.randint(1, 100)
    print(random_number)

import random

num = random.random()

print(num)

pip install numpy
     # Server responds with data