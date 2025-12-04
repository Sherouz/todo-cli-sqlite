# src/database.py

import sqlite3
from sqlite3 import Connection
from src.config  import DB_PATH
from src.utils.logger import log

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    created_at TEXT NOT NULL,
    due_date TEXT,
    done INTEGER DEFAULT 0,
    is_deleted INTEGER DEFAULT 0
);
"""


def get_connection() -> Connection:
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        log.debug("Opened DB connection: %s", DB_PATH)
        return conn
    except Exception as e:
        log.exception(f"Failed to open DB connection: {e}")
        raise


def init_db():
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.executescript(SCHEMA)
            log.info("Database initialized")
    except Exception as e:
        log.exception(f"Failed to initialize database: {e}")
        raise
