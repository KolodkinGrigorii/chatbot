from bot.database_client import ensure_user_exists
from bot.handlers.handler import Handler, HandlerStatus


class EnsureUserExists(Handler):
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool:
        return "message" in update and "from" in update["message"]

    def handle(self, update: dict, state: str, order_json: dict) -> bool:
        telegram_id = update["message"]["chat"]["id"]
        ensure_user_exists(telegram_id)
        return HandlerStatus.CONTINUE
