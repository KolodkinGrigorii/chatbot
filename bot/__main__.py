import bot.database_client
import bot.telegram_client
import time

def main() -> None:
    next_update_offset=0
    try:
        while True:
            updates = bot.telegram_client.getUpdates(next_update_offset)
            bot.database_client.persist_updates(updates)
            for update in updates:
                message = update.get("message")
                if message is not None:
                    chat_id = message.get("chat", {}).get("id")
                    text = message.get("text")
                    if chat_id is not None and text is not None:
                        bot.telegram_client.sendMessage(
                            chat_id=chat_id,
                            text=text,
                        )
                        print(".", end="", flush=True)
                    else:
                        print("error", end="", flush=True)
                else:
                    print("error", end="", flush=True)
                next_update_offset=max(next_update_offset, update["update_id"]+1)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBye!")
    

if __name__ == "__main__":
    main()