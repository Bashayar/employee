from api.connection import connection 


def delete_employee(id):
    cur = connection.cursor()
    sql = f"DELETE FROM Employees WHERE Employee_No={id}"
    cur.execute(sql)

    return cur.fetchall()
    
    