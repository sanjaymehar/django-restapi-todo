from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from task.views import RegisterView, Taskk, MyTokenObtainPairView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

router = routers.DefaultRouter()

router.register('api/task', Taskk)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/token/',  MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
