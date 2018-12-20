from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

import apps.accounts.views as views

app_name = 'accounts'

urlpatterns = [
    url(_(r'^register/$'),
        views.UserRegisterView.as_view(),
        name='register'),
    url(_(r'^login/$'),
        views.UserLoginView.as_view(),
        name='login'),
    url(_(r'^confirm/email/(?P<activation_key>.*)/$'),
        views.UserConfirmEmailView.as_view(),
        name='confirm_email'),
    url(_(r'^status/email/$'),
        views.UserEmailConfirmationStatusView.as_view(),
        name='status'),

]
