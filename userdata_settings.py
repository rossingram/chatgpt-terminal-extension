import json
import os
from sys import platform


class UserData:
    def __init__(self):
        self.chatgpt_token = ""
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            self.user_data_path = "user_pref.json"
        elif platform == "win32":
            self.user_data_path = "user_pref.json"

    def check_user_file_exists(self):
        """
        Checks if there is a user file
        :return: (boolean) Returns result if path exists or not.
        """
        if os.path.exists(self.user_data_path):
            return True
        else:
            return False

    def load_user_data(self):
        """
        Loads the user data to run the application
        """
        if os.path.exists(self.user_data_path):
            with open(self.user_data_path, 'r') as f:
                data = json.load(f)
                self.chatgpt_token = data["chatgpt_token"]
                f.close

    def write_user_data_file(self):
        """
        Writes the user data to manage the user's personal data
        """
        userdata = {
            "chatgpt_token":self.chatgpt_token
        }
        with open(self.user_data_path, 'w') as json_file:
            json.dump(userdata, json_file, indent=4, sort_keys=True)
            json_file.close()
