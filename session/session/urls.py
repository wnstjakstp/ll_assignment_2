from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', home)
]


