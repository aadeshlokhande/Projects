from flask import session
from model.rolesql import roleModel

def header():
    role_id=session.get('role_id')
    permissions = roleModel.getPermissionByRoleID(role_id)
    # print(var)
    # menu=[
    #     {
    #         "route":"/dashboard/home",
    #         "title":"Home",
    #         "child":[]

    #     }]
    
    menu=[{"route":permission["route"],"title":permission["name"],"child":[]} for permission in permissions]
    print(menu)
        
    return menu
