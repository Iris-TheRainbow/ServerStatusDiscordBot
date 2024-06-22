import apikey
class authy:
    def __init__(self):
        self.authorized = False

    def authorize(self):
        return self.authorized

    def login(self, password):
        if password == apikey.psswd():
            self.authorized = True
        return self.authorized