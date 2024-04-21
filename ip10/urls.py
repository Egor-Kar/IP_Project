from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView

from django.urls import path, include
from django.conf import settings
from testapp.views import registration
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from main.views1 import UserAPIView

urlpatterns = [
    path('', include('main.urls'), name="home"),
    path('admin/', admin.site.urls),
    path('registration/', registration, name="reg"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
