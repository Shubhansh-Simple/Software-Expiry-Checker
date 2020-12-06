from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsOwnerRequest(permissions.BasePermission):
    '''Is this request is coming from owner'''

    def has_permission(self,request,view):
        '''Requested user is the owner of thing'''

        user = get_user_model().objects.get(pk=request.user.id)
        print('User id - ',request.user.id)
        print('Permission side username - ',user)

        if request.user == user:
            return True
        return False
