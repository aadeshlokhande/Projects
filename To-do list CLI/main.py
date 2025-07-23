import sqlite3
import pyperclip

conn = sqlite3.connect("database.db")

try:
# if not exist ---->
    conn.execute('''CREATE TABLE  PASSWORDS
                (PLATFORM       TEXT    NOT NULL,
                USERNAME        TEXT     NOT NULL,
                PASSWORD        TEXT     NOT NULL)''')
except Exception as e:
    # print(e)
    pass


print("1) Add Password")
print("2) Show Password")
print("3) Edit Password")


choice1 = int(input("enter your choice = "))
# choice1 = 2
if(choice1==1):
    platform = input("Enter a Platform = ")
    username = input("Enter a Username = ")
    password = input("Enter a password = ")
    conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('{platform}','{username}','{password}');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('fb','asd','passw1');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('fb','sd','passw2');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWOR2D) VALUES ('insta','df','passw3');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('google','dfs','passw4');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('google','sdfs','passw5');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('insta','ssde','passw6');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('google','eee','passw7');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('google','efd','passw8');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('fb','dg','passw9');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('insta','br','passw10');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('insta','bg','passw11');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('fb','gr','passw12');")
    # conn.execute(f"INSERT INTO PASSWORDS (PLATFORM, USERNAME, PASSWORD) VALUES ('google','bb','passw13');")
    conn.commit()
elif(choice1==2):
    data = conn.execute(f"SELECT DISTINCT PLATFORM FROM PASSWORDS;")
    platformDic = {}
    key = 0
    for i in data.fetchall():
        platformDic[key] = i[0]
        key += 1 
    
    for i,j in platformDic.items():
        print(f"Press {i} : {j}")
    
    platform = int(input("Choose your Platform = "))
    data = conn.execute(f"select USERNAME from PASSWORDS where PLATFORM=='{platformDic[platform]}'")
    usernameDic = {}
    key = 0
    for i in data:
        usernameDic[key] = i[0]
        key += 1

   
    for i,j in usernameDic.items():
        print(f"Press {i} : {j}")

    username = int(input("Choose your Username = "))
    data = conn.execute(f"select PASSWORD from PASSWORDS where PLATFORM=='{platformDic[platform]}'")
    passwordsDic = {}
    key = 0
    for i in data:
        passwordsDic[key] = i[0]
        key += 1
    
    print(f"Password : {passwordsDic[username]}")
    pyperclip.copy(passwordsDic[username])
elif(choice1==3):
    platform = input()
    username = input()
    newPassword = input("Enter a new password = ")
    confirmPassword = input("Confirm your password = ")
    if(newPassword==confirmPassword):
        conn.execute(f"UPDATE PASSWORDS set PASSWORD = {newPassword} where PLATFORM=={platform} and USERNAME=={username}")
        conn.commit()
