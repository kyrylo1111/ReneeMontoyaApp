from framework.models import Model
import pymysql
from database.config import host, user, password, db_name


class Salon(Model):
    file = "salons.json"

    def __init__(self, id, name, email, department_type, department_id, salon):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id
        self.salon = salon

    def savesalon(self):

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
        salo = (self.id, self.name, self.email, self.department_type, self.department_id, self.salon)

        mycursor.execute(sql2, salo)

        connection.commit()
