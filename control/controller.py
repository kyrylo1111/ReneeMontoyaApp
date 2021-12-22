from models.plant import Plant
from models.employee import Employee
from models.salon import Salon

class Controller:
    def addplant():
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
        plant.saveplant()
    def addemployee():
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.saveemployee()
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
        salon = Salon(id, name, email, department_type, department_id, salon)
        salon.savesalon()
    def getsalon():
        id = int(input("ID: "))
        salon = Salon.get_by_id(id)
        print(salon)
