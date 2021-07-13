
from django.contrib import admin
from django.urls import path
from blogs.views import homepage

urlpatterns = [
    path('site-admin-9281/', admin.site.urls),
    path('', homepage),

]
