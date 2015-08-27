from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from MASTER.views import KabupatenViewSet, KecamatanViewSet, KelurahanViewSet


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'kabupatens', KabupatenViewSet)
router.register(r'kecamatans', KecamatanViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'REMBUGDESA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]