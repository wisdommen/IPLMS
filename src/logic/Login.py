from src.beans.UserData import UserData


class Login(object):
    """
    This Class contains the logic of login page.
    """

    def __init__(self, username: str, password: str):
        """ Initiate with username and password

        Args:
            username: a string which is username
            password: a string which is password
        """
        self.username = username
        self.password = password
        self.identity = {}

    def get_login(self, user_data_obj: UserData) -> bool:
        """ This method return if the entered user information is valid

        Args:
            user_data_obj: the data object of user data

        Returns: a boolean if the entered user information is valid

        """
        for each in user_data_obj.data_map:
            if each["username"] == self.username and each["password"] == self.password:
                self.identity = each
                if self.identity["is_blocked"] != "true":
                    return True
        return False

    def get_department(self) -> str:
        """ This method returns a string of the department of a certain password and username entered

        Returns: a string of the department of a certain password and username entered

        """
        return self.identity["department"]
