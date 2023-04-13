# groups-list-bot

## Описание бота
Данный телеграм бот создан для поиска групп в Telegram. Он написан на aiogram, использует sqlite3 для БД и sqlalchemy для ORM. Бот позволяет добавлять новые группы в файл `utils/misc/group_links.py`, чтобы они могли отображаться на пользовательском интерфейсе бота. Кроме того, вы можете добавлять новых администраторов, следуя инструкциям в разделе ниже.


## Установка
Чтобы установить и запустить бота, выполните следующие шаги:
1. Склонируйте репозиторий с ботом на ваше устройство.
2. Установите зависимости, выполнив команду `pip install -r requirements.txt`.
3. Создайте файл .env, добавьте переменную `BOT_TOKEN` с токеном вашего телеграм бота и переменную `ADMINS` с user_id нового админа (если требуется).
4. Запустите бота командой `python app.py`.


## Добавление новых групп
Чтобы добавить новые группы в бот, следуйте этим инструкциям:
1. Откройте файл `utils/misc/group_links.py`.
2. Добавьте новый ключ значение в словарь `links`. Ключ - это название группы, а значение - это ссылка на группу. Можно указать несколько значений для одного ключа, перечислив их в виде списка.
3. Сохраните изменения в файле.


## Добавление новых администраторов
Чтобы добавить новых администраторов в бота, выполните следующие действия:
    1. Откройте файл `.env`
    2. Добавьте `user_id` нового админа в переменную `ADMINS`, разделяя их запятой.
    3. Сохраните изменения в файле.


## Замена БД
Если вы хотите заменить sqlite3 на другую СУБД, выполните следующие шаги:
    1. Откройте файл `config.py`.
    2. Измените значение переменной `DATABASE_URL` на соответствующую для вашей СУБД.
    3. Измените ORM на используемый для вашей СУБД.
    4. Сохраните изменения в файле.