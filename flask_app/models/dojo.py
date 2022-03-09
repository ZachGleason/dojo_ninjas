# from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL
# from .ninja import Ninja
from flask_app.models.ninja import Ninja
from pprint import pprint


class Dojo:
    db = 'ninja-dojo'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s , NOW(), NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        pass

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        pass

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        pass


    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojo_id =%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
            pprint(n)
        return dojo

        # print(results)
        # dojo = cls(results[0])
        # for row in results:
        #     n = {
        #         "id": row['ninjas.id'],
        #         "first_name": row['first_name'],

        #     }