from flask import render_template, request, redirect,url_for
from Config.DataBaseConnection import getDBConnection, closeDBConnection
from controller.common.header import header
from model.menusql import MenuModel



class Menu:
    def getList():
        error = {}
        data = {'title':"Menu", 'menus': header()}
        allMenus = MenuModel.fetchAllMenu()
        print(allMenus)
        return render_template("menu/menu.html", data = data, menus=allMenus)

    def addmenu():
        data = {'menus' : header()}
        error = {}
        name = request.form.get('name',"")
        route = request.form.get('route',"")
        formValues = {"name":name, "route":route}

        if request.method == "POST":
            if name=="":
                error['name_error'] = "name is required"
            if route=="":
                error['route_error'] = "route is required"
            if not MenuModel.uniqueName(name):
                error["dub_name_error"] = "Name already exist"
            if not MenuModel.uniqueRoute(route):
                error['dub_route_error'] = "Route already exist"

        
            if len(error)==0:
                MenuModel.addMenu(formValues)
                return redirect(url_for('getList'))

        return render_template("menu/form.html", data = data, error = error,formValue = formValues)


    def details():
        data = {'menus' : header()}
        id = request.args.get("menu_id")
        print(f"this is {id}")
        dbData = MenuModel.getRole(id)
        return render_template("menu/details.html", data = data, formdata = dbData)


    def delMenu():
        data = {'menus' : header()}
        id = request.args.get("menu_id")
        MenuModel.delmenu(id)
        # print("hello aadesh")
        return redirect(url_for('getList'))
    
    def editMenu():
        data = {'menus' : header()}
        formValues = {}
        error = {}

        idd = request.args.get('menu_id')
        formValues = MenuModel.getRole(idd)
        
        if request.method == "POST":
            name = request.form.get('name')
            route = request.form.get('route')
            if name=="":
                error['name_error'] = "name is required"
            if route=="":
                error['route_error'] = "route is required"
            if not MenuModel.uniqueNameee(idd,name):
                error["dub_name_error"] = "Name already exist"
            if not MenuModel.uniqueRouteee(idd,route):
                error['dub_route_error'] = "Route already exist"

            if len(error)==0:
                MenuModel.update(idd,name,route)
                formValues['name'] = name
                formValues['route'] = route
        return render_template("menu/form.html", data = data, error = error,formValue = formValues)
