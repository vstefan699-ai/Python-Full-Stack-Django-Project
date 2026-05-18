from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

handler404 = 'core.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', RedirectView.as_view(pattern_name='landing'), name='home'),
]