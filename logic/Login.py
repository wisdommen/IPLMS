class Login(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.identity = {}

    def get_login(self, user_data_obj):
        for each in user_data_obj.data_map:
            if each["username"] == self.username and each["password"] == self.password:
                self.identity = each
                if self.identity["is_blocked"] != "true":
                    return True
                else:
                    return "Blocked"
        return "Unauthorized"

    def get_department(self):
        return self.identity["department"]
