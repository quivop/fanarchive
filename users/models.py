from authtools.models import AbstractNamedUser, UserManager

# Custom user manager and model

class FicUserManager(UserManager):
    pass

class FicUser(AbstractNamedUser):
    objects = FicUserManager()
    pass
