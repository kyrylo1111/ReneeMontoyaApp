from abc import ABC, abstractmethod
import json
import pymysql
from database.config import host, user, password, db_name
class Model(ABC):
    file = 'default.json'

    def savep(self):

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
        val = (self.id, self.location, self.name, self.director_id)
        mycursor.execute(sql, val)

        connection.commit()

    def savee(self):
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

    def saves(self):
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
    def save(self):
        file_in_dict_format = self._generate_dict()
        file = self.get_file_data(self.file)
        file.append(file_in_dict_format)
        self.save_to_file(file)

    def _generate_dict(self):
        return self.__dict__

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el['id'] == id:
                return el

        raise Exception("Not found")

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()
