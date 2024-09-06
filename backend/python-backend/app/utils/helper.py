from datetime import datetime
from typing import Any, Dict, Tuple

def validate_date(date_str: str) -> Tuple[bool, str]:
    """
    Validate if the input date string is in the correct format (YYYY-MM-DD).

    Args:
        date_str (str): The date string to validate.

    Returns:
        Tuple[bool, str]: A tuple where the first element is a boolean indicating validity,
                          and the second element is an error message if invalid.
    """
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True, ""
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."

def format_date(date: datetime) -> str:
    """
    Format a datetime object to a string in the format YYYY-MM-DD.

    Args:
        date (datetime): The datetime object to format.

    Returns:
        str: The formatted date string.
    """
    return date.strftime('%Y-%m-%d')

def get_current_timestamp() -> str:
    """
    Get the current timestamp as a string in the format YYYY-MM-DD HH:MM:SS.

    Returns:
        str: The current timestamp.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def extract_error_message(response: Dict[str, Any]) -> str:
    """
    Extract an error message from a response dictionary.

    Args:
        response (Dict[str, Any]): The response dictionary containing error information.

    Returns:
        str: The extracted error message.
    """
    return response.get("error", "An unknown error occurred.")

def is_valid_email(email: str) -> bool:
    """
    Validate if the input string is a valid email format.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    import re
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex, email) is not None

def sanitize_input(input_string: str) -> str:
    """
    Sanitize input string to prevent injection attacks and other security issues.

    Args:
        input_string (str): The input string to sanitize.

    Returns:
        str: The sanitized string.
    """
    return input_string.replace("<", "&lt;").replace(">", "&gt;").strip()
