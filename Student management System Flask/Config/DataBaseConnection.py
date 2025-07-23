from flask import g 

import pymysql
import pymysql.cursors

# ████████████████████ Database connection ████████████████████
DATABASE_CONFIGURATION = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "db" : "monolythicapp_db",
    "cursorclass" : pymysql.cursors.DictCursor
}


def getDBConnection():
    if 'db' not in g:
        g.db = pymysql.connect(**DATABASE_CONFIGURATION)
        print("Database connection established")
    return g.db

def closeDBConnection(exception):
    db = g.pop('db',None)
    if db is not None:
        db.close()
        print("db connection closed")
