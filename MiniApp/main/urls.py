from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('', include('social_django.urls', namespace='social')),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('edit_user/<int:pk>/', Edit_View.as_view(), name='edit_user')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

