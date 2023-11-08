import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        connect = sqlite3.connect('database/database.db')
        return connect
    except Error:
        print(Error)


def sql_create_table(conn):
    cursor_obj = conn.cursor()
    cursor_obj.execute(
        "CREATE TABLE if not exists users(id integer PRIMARY KEY, "
        "name text, quantity_requests integer)"
    )
    cursor_obj.execute(
        "CREATE TABLE if not exists requests(name text, request text, number_request integer)"
    )

    conn.commit()


def insert_user(conn, name, data):
    cursor_obj = conn.cursor()
    rows = len(cursor_obj.execute('SELECT * FROM users').fetchall())
    cursor_obj.execute(f'INSERT INTO users(id, name, quantity_requests) '
                       f'VALUES({rows + 1}, "{name}", 1)')
    cursor_obj.execute(f'INSERT INTO requests(name, request, number_request) '
                       f'VALUES("{name}", "{data}", 1)')

    conn.commit()


def update_user(conn, name, data):
    cursor_obj = conn.cursor()
    quantity = cursor_obj.execute(f'SELECT quantity_requests from users WHERE name = "{name}"').fetchall()[0][0]
    if quantity < 10:
        cursor_obj.execute(f'UPDATE users SET quantity_requests = {quantity + 1} WHERE name = "{name}"')
        cursor_obj.execute(f'INSERT INTO requests(name, request, number_request) '
                           f'VALUES("{name}", "{data}", {quantity + 1})')
    else:
        cur_data = cursor_obj.execute(
            f'SELECT request, number_request from requests WHERE name = "Bladgor"').fetchall()
        for elem in cur_data[1:]:
            print(elem)
            cursor_obj.execute(f'UPDATE requests SET request = "{elem[0]}" '
                               f'WHERE name = "Bladgor" AND number_request = {elem[1] - 1}')
        cursor_obj.execute(f'INSERT INTO requests(name, request, number_request) '
                           f'VALUES("{name}", "{data}", 10)')

    conn.commit()


def select_name(conn):
    cursor_obj = conn.cursor()
    users = cursor_obj.execute('SELECT name FROM users')

    return users.fetchall()


def database_handler(name_user, request):
    con = sql_connection()
    sql_create_table(con)

    if (name_user,) in select_name(con):
        update_user(con, name_user, request)
    else:
        insert_user(con, name_user, request)
