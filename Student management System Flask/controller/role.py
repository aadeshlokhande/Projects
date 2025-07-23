from flask import render_template, request, redirect,url_for
from Config.DataBaseConnection import getDBConnection, closeDBConnection
from controller.common.header import header
from model.rolesql import roleModel
from model.menusql import MenuModel


class Role():  
    def getList():
        error = {}
        data = {'menus' : header()}
        allRoles = roleModel.fetchAllMenu()
        return render_template("role/role.html", data = data, roles = allRoles)

    def addRole():
        data = {'menus' : header()}
        error = {}
        formvalue = {}
        allMenus = MenuModel.fetchAllMenu()

        if request.method == "POST":
            role = request.form.get("name")
            allPermissions = request.form.getlist('permission')
            roleData = {"name":role, "permissions":allPermissions}
            roleData["id"] = False
            roleModel.addRole(roleData)
        return render_template("role/form.html",data = data, error = error, formValue = formvalue, menus = allMenus)
    
    def details():
        data = {'menus' : header()}
        id = request.args.get("role_id")
        dbData = roleModel.roleDetails(id)
        print(dbData)
        return render_template("role/details.html", data = data, formdata = dbData)

    def editRole():
        data = {'menus' : header()}
        # print(header())
        error = {}
        formvalue = {}
        allMenus =  MenuModel.fetchAllMenu()
        id = request.args.get("role_id")
        # print(allMenus)
        data["id"] = id
        data["roles"] = roleModel.getRole(id)
        
        data["roles"]["permissionsLen"] = len(data["roles"]["permissions"])
        if request.method=="POST":
            print()
            role = request.form.get("name")
            allPermissions = request.form.getlist('permission')
            roleData = {"name":role, "permissions":allPermissions}
            roleData["id"] = id
            roleModel.addRole(roleData)
            return redirect(url_for(f'edit_role',role_id=id))
        formvalue['name']=data["roles"]['roles']["name"]
        if request.form.get("name") is not None:
            formvalue['name']=request.form.get("name")
        return render_template("role/form.html",data = data, error = error, formValue = formvalue, menus = allMenus)

    def delMenu():
        data = {'menus' : header()}
        id = request.args.get("role_id")
        roleModel.delRole(id)
        return redirect(url_for('role'))