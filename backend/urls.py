from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/v1/accounts/', include('apps.accounts.urls', namespace='accounts')),
]
