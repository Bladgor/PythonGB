import sqlite3
from pprint import pprint

connect = sqlite3.connect('database.db')

cursor_obj = connect.cursor()
data = cursor_obj.execute(f'SELECT request, number_request from requests WHERE name = "Bladgor"').fetchall()
print(data)

for elem in data[1:]:
    print(elem)
    cursor_obj.execute(f'UPDATE requests SET request = "{elem[0]}" '
                       f'WHERE name = "Bladgor" AND number_request = {elem[1] - 1}')
connect.commit()

