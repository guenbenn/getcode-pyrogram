import os
from pyrogram import Client

api_id = xxx  # Thay bằng api_id của bạn
api_hash = 'xxx'  # Thay bằng api_hash của bạn

sessions_dir = "sessions"
telegram_id = 777000

while True:
    print("--------------------")
    session_name_input = input("Nhập tên file .session: ")
    session_name = os.path.join(sessions_dir, session_name_input)

    app = Client(session_name, api_id, api_hash)

    with app:
        messages = app.get_chat_history(telegram_id, limit=10)

        for message in messages:
            if "Login code" in message.text:
                login_code = message.text.split("Login code: ")[1].split()[0].rstrip('.')
                message_time = message.date.strftime('%Y-%m-%d %H:%M:%S')
                print(f"Mã đăng nhập: {login_code} ({message_time}).")
                break

    continue_input = input("Nhập mã tiếp (y/n): ").strip().lower()
    if continue_input != 'y':
        break
