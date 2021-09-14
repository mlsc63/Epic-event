from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from api.views import TeamViewSet, ClientViewSet, ContractViewSet, EventViewSet, UserViewSet



router = DefaultRouter()

router.register(r'team', TeamViewSet )
router.register(r'client', ClientViewSet )
router.register(r'contract', ContractViewSet )
router.register(r'event', EventViewSet )
router.register(r'user', UserViewSet )


client_router = routers.NestedSimpleRouter(router, r'client', lookup='client')
client_router.register(r'contract', ContractViewSet, basename='contract')
event_router = routers.NestedSimpleRouter(client_router, r'contract', lookup='contract')
event_router.register(r'event', EventViewSet, basename='event')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(client_router.urls)),
    path('', include(event_router.urls)),

]
