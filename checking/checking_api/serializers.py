from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Checking

class CheckingSerializer(serializers.ModelSerializer):
    '''Serialize link b/w no_of_times with Django User Model'''

    class Meta:
        model = Checking
        fields = ['no_of_times','id']



class UserSerializer(serializers.ModelSerializer):
    '''Serialize Django default user model'''

    class Meta:
        model  = get_user_model()
        fields = ('username',)





















