import sqlite3

connection = sqlite3.connect('database/database.db')
cursor = connection.cursor()

# Подсчет общего числа пользователей
cursor.execute('SELECT COUNT(*) FROM Requests WHERE name = "Bladgor"')
total_users = cursor.fetchone()[0]

print('Общее количество пользователей:', total_users)
quantity = cursor.execute(f'SELECT quantity_requests from Users WHERE name = "Bladgor"').fetchall()[0][0]
print(cursor.execute(f'SELECT quantity_requests from Users WHERE name = "Bladgor"').fetchall())
connection.close()
