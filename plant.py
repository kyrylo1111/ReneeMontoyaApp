from framework.models import Model
import pymysql
from database.config import host, user, password, db_name
class Plant(Model):

    def __init__(self, id, location, name, director_id):
        self.id = id
        self.location = location
        self.name = name
        self.director_id = director_id

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

    cursor = connection.cursor()
    sql = "INSERT INTO Plants (id, location, name, director_id) VALUES (%s, %s, %s, %s)"
    val = ()
    cursor.executemany(sql, val)


