from flask import render_template,request, redirect,url_for, session
from Config.DataBaseConnection import getDBConnection, closeDBConnection
from controller.common.header import header

def abc():
    print("hello")
    return "this is my api"

def main():
    error = {}
    formData = {}
    query = ""
    if request.method=="POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")
        formData = {"name": name, "username" : username, "email" : email, "password" : password, "cpassword" : cpassword}
        if name == "":
            error["name_error"] = "Name is required"

        if username == "":
            error["username_error"] = "username is required"

        if email == "":
            error["email_error"] = "email is required"

        if password == "":
            error["password_error"] = "password is required"
        
        if cpassword == "":
            error["cpassword_error"] = "cpassword is required"
        
        
        db = getDBConnection()
        query = db.cursor()
        
        sql = f"select username from users where username = '{username}'"
        query.execute(sql)
        if (query.fetchone()):
            error["dup_user_error"] = "user already exist"
            print("user already exist")

        sql = f"select email from users where email = '{email}'"
        query.execute(sql)
        if (query.fetchone()):
            error["dup_email_error"] = "email already exist"
            


        if password!=cpassword :
            error["cpassword_error"] = "confirm is not matched with passsword"
        
        print(error)
        if len(error)==0:
            db = getDBConnection()
            query = db.cursor()
            sql = f"""INSERT INTO users SET 
            name = '{formData['name']}',
            username = '{formData['username']}',
            email = '{formData['email']}',
            password = '{formData["password"]}'"""
            query.execute(sql)
            db.commit()

    return render_template("index.html", title="My web page", error = error, formData = formData)

def userLogin():
    error = {}
    formData = {}
    loginStatus = 0
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        formData = {"username":username, "password" : password}

        if username == "":
            error["username"] = "username is required"
        
        if password == "":
            error["password"] = "password is required"

        db = getDBConnection()
        query = db.cursor()
        sql = f"SELECT id, username, password,role_id FROM users WHERE username = '{username}'"
        query.execute(sql)
        userData = query.fetchone()
        db.commit()

        if userData is not None:
            if userData['password'] == password:
                session["username"] = username
                session["id"] = userData['id']
                session["role_id"] = userData['role_id']
                return redirect(url_for("dashboard"))
            else:
                error["invalid_password"] = "incorrect password"
        else:
            error["invalid_user"] = "user not found"

    return render_template("login.html", login = loginStatus)
# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

def addStudent():
    formData = {}
    error = {}
    data = {'title' : "Add Students", 'menus': header()} 

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        mobile_number = request.form.get("mobile_number")
        standard = request.form.get("standard")
        section = request.form.get("section")
        age = request.form.get("age")
        prn = request.form.get("prn")
        
        formData = {"first_name" : first_name, "last_name" : last_name, "mobile_number" : mobile_number, "standard" : standard, "section" : section, "age" : age, "prn" : prn}

        if first_name == "":
            error["first_name_error"] = "First Name is required"

        if last_name == "":
            error["last_name_error"] = "Last Name is required"

        if mobile_number == "":
            error["mobile_number_error"] = "Mobile Number is required"

        if standard == "":
            error["standard_error"] = "Standard is required"

        if section == "":
            error["section_error"] = "Section is required"

        if age == "":
            error["age_error"] = "Age is required"

        if prn == "":
            error["prn_error"] = "PRN is required"
        
        db = getDBConnection()
        query = db.cursor()

        sql = f"select prn from students where prn = '{prn}'"
        query.execute(sql)
        if (query.fetchone()):
            error["dub_prn_error"] = "PRN already exist"
        
        sql = f"select mobile_number from students where mobile_number = '{mobile_number}'"
        query.execute(sql)
        if(query.fetchone()):
            error["dub_mobile_error"] = "Mobile Number already exist"
        
        print(error)
        print(formData)
        if ("" not in [first_name, last_name, mobile_number, standard, section, age, prn]) and (len(error)== 0):
            db = getDBConnection()
            query = db.cursor()
            sql = f"""INSERT INTO students SET first_name = '{formData['first_name']}', last_name = '{formData['last_name']}', mobile_number = '{formData['mobile_number']}', standard = '{formData['standard']}', section = '{formData['section']}', age = '{formData['age']}', prn = '{formData['prn']}'"""
            query.execute(sql)
            db.commit()
            print("Data store successfuly")
        else:
            print("1", "" not in [first_name, last_name, mobile_number, standard, section, age, prn])
            print(error is None)

    return render_template("addstudent.html", error = error, formData = formData, data=data )





# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
def viewStudent():
    pass

def editStudent(id):
    return f"this is {id}"

def deleteStudent(id):

    db = getDBConnection()
    query = db.cursor()
    sql = f"""DELETE FROM students where id='{id}'"""
    query.execute(sql)
    db.commit()     
    # print("student id = ",id)
    closeDBConnection(db)

    return render_template("studentdashboard.html")
    


# <a href="/deletestudent?student_id={{data.id}}" class="btn btn-danger">Delete</a>
# def deleteStudent():
#     return request.args.get('student_id')

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩

def students():
    data = {'title' : "Students", 'menus': header()} 
    db = getDBConnection()
    query = db.cursor()
    sql = """SELECT id,first_name, last_name, mobile_number, standard, section, age, prn FROM students"""
    query.execute(sql)
    DBdata = query.fetchall()
    db.commit()
    print(DBdata)
    closeDBConnection(db)

    return render_template("students.html", data=data, DBdata = DBdata)





# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩
def dashboard():
    
    data = {'title' : "Dashboard", 'menus': header()} 
    if not session:
        return redirect(url_for("userLogin"))
    return render_template("dashboard.html", data = data)

def logout():
    session.pop('id')
    session.pop('username')
    return redirect(url_for("userLogin"))





