import bot.telegram_client
import json
import os
import sqlite3

from bot.handler import Handler
from dotenv import load_dotenv

load_dotenv()


class DatabaseLogger(Handler):
    def can_handle(self, update: dict) -> bool:
        try:
            connection=sqlite3.connect(os.getenv('SQLITE_DATABASE_PATH'))
            connection.close()
            return True
        except:
            return False

    def handle(self, update: dict) -> bool:
        connection=sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH"))
        with connection:
            data = [(json.dumps(update, ensure_ascii=False, indent=2),)]
            connection.executemany(
                "INSERT INTO telegram_updates (payload) VALUES(?)",
                data,
            )
        connection.close()
        return True