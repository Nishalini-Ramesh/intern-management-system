from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('growtern.urls')),  # Assuming your app name is 'growtern'
]
