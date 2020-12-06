from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Checking(models.Model):

    no_of_times = models.PositiveSmallIntegerField(default=0)
    login_user       = models.OneToOneField( get_user_model() ,on_delete=models.CASCADE )

    def increment(self):
        self.no_of_times += 1
        self.save()
        print('Calling Model\'s method')
    
    def __str__(self):
        return str(self.no_of_times) + ' - ' + str(self.login_user)




