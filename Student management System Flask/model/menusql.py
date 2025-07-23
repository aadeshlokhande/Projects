from Config.DataBaseConnection import getDBConnection, closeDBConnection
from flask import request

class MenuModel:
    def fetchAllMenu():
        db = getDBConnection()
        with getDBConnection().cursor() as query:
            sql = """SELECT id, name,route,is_delete FROM permissions WHERE is_delete = '0'"""
            query.execute(sql)
            DBdata = query.fetchall()
            return DBdata
    
    def uniqueName(name):
        db=getDBConnection()
        with db.cursor() as query:
            sql = f"""SELECT id from permissions WHERE name='{name}' and is_delete = '0'"""
            query.execute(sql)
            dbData = query.fetchone()
            return True if dbData==None else False 
        
    def uniqueRoute(route):
        db=getDBConnection()
        with db.cursor() as query:
            sql = f"""SELECT id from permissions WHERE name='{route}' and is_delete = '0'"""
            query.execute(sql)
            dbData = query.fetchone()
            return True if dbData==None else False
        
    def addMenu(formData):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""INSERT INTO permissions SET 
                name = '{formData['name']}', 
                route = '{formData['route']}'"""
            query.execute(sql)
            db.commit()
    
    def getRole(id):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""SELECT id, name, route, is_delete from permissions WHERE id = '{id}' and is_delete = '0'"""
            query.execute(sql)
            dbdata = query.fetchone()
            return dbdata

    def delmenu(idd):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""UPDATE permissions SET 
                is_delete = '1'
                WHERE id = '{idd}'"""
            query.execute(sql)
            db.commit()

    def uniqueNameee(idd,name):
        db=getDBConnection()
        with db.cursor() as query:
            sql = f"""SELECT id from permissions WHERE id != {idd} AND name='{name}' AND is_delete = '0'"""
            query.execute(sql)
            dbData = query.fetchone()
            return True if dbData==None else False
        
    def uniqueRouteee(idd,route):
        db=getDBConnection()
        with db.cursor() as query:
            sql = f"""SELECT id from permissions WHERE id != {idd} AND route ='{route}' AND is_delete = '0'"""
            query.execute(sql)
            dbData = query.fetchone()
            return True if dbData==None else False

    def update(idd, name,route):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""UPDATE permissions SET name = '{name}', route = '{route}' WHERE id='{idd}'"""
            query.execute(sql)
            db.commit()