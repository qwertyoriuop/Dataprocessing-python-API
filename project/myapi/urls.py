from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'citys', views.CityViewSet)
router.register(r'countrys', views.CountryViewSet)
router.register(r'countrylanguages', views.CountryLanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]