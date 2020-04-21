from api.connection import connection 
from model.Employee import Employee


def update_employee(employee: Employee, id):
    cur = connection.cursor()
    sql = f"UPDATE Employees SET\
            First_Name='{employee.first_name}',\
            Last_Name='{employee.surname}',\
            Email='{employee.email}',\
            Phone_Number='{employee.phone_number}',\
            Hire_Date='{employee.hire_date}',\
            Job_ID='{employee.job_id}',\
            Annual_Salary={employee.salary},\
            Commission_Percent={employee.commission},\
            Manager_ID={employee.manager_id},\
            Department_No={employee.department_no}\
            WHERE Employee_No={id}"
    print(sql)
    cur.execute(sql)

    return cur.fetchall()
    
    