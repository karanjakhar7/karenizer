import os
from dotenv import load_dotenv

load_dotenv()

LITELLM_MODEL: str = os.getenv("LITELLM_MODEL", "gpt-4o-mini")
