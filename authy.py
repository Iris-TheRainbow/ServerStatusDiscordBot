import apikey, mail
import random, string, base64
class authy:
    def __init__(self):
        self.authorized = False
        self.psswd = ''

    def authorize(self):
        return self.authorized

    def login(self, password):
        if password == apikey.psswd():
            self.authorized = True
        return self.authorized
    
    def generatePsswd(self):
        text = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=64))
        self.psswd = base64.b64encode(text.encode("utf-8")).decode("utf-8")[:-2]
        mail.SendMessage('iristherainbow25@gmail.com', 'snazzsinclair@gmail.com', 'YOUR DISCORD SSH KEY','THIS IS YOUR KEY FOR DISCORD SSH</br>' + self.psswd, 'THIS IS YOUR KEY FOR DISCORD SSH ' + self.psswd)
        return self.psswd
