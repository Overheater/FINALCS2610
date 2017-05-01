from django.conf.urls import url, include
from django.views.generic import TemplateView

from sneakers import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='sneakers.html'), name='sneakers-home'),
    url(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='sneakers-event'),
    url(r'^swingtime/', include('swingtime.urls')),
]

