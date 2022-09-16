
# TA module
# manny things will be here.
# copyright: none, this is free and open source!
# written by: lemonsarelimes


from calendar import THURSDAY


users = {

    "hello":{
            "username":"hello",
            "password":"world"
            },

    "world":{
        "username":"test",
        "password":"admin"
            }

}


def check_name_exist(name):
    try: 
        users[name]
        return True
        
    except KeyError:
        return False


def auth(name, password):
    if users[name]['password'] == password:
        return True

    else:
        return False
