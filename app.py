import pymysql.cursors
# Подключиться к базе данных.
connection = pymysql.connect(host='5.183.188.132',
                             user='db_vgu_student',
                             password='thasrCt3pKYWAYcK',
                             db='db_vgu_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print ("connect successful!!")
try:
    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT * FROM attribute"
        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)
        print ("cursor.description: ", cursor.description)
        print()
        for row in cursor:
            print(row)
finally:
    # Закрыть соединение (Close connection).
    connection.close()