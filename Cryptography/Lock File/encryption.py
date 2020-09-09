class GUI_e:

    def __init__(self, username, password):
        self.name = username
        self.Pass = password
        self.types = ['caesar', 'vig', 'rsa']
        self.n = len(self.Pass)
