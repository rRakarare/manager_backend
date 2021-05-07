from rest_framework import routers
from django.urls import path
from .views import ClientViewSet, ProjectViewSet, StatusViewSet, ProjectList, ProjectPutView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [  
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('projects/', ProjectList.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectPutView.as_view(), name='projects'),
]

urlpatterns += router.urls


