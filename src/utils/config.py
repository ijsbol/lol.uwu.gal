
import json
from typing import Dict, Final

from fastapi.templating import Jinja2Templates

from utils.types import Videos


with open("config/videos.json", "r") as f:
    ENABLED_MEMES: Final[Dict[str, Videos]] = json.loads(f.read())


templates = Jinja2Templates(directory="templates")

