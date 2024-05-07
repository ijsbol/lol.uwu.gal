
import json
from typing import Dict, Final

from fastapi.templating import Jinja2Templates

from utils.types import IPMemes


with open("config/ip_memes.json", "r") as f:
    ENABLED_MEMES: Final[Dict[str, IPMemes]] = json.loads(f.read())


templates = Jinja2Templates(directory="templates")

