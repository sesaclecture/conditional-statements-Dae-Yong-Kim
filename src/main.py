"""
Implement User Management System
"""
import json
import datetime

def print_all_user():
    print(json.dumps(user_info))

def check_pwd_rule(pwd):
    rule = set("!@#$%^&*")
    pwd_set = set(pwd)
    return bool(rule & pwd_set)

def check_birth_rule(birth):
    year = int(birth[0:4])
    month = int(birth[4:6])
    day = int(birth[6:8])

    cur_year = datetime.datetime.now().year

    return (1850 <= year <= cur_year) and (1 <= month <= 12) and (1 <= day <= 31)

user_info = {
    "kdy": {                            # id
        "name": "kdy",
        "birth": "19990420",
        "pwd": "abcd12345!",            # pwd rule: 10자 이상, 특수문자(!, @, #, $, %, ^, &, *) 포함
        "role": "admin"                 # role: viewer, editor, admin 중 하나
    }
}

print_all_user()

login_id = None
login_pwd = None

while True:
    command = int(input("Enter Command (1: Sign up, 2: Sign in, 3: Udate, 4: Delete, 5: Quit): "))

    match command:
        case 1:
            flag = False

            #id
            while True:
                id = input("Enter your id (q: Quit): ")

                if id == 'q':
                    flag = True
                    break

                if id in user_info:
                    print(f"{id} is already exited!", end="\n\n")
                    continue
                break
            if flag:
                continue
            
            #name
            name = input("Enter your name (q: Quit): ")
            if name == 'q':
                continue

            #birth
            while True:
                birth = input("Enter your birth (ex. 20250828 | q: Quit): ")

                if birth == 'q':
                    flag = True
                    break

                if not (len(birth) == 8 and check_birth_rule(birth)):
                    print(f"{birth} does not satisfy the rule!", end="\n\n")
                    continue
                break
            if flag:
                continue

            #password
            while True:
                pwd = input("Enter your pwd (10글자 이상, 특수문자(!, @, #, $, %, ^, &, *) 포함 | q: Quit): ")

                if pwd == 'q':
                    flag = True
                    break

                if not (len(pwd) >= 10 and check_pwd_rule(pwd)):
                    print(f"{pwd} does not satisfy the rule!", end="\n\n")
                    continue
                break
            if flag:
                continue

            #role
            while True:
                role = input("Enter your role (admin, editor, viewer) | q: Quit): ")

                if role == 'q':
                    flag = True
                    break

                if role in ["admin", "editor", "viewer"]:
                    break
                else:
                    print("Role must be one of: admin, editor, viewer.", end="\n\n")
            if flag:
                continue

            user_info[id] = dict()
            user_info[id]["name"] = name
            user_info[id]["birth"] = birth
            user_info[id]["pwd"] = pwd
            user_info[id]["role"] = role
            print_all_user()

        case 2:
            flag = False

            #id
            while True:
                login_id = input("Enter your id (q: Quit): ")

                if login_id == 'q':
                    flag = True
                    break

                if not login_id in user_info:
                    print(f"{login_id} is not exited!", end="\n\n")
                    continue
                break
            if flag:
                continue

            #password
            while True:
                login_pwd = input("Enter your pwd (q: Quit): ")

                if login_pwd == 'q':
                    flag = True
                    break

                if user_info[login_id]["pwd"] != login_pwd:
                    print(f"{login_pwd} in wrong password!", end="\n\n")
                    continue
                break
            if flag:
                continue

        case 3:
            flag = False

            if login_id is None:
                print("You must log in!", end="\n\n")
                continue

            #id
            while True:
                update_id = input("Enter update id (q: Quit): ")

                if update_id == 'q':
                    flag = True
                    break

                if not update_id in user_info:
                    print(f"{update_id} is not exited!", end="\n\n")
                    continue
                break
            if flag:
                continue

            permition = True

            if user_info[login_id]["role"] == "viewer":
                if update_id != login_id:
                    print("You don't have permition!", end="\n\n")
                    permition = False

            if permition:
                #name
                name = input("Enter update name (q: Quit): ")
                if name == 'q':
                    continue

                #birth
                while True:
                    birth = input("Enter update birth (ex. 20250828 | q: Quit): ")

                    if birth == 'q':
                        flag = True
                        break

                    if not (len(birth) == 8 and check_birth_rule(birth)):
                        print(f"{birth} does not satisfy the rule!", end="\n\n")
                        continue
                    break
                if flag:
                    continue

                #password
                while True:
                    pwd = input("Enter update pwd (10글자 이상, 특수문자(!, @, #, $, %, ^, &, *) 포함 | q: Quit): ")

                    if pwd == 'q':
                        flag = True
                        break

                    if not (len(pwd) >= 10 and check_pwd_rule(pwd)):
                        print(f"{pwd} does not satisfy the rule!", end="\n\n")
                        continue
                    break
                if flag:
                    continue

                #role
                while True:
                    role = input("Enter update role (admin, editor, viewer) | q: Quit): ")

                    if role == 'q':
                        flag = True
                        break

                    if role in ["admin", "editor", "viewer"]:
                        break
                    else:
                        print("Role must be one of: admin, editor, viewer.", end="\n\n")
                if flag:
                    continue

                user_info[update_id]["name"] = name
                user_info[update_id]["birth"] = birth
                user_info[update_id]["pwd"] = pwd
                user_info[update_id]["role"] = role
                print_all_user()

        case 4:
            flag = False

            if login_id is None:
                print("You must log in!", end="\n\n")
                continue

            #id
            while True:
                delete_id = input("Enter delete id (q: Quit): ")

                if delete_id == 'q':
                    flag = True
                    break

                if not delete_id in user_info:
                    print(f"{delete_id} is not exited!", end="\n\n")
                    continue
                break
            if flag:
                continue

            if user_info[login_id]["role"] in ["viewer", "editor"]:
                if delete_id != login_id:
                    print("You don't have permition!", end="\n\n")
                else:
                    login_id = None
                    login_pwd = None
                    user_info.pop(delete_id)
                    print_all_user()
            else:
                if delete_id == login_id:
                    login_id = None
                    login_pwd = None
                user_info.pop(delete_id)
                print_all_user()

        case 5:
            break