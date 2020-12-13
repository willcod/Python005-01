import pymysql

db = pymysql.connect('47.103.136.85', 'remoteUser', '123456', 'mydevdb')


try:
    with db.cursor() as cursor:
        transfer_amount = 100

        cursor.execute('''SELECT account.ID, amount FROM account
                 JOIN user on account.ID = user.ID
                 WHERE user.user_name = '张三'
                 ''')
        user_out = cursor.fetchone()
        if user_out[1] < transfer_amount:
            raise ValueError("the amount is less than demanding")

        cursor.execute('''SELECT account.ID, amount FROM account
                 JOIN user on account.ID = user.ID
                 WHERE user.user_name = '李四'
                 ''')

        user_in = cursor.fetchone();
        
        sql = 'UPDATE account SET amount = %s WHERE ID = %s'
        value = (user_out[1] - transfer_amount, user_out[0])
        cursor.execute(sql, value)

        sql = 'UPDATE account SET amount = %s WHERE ID = %s'
        value = (user_in[1] + transfer_amount, user_in[0])
        cursor.execute(sql, value)

        sql = 'INSERT INTO audit (user_in, user_out, amount) VALUES(%s, %s, %s)'
        value = (user_in[0], user_out[0], transfer_amount)
        cursor.execute(sql, value)

    db.commit()

except Exception as e:
    print("transfer failed")
    db.rollback();

finally: 
    db.close()
    print(cursor.rowcount)