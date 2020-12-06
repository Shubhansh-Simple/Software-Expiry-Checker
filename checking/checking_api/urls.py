from django.urls import path
from .views import CheckListApiView,CheckUpdateApiView

urlpatterns = [
    path('get/', CheckListApiView.as_view()  ),
    path('set/<int:pk>/', CheckUpdateApiView.as_view()  ),
]

