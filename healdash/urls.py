from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

from landing.views import landing_view

from rest_framework.routers import DefaultRouter
from accounts.views import UserView, ListUsers

router = DefaultRouter()

urlpatterns = [
    url(r'^admin/clearcache/', include('clearcache.urls')), # to clean cache
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('employee/', include('employees.urls')),
    path('account/', include('accounts.urls')),
    path('', landing_view, name='landing_homepage'),
    path('media/<path>', serve,
        {'document_root': settings.MEDIA_ROOT}),
    path('static/<path>', serve,
        {'document_root': settings.STATIC_ROOT}),
] 
