
from django.contrib import admin
from django.urls import path, include
from HealthUp_Dj.core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('upload/', views.upload, name='upload'),
    path('prescription/', views.pres_list, name ='pres_list'),
    path('prescription/<int:pk>/', views.delete_pres, name='delete_pres'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)