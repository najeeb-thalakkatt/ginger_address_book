from django.conf.urls import include, url
from django.contrib import admin

from ginger_address_book.views.views import PersonView, GroupView, PersonGroupDetails, SearchView

urlpatterns = [
    # Examples:
    # url(r'^$', 'ginger_address_book.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/$', PersonView.as_view()),
    url(r'^person/(?P<id>[0-9]+)/$', PersonView.as_view()),
    url(r'^group/$', GroupView.as_view()),
    url(r'^group/(?P<id>[0-9]+)/$', GroupView.as_view()),
    url(r'^person_group_details/(?P<id>[0-9]+)/$', PersonGroupDetails.as_view()),
    url(r'^search/$', SearchView.as_view()),
]
