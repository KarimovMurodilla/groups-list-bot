import openpyxl

from loader import db


# Для конвертирования данных из бд в формат xlsx, используем модуль openpyxl 
async def export_to_xlsx():
    data = await db.get_all_users() # получаем всех пользователей бота 

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Пользователи'
    ws.append(['user_id', 'username', 'first_name', 'date'])

    # с помощью цикла заполняем строки
    for row in data:
        ws.append([row.user_id, row.username, row.first_name, row.date])
    
    wb.save('users.xlsx') # сохраняем файл с названием 'users.xlsx' 