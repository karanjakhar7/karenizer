import sys
from pathlib import Path

# Add project root to sys.path so imports from app/ resolve correctly
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app  # noqa: F401 — Vercel looks for `app` as the ASGI handler
