import json
from pathlib import Path

LOG_DIR = Path("data")
LOG_DIR.mkdir(exist_ok=True)


def save_to_json_file(contacts, filename):
    with open(
        f"{LOG_DIR}/{filename}_contacts.json", "w", encoding="utf-8"
    ) as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
