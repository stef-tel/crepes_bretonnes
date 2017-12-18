"""
Definition of urls for crepes_bretonnes.
"""

from django.conf.urls import include, url
from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', crepes_bretonnes.views.home, name='home'),
    # url(r'^crepes_bretonnes/', include('crepes_bretonnes.crepes_bretonnes.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^accueil$', views.home), essai git
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^couleurs', views.couleurs),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^article/(\d+)$', views.lire, name='lire'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^addArticle$', views.addArticle, name='addArticle'),
    url(r'^whoami', views.whoami),
    
]
