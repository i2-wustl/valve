import os
from pprint import pprint
import requests
from datetime import datetime
import json

class HttpClientFactory:
    def data_basin_api(self):
        timezone_offset = -datetime.utcnow().timestamp() + datetime.now().timestamp()

        headers = {
            "X-Timezone-Offset": str(timezone_offset),
        }

        client = requests.Session()
        client.base_url = os.getenv("X_API_BASE_URL")  # Replace with your API base URL
        client.headers.update(headers)        
        client.timeout = 10  # Timeout of 10 seconds

        return client

    def handle_error(self, response):
        data = {
            "title": "Sorry, an unexpected error has occured.",
            "message": "Sorry, an unexpected error has occured.",
            "errors": [],
        }

        if response.text:
            try:
                data = response.json()
                pprint(data)
            except json.JSONDecodeError:
                pass

        status = response.status_code

        if status == 0:
            raise NetworkException()

        error_mapping = {
            400: BadRequestException,
            401: UnauthorizedException,
            403: ForbiddenException,
            409: ConflictException,
            500: UnexpectedException,
        }

        exception_cls = error_mapping.get(status, UnexpectedException)
        pprint(data)
        if isinstance(data, list):            
            raise exception_cls(data[0].get('title', ''), data[0].get('errors', []))
        else:            
            raise exception_cls(data.get('title', ''), data.get('errors', []))
    

    def create(self):
        return self.data_basin_api()

class CustomException(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

class UnexpectedException(CustomException):
    def __init__(self, message="Sorry, an unexpected error has occured.", code="500"):
        super().__init__(message, code)

class UnauthorizedException(CustomException):
    def __init__(self, message="Unauthorized", code="401"):
        super().__init__(message, code)

class ForbiddenException(CustomException):
    def __init__(self, message="Forbidden", code="403"):
        super().__init__(message, code)

class ConflictException(CustomException):
    def __init__(self, message="Already exists", code="409"):
        super().__init__(message, code)

class NetworkException(CustomException):
    def __init__(self, message="Network Exception", code="0"):
        super().__init__(message, code)

class BadRequestException(CustomException):
    def __init__(self, title, errors):
        message = f"{title}\n{''.join(f'{error}' for error in errors)}"
        super().__init__(message, "400")
