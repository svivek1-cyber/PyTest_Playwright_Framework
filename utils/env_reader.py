import os
from pathlib import Path
from dotenv import load_dotenv

# Path to the .env file at the project root
ENV_PATH = Path(__file__).parent.parent / ".env"

# Load the .env file into os.environ
load_dotenv(dotenv_path=ENV_PATH)

def get_env_variable(key: str, default: str = None) -> str:
    """Retrieve an environment variable or return default/raise error."""
    value = os.getenv(key, default)
    if value is None:
        raise KeyError(f"Environment variable '{key}' is not set.")
    return value

def get_env_bool(key: str, default: bool = False) -> bool:
    """Retrieve a boolean environment variable."""
    val = os.getenv(key)
    if val is None:
        return default
    return val.strip().lower() in ("true", "1", "yes")

def get_env_int(key: str, default: int = 30000) -> int:
    """Retrieve an integer environment variable."""
    return int(os.getenv(key, default))