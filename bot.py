import os
import requests
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv("BOT_TOKEN")
VIDEO_URL = os.getenv("VIDEO_URL")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def send_video():
    try:
        response = requests.get(VIDEO_URL, stream=True)
        file_name = "video.mp4"

        if response.status_code == 200:
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print("Видео загружено, отправляю в Telegram...")
            with open(file_name, "rb") as video:
                await bot.send_video(chat_id=CHAT_ID, video=video)
        else:
            print("Ошибка загрузки видео")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    executor.start(dp, send_video())
  
