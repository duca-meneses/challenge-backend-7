from django.contrib import admin
from django.urls import include, path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions, routers

from depoimentos.views import DepoimentoHomeView, DepoimentoViewSet
from destinos.views import DestinoHomeView, DestinoViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Api do Jornada Milhas',
        default_version='v1',
        description='ApiRest de viagens desenvolvido por Carlos Eduardo ',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@jornadamilhas.local'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register('depoimentos', DepoimentoViewSet, basename='Depoimentos')
router.register('destinos', DestinoViewSet, basename='Destinos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'depoimentos-home/',
        DepoimentoHomeView.as_view(),
        name='depoimentos-home',
    ),
    path('destinos-home/', DestinoHomeView.as_view(), name='destinos-home'),
    path('', include(router.urls)),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]
