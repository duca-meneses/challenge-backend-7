from django.contrib import admin
from django.urls import path, include
from depoimentos.views import DepoimentosViewSet, DepoimentosHomeView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='depoimentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depoimentos-home/', DepoimentosHomeView.as_view(), name='depoimentos-home'),
    path('', include(router.urls))
]
