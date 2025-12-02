# utils.py

import os
import logging
import re

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_current_path():
    """Returns the current working directory."""
    return os.getcwd()

def is_valid_email(email: str) -> bool:
    """Validates an email address using a regular expression."""
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def get_env_var(var_name: str, default: str = None):
    """Gets an environment variable or returns a default value if it's not set."""
    return os.environ.get(var_name, default)

def format_date(date_string: str) -> str:
    """Formats a date string in the format 'YYYY-MM-DD' to 'Month DD, YYYY'."""
    import dateutil.parser
    date = dateutil.parser.parse(date_string)
    return date.strftime("%B %d, %Y")

def trim_whitespace(s: str) -> str:
    """Removes leading and trailing whitespace from a string."""
    return s.strip()