from rest_framework.authtoken import views

from api.apiviews import EventoList, \
    EventoDetalle, \
    EventoSave, \
    UserCreate, \
    LoginView, \
    GetAddress


from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="API EVENTOS",
        default_version='v1',
        description="COORDINADORA EVENTOS",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="correoContact@gmail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/eventos/', EventoList.as_view(),name='Evento_list'),
    path('v1/eventos/<int:pk>', EventoDetalle.as_view(),name='EventoDetalle' ),
    path('v1/eventos/', EventoSave.as_view(),name='evento_save' ),
    path('v3/usuarios/', UserCreate.as_view(),name='usuario_crear'),
    path('v3/getStreets/', GetAddress.as_view(),name='Get_Address'),
    path('v4/login/', LoginView.as_view(),name='LoginView'),
    path('v4/login-drf/', views.obtain_auth_token, name='login-drf'),
    path('swagger-docs/',  schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    ]