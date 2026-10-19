
import os
import requests


def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    message = (
        "✅ Telegram-мониторинг подключён.\n\n"
        "Следующий этап — подключение Tonnel, MRKT и Getgems."
    )

    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message,
        },
        timeout=20,
    )

    response.raise_for_status()
    print("Сообщение успешно отправлено")


if __name__ == "__main__":
    main()
