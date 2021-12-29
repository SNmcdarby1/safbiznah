from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

class CheckoutConfig(AppConfig):
    name = 'checkout'

def ready(self):

    import checkout.signals
