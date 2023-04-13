from environs import Env

# используем библиотеку environs
env = Env()
env.read_env()

# Telegram Bot
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список админов

# DB
DATABASE_URL = env.str("DATABASE_URL")