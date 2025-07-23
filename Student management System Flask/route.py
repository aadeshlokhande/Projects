from controller.user import abc, main, userLogin,dashboard,logout,addStudent,students,render_template
from controller.students import Students
from controller.menu import Menu
from controller.role import Role

def registerRoute(app):
    # Instaciate class here
    students = Students()
    app.add_url_rule("/api/abc", view_func=abc, methods=["POST"])
    app.add_url_rule("/", view_func=main, methods=["GET","POST"])
    app.add_url_rule("/userlogin", view_func=userLogin, methods=["GET","POST"])
    app.add_url_rule("/dashboard", view_func=dashboard, methods=["GET","POST"])
    app.add_url_rule("/logout", view_func=logout, methods=["GET"])

    # app.add_url_rule("/addstudent", view_func=addStudent, methods=["GET", "POST"])
    # app.add_url_rule("/editinfo", view_func=editStudentData, methods=["GET", "POST"])
    # app.add_url_rule("/deletestudent/", view_func=deleteStudent, methods=["GET", "POST"])
    # app.add_url_rule("/deletestudent/<id>", view_func=deleteStudent, methods=["GET", "POST"])

    app.add_url_rule("/students", view_func=students.getList, methods=["GET", "POST"], endpoint="students")
    app.add_url_rule("/students/add", view_func=students.add, methods=["GET", "POST"])
    app.add_url_rule("/students/edit", view_func=students.edit, methods=["GET", "POST"])
    app.add_url_rule("/students/delete", view_func=students.delete, methods=["GET", "POST"])
    app.add_url_rule("/students/details", view_func=students.studentDetails, methods=["GET", "POST"])
    app.add_url_rule("/students/import", view_func=students.importStudents, methods=["GET", "POST"])
    
    app.add_url_rule("/menu", view_func=Menu.getList, methods=["GET", "POST"])
    app.add_url_rule("/menu/add", view_func=Menu.addmenu, methods=["GET", "POST"])
    app.add_url_rule("/menu/details", view_func=Menu.details, methods=["GET", "POST"])
    app.add_url_rule("/menu/delete", view_func=Menu.delMenu, methods=["GET", "POST"])
    app.add_url_rule("/menu/edit", view_func=Menu.editMenu, methods=["GET", "POST"])

    app.add_url_rule("/role", view_func=Role.getList, methods=["GET", "POST"], endpoint="role")
    app.add_url_rule("/role/add", view_func=Role.addRole, methods=["GET", "POST"])
    app.add_url_rule("/role/details", view_func=Role.details, methods=["GET", "POST"], endpoint = "/role/details")
    app.add_url_rule("/role/edit", view_func=Role.editRole, methods=["GET", "POST"],endpoint="edit_role")
    app.add_url_rule("/role/delete", view_func=Role.delMenu, methods=["GET", "POST"], endpoint = "/role/delete")

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("error/not_found.html"), 404  # Ensure you have a 404.html template

