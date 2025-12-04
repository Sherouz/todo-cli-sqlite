# src/config.py

from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "task.db"
DB_PATH.parent.mkdir(exist_ok=True, parents=True)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"