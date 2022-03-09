# from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    db = 'ninja-dojo'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)


    # @classmethod
    # def get_all_dojos(cls, data):
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE id=%(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE ninjas SET name=%(name)s, age=%(age)s, updated_at=NOW() WHERE id=%(id)s"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     pass

    # @classmethod
    # def delete(cls,data):
    #     query = "DELETE FROM ninjas WHERE id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data)
    #     pass


