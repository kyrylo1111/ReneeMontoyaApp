from models.plant import Plant
from models.employee import Employee
from models.salon import Salon
import pymysql
from database.config import host, user, password, db_name
class Controller:
    def addplant():
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
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

        sql = "INSERT INTO Plants (id, location, name, director_id) VALUES (%s, %s, %s, %s)"
        val = (id, location, name, director_id)
        mycursor.execute(sql, val)

        connection.commit()
    def addemployee():
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))

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
        employee = (id, name, email, department_type, department_id)
        mycursor.execute(sql1, employee)

        connection.commit()
    def getplant():
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)
    def getemployee():
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)
    def addsalon():
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        salon = input("Salon:")

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

        sql2 = "INSERT INTO Salons (id, name, email, department_type, department_id, salon) VALUES (%s, %s, %s, %s, %s, %s)"
        salo = (id, name, email, department_type, department_id, salon)

        mycursor.execute(sql2, salo)

        connection.commit()
    def getsalon():
        id = int(input("ID: "))
        salon = Salon.get_by_id(id)
        print(salon)
