from Config.DataBaseConnection import getDBConnection, closeDBConnection
from flask import request

class roleModel:
    def fetchAllMenu():
        db = getDBConnection()
        with getDBConnection().cursor() as query:
            sql = """SELECT id, name, is_delete FROM roles WHERE is_delete = '0'"""
            query.execute(sql)
            DBdata = query.fetchall()
            return DBdata

    def addRole(data):
        row_id = ""
        db = getDBConnection()

        if data["id"]:
            with db.cursor() as query:
                sql = f"DELETE FROM role_permission_mapping WHERE role_id = '{data["id"]}';"
                query.execute(sql)
                db.commit()

        if not data["id"]:
            with db.cursor() as query:
                sql = f"""INSERT INTO roles SET name = '{data["name"]}'"""
                query.execute(sql)
                db.commit()
                row_id = query.lastrowid 
        else:
            row_id = data["id"]
            with db.cursor() as query:
                sql = f"UPDATE roles SET name= '{data["name"]}' WHERE id= {row_id}"
                query.execute(sql)
                db.commit()

        with db.cursor() as query:
            sql = f"""INSERT INTO role_permission_mapping (role_id, permission_id) values"""
            for per in data["permissions"]:
                sql += f"""({row_id},{per}),"""
            sql = sql[:-1]
            print(sql)
            query.execute(sql)
            db.commit()


    
    def roleDetails(id):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""SELECT id, name, is_delete from roles WHERE id = '{id}' and is_delete = '0'"""
            query.execute(sql)
            dbdata = query.fetchone()
            return dbdata

    def getRole(id):
        db = getDBConnection()
        permissions,roles = {},{}

        with db.cursor() as query:
            sql = f"""SELECT * FROM roles r
              WHERE r.id={id}"""
            print(sql)
            query.execute(sql)
            roles = query.fetchone()
        
        with db.cursor() as query:
            sql = f"SELECT permission_id FROM role_permission_mapping WHERE role_id={id}"
            query.execute(sql)
            permissions = query.fetchall()
        
        return {"permissions":permissions, "roles":roles}



    def delRole(idd):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""UPDATE roles SET 
                is_delete = '1'
                WHERE id = '{idd}'"""
            query.execute(sql)
            db.commit()

    def getPermissionByRoleID(role_id):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""SELECT p.name, p.route, p.id FROM role_permission_mapping AS rpm
            join permissions p ON rpm.permission_id = p.id 
            WHERE rpm.role_id = {role_id}"""
            query.execute(sql)
            permission = query.fetchall()
            return permission