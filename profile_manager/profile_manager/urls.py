"""
Definition of urls for profile_manager.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/form/$', views.create_profile, name='model_form_upload'),
    url(r'^edit/form/$', views.model_form_edit, name='model_form_edit'),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
