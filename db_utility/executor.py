from mysql.connector import connect
import json
from flask import jsonify


class DB:

    def __init__(self, string : str, **kwargs):
        self.db_name = string
        self.db = connect( host='localhost', user='root',passwd='adRenalin77#' )
        self.cs = self.db.cursor(**kwargs)

    def exe(self,string : str):
        self.cs.execute('use ' + self.db_name)
        self.cs.execute(string)
        self.temp = tuple(i for i in self.cs)
        return self

    def get(self,string:str,**options):
        self.cs.execute('use ' + self.db_name)
        self.cs.execute(string)
        self.temp = tuple(i for i in self.cs)

        if(options.get('get_one',False) == True and len(self.temp) == 1):
            self.temp = self.temp[0]
        return jsonify(self.temp)

    def get_raw(self,string:str,**options):
        self.cs.execute('use ' + self.db_name)
        self.cs.execute(string)
        self.temp = tuple(i for i in self.cs)

        if(options.get('get_one',False) == True and len(self.temp) == 1):
            self.temp = self.temp[0]
        return self.temp

    def commit(self):
        self.db.commit()
        return self

    def close(self):
        self.db.close()
