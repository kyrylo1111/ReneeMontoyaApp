from framework.models import Model
import pymysql
from database.config import host, user, password, db_name


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

    def saveemployee(self):
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name

            )
        except Exception:
            print("соси хуй")
        else:
            print("все гуд")
        mycursor = connection.cursor()

        sql1 = "INSERT INTO Employees (id, name, email, department_type, department_id) VALUES (%s, %s, %s, %s, %s)"
        employee = (self.id, self.name, self.email, self.department_type, self.department_id)
        mycursor.execute(sql1, employee)

        connection.commit()
