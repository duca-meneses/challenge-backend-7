from django.contrib import admin
from django.urls import path, include
from depoimentos.views import DepoimentoViewSet, DepoimentoHomeView
from destinos.views import DestinoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('depoimentos', DepoimentoViewSet, basename='Depoimentos')
router.register('destinos', DestinoViewSet, basename='Destino') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depoimentos-home/', DepoimentoHomeView.as_view(), name='depoimentos-home'),
    path('', include(router.urls))
]
