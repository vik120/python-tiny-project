# insert record in database
import pymysql


def insert_data(connection, cursor, name, email, city):
    connection.connect()
    args = (name, email, city)
    query = f"insert into student (name, email, city) value (%s, %s, %s)"
    cursor.execute(query, args)
    connection.commit()
    print('data inserted')


def show_all_data(cursor, table_name):
    query_select_all = f"select * from {table_name}"
    print(query_select_all)
    cursor.execute(query_select_all)
    query_result = cursor.fetchall()
    print(query_result)


def show_data_by_id(cursor, table_name, sid):
    query = f'select * from {table_name} where sid ={sid}'
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def show_column_by_id(cursor, table_name, column, sid):
    query = f'select {column} from {table_name} where sid ={sid}'
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def update_data(cursor, table_name, name, email, city, sid):
    query = f"update {table_name} set name = '{name}', email = '{email}', city = '{city}' where sid = {sid}"
    print(query)
    cursor.execute(query)


def delete(cursor, table_name, id):
    show_all_data(cursor, table_name)
    query = f"delete from {table_name} where sid = {id}"
    print(query)
    try:

        cursor.execute(query)
        print('query in process')
    except pymysql.Error as e:
        print(e)
    finally:
        print('query executed')
        show_all_data(cursor, table_name)


def user_action(connection, cursor, table_name):
    action = input(" what you want to execute")
    if action == 'insert':
        name = input("enter your name")
        email = input("enter your email")
        city = input("enter your city")
        insert_data(connection, cursor, name, email, city)
    elif action == 'show all':
        show_all_data(cursor, table_name)
    elif action == 'by id':
        id = int(input("what is the id"))
        show_data_by_id(cursor, table_name, id)
    elif action == 'by header and id':
        column = input(' what is column')
        id = int(input(' what is id'))
        show_column_by_id(cursor, table_name, column, id)
    elif action == 'update':
        id = int(input(' what is id'))
        name = input("enter your name")
        email = input("enter your email")
        city = input("enter your city")
        update_data(cursor, table_name, name, email, city, id)
    elif action == 'delete':
        id = int(input(' what is id'))
        delete(cursor, table_name, id)
    else:
        print('pls select proper execution')

# fetch all data from database
