from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def ensure_user_exists(self, telegram_id: int) -> None: ...

    @abstractmethod
    def clear_user_state_and_order(self, telegram_id: int) -> None: ...

    @abstractmethod
    def update_user_state(self, telegram_id: int, state: str) -> None: ...

    @abstractmethod
    def persist_update(self, update: dict) -> None: ...

    @abstractmethod
    def update_user_state_and_order(self, telegram_id: int, order: dict) -> None: ...

    @abstractmethod
    def recreate_database(self) -> None: ...

    @abstractmethod
    def get_user(self, telegram_id: int) -> dict: ...
