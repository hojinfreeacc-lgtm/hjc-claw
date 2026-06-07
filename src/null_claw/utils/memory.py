import sqlite3
import json
from datetime import datetime
from pathlib import Path

class Memory:
    def __init__(self):
        self.db_path = Path.home() / ".null-claw" / "history.db"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    input TEXT,
                    intent TEXT,
                    status TEXT,
                    result TEXT
                )
            """)

    def save(self, analysis, status, result):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO history (timestamp, input, intent, status, result) VALUES (?, ?, ?, ?, ?)",
                (datetime.now().isoformat(), analysis["raw"], analysis["intent"], status, result)
            )

    def get_recent(self, limit=5):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM history ORDER BY id DESC LIMIT ?", (limit,))
            return [dict(row) for row in cursor.fetchall()]
