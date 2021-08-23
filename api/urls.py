from rest_framework import routers
from django.urls import path
from .views import ClientViewSet, StatusViewSet, ProjectList, ProjectPutView, InvoiceViewSingle, InvoiceView, PostClient, AddProject, ProjectTypeViewSet, ArtikelViewSet, ProjectUpdateView, InvoiceStatusViewSet, InvoiceAll, CrewAll, SkillAll, TemplateViewSet, InvoiceNumberView
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

router.register(r'invoicestatus', InvoiceStatusViewSet)
router.register(r'artikel', ArtikelViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'status', StatusViewSet)
router.register(r'types', ProjectTypeViewSet)
router.register(r'templates', TemplateViewSet)
router.register(r'invoice-number', InvoiceNumberView)

urlpatterns = [  
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('projects/', ProjectList.as_view(), name='projects'),
    path('addProject/', AddProject.as_view(), name='addProjects'),
    path('kunden/', PostClient.as_view(), name='kunden'),
    path('invoices/', InvoiceViewSingle.as_view(), name='invoices'),
    path('invoicesall/', InvoiceAll.as_view(), name='invoicesAll'),
    path('crew/', CrewAll.as_view(), name='crew'),
    path('skill/', SkillAll.as_view(), name='skill'),
    path('invoices/<int:pk>', InvoiceView.as_view(), name='invoice'),
    path('projects/<int:pk>/', ProjectPutView.as_view(), name='project'),
    path('projectupdate/<int:pk>/', ProjectUpdateView.as_view(), name='project'),
]

urlpatterns += router.urls


