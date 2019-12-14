from django.urls import include, path
from rest_framework import routers
from my_web.estudios import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'estudios', views.EstudioViewSet)
router.register(r'collectores', views.CollectoresViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
