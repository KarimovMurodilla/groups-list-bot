import openpyxl

from loader import db

async def export_to_xlsx():
    data = await db.get_all_users()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Пользователи'
    ws.append(['user_id', 'username', 'first_name', 'date'])

    for row in data:
        ws.append([row.user_id, row.username, row.first_name, row.date])
    
    wb.save('users.xlsx')