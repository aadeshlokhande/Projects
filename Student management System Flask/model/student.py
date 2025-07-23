from Config.DataBaseConnection import getDBConnection, closeDBConnection
from flask import request

class StudentModel:
    def checkduplicatePrn(student_id,prn_number):
        print("in midel")
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"SELECT id FROM students WHERE id != '{student_id}' and prn='{prn_number}'"
            query.execute(sql)
            db.commit()
            return query.fetchone()

    def fetchAllStudentInfo(search=False,limit=10 ):
        db = getDBConnection()
        offset = request.args.get('offset',0)
        with getDBConnection().cursor() as query:
            sql = """SELECT id,first_name, last_name, mobile_number, standard, section, age, prn FROM students"""
            if search:
                sql += f""" 
                WHERE first_name LIKE '%{search}%' OR last_name LIKE '%{search}%' OR mobile_number LIKE '%{search}%' OR standard LIKE '%{search}%' OR section LIKE '%{search}%' OR age LIKE '%{search}%' OR prn LIKE '%{search}%'
                """
            sql+=f""" limit {limit} offset {offset} """
            query.execute(sql)
            DBdata = query.fetchall()
            return DBdata

    def addStudent(formData):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"""
                INSERT INTO students SET 
                first_name = '{formData['first_name']}', 
                last_name = '{formData['last_name']}', 
                mobile_number = '{formData['mobile_number']}', 
                standard = '{formData['standard']}', 
                section = '{formData['section']}', 
                age = '{formData['age']}', 
                prn = '{formData['prn']}'
            """
            query.execute(sql)
            db.commit()

    def fetchStudent(student_id):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"SELECT first_name, last_name, mobile_number, standard, section, age, prn FROM students WHERE id = '{student_id}'"
            query.execute(sql)
            db.commit()
            formData = query.fetchone()
            return formData

    def updateStudent(formData,student_id):
        db = getDBConnection()
        print("\n")
        print(formData)
        print("\n")
        with db.cursor() as query:
            sql = f"""UPDATE students SET 
                first_name = '{formData['first_name']}', 
                last_name = '{formData['last_name']}', 
                mobile_number = '{formData['mobile_number']}', 
                standard = '{formData['standard']}', 
                section = '{formData['section']}', 
                age = '{formData['age']}', 
                prn = '{formData['prn']}'
                WHERE id = '{student_id}';"""
            query.execute(sql)
            db.commit()

    def validatePRN(prn):
        db = getDBConnection()
        query = db.cursor()
        sql = f"select prn from students where prn = '{prn}'"
        query.execute(sql)
        db.commit()
        prn = query.fetchone()
        return prn

    def validateMobile(mobile_number):
        db = getDBConnection()
        query = db.cursor()
        sql = f"select mobile_number from students where mobile_number = '{self.formData['mobile_number']}'"
        query.execute(sql)
        db.commit()
        mobile_number = query.fetchone()
        return mobile_number

    def deleteStudent(student_id):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"DELETE FROM students WHERE id = '{student_id}'"
            query.execute(sql)
            db.commit()
        
    def studentDetails(student_id):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"SELECT first_name, last_name, mobile_number, standard, section, age, prn FROM students WHERE id = '{student_id}'"
            query.execute(sql)
            db.commit()
            details = query.fetchone()
            return details
        
    def importStudents(studentsData):
        db = getDBConnection()
        with db.cursor() as query:
            sql = "INSERT INTO students (first_name, last_name, mobile_number, standard, section, age, prn) VALUES "
            for studentData in studentsData:
                sql += f"('{studentData['first_name']}', '{studentData['last_name']}', '{studentData['mobile_number']}', '{studentData['standard']}', '{studentData['section']}', '{studentData['age']}', '{studentData['prn']}'),"
            sql += ";"
            sql = sql.replace(",;", ";")
            
            query.execute(sql)
            db.commit()
            
    
    def unique_PRN_Mobile(prn, mobile_number):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"SELECT id FROM students WHERE prn = '{prn}' OR mobile_number = '{mobile_number}'"
            query.execute(sql)
            db.commit()
            if query.fetchone() == None:
                return True
            return False 
    
    def totalStudent():
        db = getDBConnection()
        with db.cursor() as query:
            sql = "SELECT count(id) as total FROM students"
            query.execute(sql)
            db.commit()
            return query.fetchone()
