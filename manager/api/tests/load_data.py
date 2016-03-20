import autofixture


class Loader():

    def __init__(self):
        self.events = None
        self.admins = None
        self.users = None

    def loadModels(self):
        self.admins = autofixture.create('auth.User', 5, field_values={'is_superuser': True})
        self.users = autofixture.create('auth.User', 30, field_values={'is_superuser': False})
        self.events = autofixture.create('event.Event', 5)
