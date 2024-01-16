import pymysql
import  db_action

# creating db with database
# def connect_db():
#     return pymysql.connect(host='Apples-MacBook-Air.local', database='learnStudent', user='root', password='Vikass@2024', port=3306)
#
#
# # Table create
# def create_table():
#     conn = connect_db()
#     print(conn)
#     cursor = conn.cursor()  # cursor helps to execute the query
#     print(cursor)
#     query = ('create table student(sid int primary key auto_increment, name VARCHAR(50), email VARCHAR(50), '
#              'city VARCHAR(50) )')
#     cursor.execute(query)
#     conn.commit()
#     print('table created')
#     conn.close()



# creating db with database
connection = pymysql.connect(host='Apples-MacBook-Air.local', database='learnStudent', user='root',
                             password='Vikass@2024', port=3306)

table_name = 'student'
cursor = connection.cursor()

# check if table exist or not
check_table_query = f"Show tables like '{table_name}'"
cursor.execute(check_table_query)

# fetch the result
result = cursor.fetchone()





# if table does not exist create it
if not result:
    query = (
        'create table if not exits student(sid int primary key auto_increment, name VARCHAR(50), email VARCHAR(50), '
        'city VARCHAR(50) )')
    cursor.execute(query)
    connection.commit()
    print(f'Table {table_name} created successfully.')
else:
    db_action.user_action(connection, cursor, table_name)




connection.close()
