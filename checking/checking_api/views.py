from rest_framework import generics,permissions
from .permission import IsOwnerRequest


# local
from ..models import Checking
from .serializers import CheckingSerializer


class CheckListApiView(generics.ListAPIView):
    queryset = Checking.objects.all()
    serializer_class = CheckingSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def get_queryset(self):
        try:
            user = self.request.user
            return Checking.objects.filter(login_user = user)
        except:
            return None


class CheckUpdateApiView(generics.UpdateAPIView):

    queryset = Checking.objects.all()
    serializer_class = CheckingSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def perform_update(self,serializer):
        serializer.save()
        serializer.instance.increment()











