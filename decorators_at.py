user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"no admin permissons for {user['username']}"
        
    return secure_function

@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password())